"""Console script for agri_tech."""
import argparse
import sys


def main():
    """Console script for agri_tech."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "agri_tech.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
