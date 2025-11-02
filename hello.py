import argparse
import logging
import sys

#!/usr/bin/env python3
"""
hello.py - simple sample script

Usage:
    python hello.py --name Alice --times 3 --uppercase
"""


def greet(name: str) -> str:
        """Return a greeting for name."""
        return f"Hello, {name}!"

def main(argv=None) -> int:
        parser = argparse.ArgumentParser(description="Sample hello script")
        parser.add_argument("--name", "-n", default="World", help="Name to greet")
        parser.add_argument("--times", "-t", type=int, default=1, help="How many times to print the greeting")
        parser.add_argument("--uppercase", "-u", action="store_true", help="Uppercase the greeting")
        parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
        args = parser.parse_args(argv)

        logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
        logging.debug("Parsed arguments: %s", args)

        message = greet(args.name)
        if args.uppercase:
                message = message.upper()

        for i in range(max(0, args.times)):
                print(message)

        return 0

if __name__ == "__main__":
        main()