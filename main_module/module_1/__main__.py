import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("root", type=str, help="The root directory to walk.")


def main(args):
    """Prints the files that are inside the container, rooted at the first argument."""
    for dirpath, _, files in os.walk(args.root):
        for f in files:
            print(os.path.join(dirpath, f))


if __name__ == "__main__":
    print("module 1 args:", parser.parse_args(), parser.parse_args().root)
    main(parser.parse_args())
