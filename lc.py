import sys
import os

def main():
    print(f'Command line arguments: {sys.argv}\n')

    # Verify that user supplies filename as command line argument
    if len(sys.argv) < 2:
        print(f'Missing file.  Usage: python3 {sys.argv[0]} somefile.txt')
        sys.exit(1) # terminate the program

    # Verify that the file exists
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f'{filename} does not exist.')
        sys.exit(1)

    # Iterate through the file, keeping track of line count
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    print(f'{filename}: {count}')

if __name__ == '__main__':
    main()

