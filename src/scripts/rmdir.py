import argparse
import pathlib
import sys


def main() -> int:
    """Main function."""

    parser = argparse.ArgumentParser(
        prog="rmdir", description="Remove an empty directory."
    )
    parser.add_argument("directory", type=pathlib.Path)

    args = parser.parse_args()

    print(f"Removing directory {args.directory.resolve()}:")
    args.directory.rmdir()


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    sys.exit(main())
