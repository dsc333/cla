import sys
import os

def main():
    # Verify that user supplies filename(s) as command line argument(s)
    if len(sys.argv) < 2:
        print(f'''
                Must provide at least one filename.  
                Usage: python3 {sys.argv[0]} file1.txt [file2.txt] ...
                ''')
        sys.exit(1) # terminate the program

    # Iterate through all files in the command line (starting at 1)
    for filename in sys.argv[1:]:
        if not os.path.isfile(filename):
            print(f'{filename} does not exist.')
            continue;   # skip over non-existent file

        # Iterate through current file, keeping track of line count
        count = 0
        with open(filename) as f:
            for line in f:
                count += 1
        print(f'{filename}: {count}')

if __name__ == '__main__':
    main()

