from pathlib import Path
import re
import subprocess


class GitError(Exception):
    pass


class Revisions:
    def __init__(self, content_dir: Path):
        self.content_dir = content_dir

    def run(self, *args: str) -> str:
        try:
            return subprocess.run(
                ["git", "--literal-pathspecs", "-C", str(self.content_dir), *args],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                timeout=10,
            ).stdout.decode("utf-8", errors="replace")
        except (OSError, subprocess.SubprocessError) as error:
            raise GitError("Git history is unavailable") from error

    def relative_path(self, path: Path) -> str:
        root = Path(self.run("rev-parse", "--show-toplevel").strip())
        return path.relative_to(root).as_posix()

    def history(self, path: Path) -> list[dict]:
        output = self.run(
            "log", "-100", "--format=%H%x09%aI%x09%an%x09%s",
            "--", path.relative_to(self.content_dir).as_posix(),
        )
        return [
            dict(zip(("sha", "date", "author", "subject"), line.split("\t", 3)))
            for line in output.splitlines() if line
        ]

    def read(self, path: Path, revision: str) -> str:
        self.validate(revision)
        return self.run("show", f"{revision}:{self.relative_path(path)}")

    def diff(self, path: Path, revision: str) -> str:
        self.validate(revision)
        return self.run(
            "show", "--format=", "--no-ext-diff", "--no-textconv",
            revision, "--", path.relative_to(self.content_dir).as_posix(),
        )

    @staticmethod
    def validate(revision: str):
        if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
            raise ValueError("A full Git commit hash is required")
