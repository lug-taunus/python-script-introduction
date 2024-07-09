import argparse
import pathlib
import sys


def main() -> int:
    """Main function."""

    parser = argparse.ArgumentParser(
        prog="mkdir", description="Create a new directory."
    )
    parser.add_argument("directory", type=pathlib.Path)

    args = parser.parse_args()

    print(f"Creating directory {args.directory.resolve()}:")
    args.directory.mkdir()


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    sys.exit(main())
