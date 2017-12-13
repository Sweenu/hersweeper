#!/usr/bin/env python
"""The main entry point."""
import sys


def main():
    try:
        from .cli import main
        sys.exit(main())
    except KeyboardInterrupt:
        exit(130)


if __name__ == '__main__':
    main()
