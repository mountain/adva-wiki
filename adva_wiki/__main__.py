import argparse
import json
from pathlib import Path

from .config import load_config
from .server import create_server


def main():
    parser = argparse.ArgumentParser(description="Serve an agent-authored Markdown wiki")
    parser.add_argument("command", nargs="?", choices=("serve", "sources"), default="serve")
    parser.add_argument("--config", type=Path, default=Path("wiki.toml"))
    args = parser.parse_args()
    try:
        config = load_config(args.config)
        if args.command == "sources":
            print(json.dumps({
                "content_dir": str(config.content_dir),
                "projects": config.projects, "feeds": config.feeds,
            }, indent=2))
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
