import sys
import os

def main(argv):
    """
    Converts specified .txt files to .csv
    Usage: python3 textToCsv.py [<file1.txt> <file2.txt> ...]
    """
    for i in range(1, len(argv)):
        src = argv[i]
        extension = src[-4:]
        if extension == ".txt":
            dest = src[:-4] + ".csv"
            try:
                os.rename(src, dest)
            except FileNotFoundError:
                print("Warning: Source file not found - {}".format(src))

def printUsage():
    print("Usage: python3 textToCsv.py <file1.txt> [<file2.txt> <file3.txt> ...]")

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        printUsage()
        exit()
    main(sys.argv)