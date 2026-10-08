import random
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python samplit-vivekccherian.py <filename>", file=sys.stderr)
        sys.exit(1)
    # Read the filename argument (hw_1a)
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if random.random() < 0.01:
                print(line, end="")


if __name__ == "__main__":
    main()


