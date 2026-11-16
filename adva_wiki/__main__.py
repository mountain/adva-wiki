import argparse
import json
from pathlib import Path

from .config import load_config
from .content import markdown_files
from .server import create_server
from .wikify import load_concept_table, wikify


def main():
    parser = argparse.ArgumentParser(description="Serve an agent-authored Markdown wiki")
    parser.add_argument("command", nargs="?", choices=("serve", "sources", "wikify"), default="serve")
    parser.add_argument("--config", type=Path, default=Path("wiki.toml"))
    parser.add_argument("--table", type=Path, help="concept-table TSV for the wikify command")
    parser.add_argument("--write", action="store_true", help="apply wikify to pages in place")
    args = parser.parse_args()
    try:
        config = load_config(args.config)
        if args.command == "sources":
            print(json.dumps({
                "content_dir": str(config.content_dir),
                "projects": config.projects, "feeds": config.feeds,
            }, indent=2))
            return
        if args.command == "wikify":
            if args.table is None:
                parser.error("wikify requires --table")
            phrases = load_concept_table(args.table)
            for name, file in markdown_files(config.content_dir):
                source = file.read_text(encoding="utf-8")
                result = wikify(source, phrases)
                if result == source:
                    continue
                if args.write:
                    file.write_text(result, encoding="utf-8")
                    print(f"wikified {name}")
                else:
                    print(f"would wikify {name}")
            return
        with create_server(config) as server:
            print(f"Serving {config.title} at http://{config.host}:{server.server_port}", flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(2, f"adva-wiki: {error}\n")


if __name__ == "__main__":
    main()
