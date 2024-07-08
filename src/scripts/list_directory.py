import argparse
import pathlib
import sys


def main() -> int:
    """Main function."""

    parser = argparse.ArgumentParser(
        prog="list-directory", description="List the contents of a given directory."
    )
    parser.add_argument("directory", type=pathlib.Path)

    args = parser.parse_args()

    print(f"Listing contents in directory {args.directory.resolve()}:")
    for child in args.directory.iterdir():
        print(f"- {child}")


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    sys.exit(main())
