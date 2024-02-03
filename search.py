# Find occurrences of a substring in files in a specified subdirectory.
# usage: python3 search.py substring subdirectory
import sys, os, glob

def main():
    if len(sys.argv) < 3:
        print(f'''
                Two arguments expected.   
                Usage: python3 {sys.argv[0]} substring subdirectory
                ''')
        sys.exit(1) 

    # Verify that subdirectory exists
    pattern = sys.argv[1]
    subdir = sys.argv[2]
    if not os.path.exists(subdir):
        print(f'{subdir} does not exist.'); sys.exit(1)

    # Iterate through all files in subdirecory recursively.   
    for filename in glob.glob(f'./{subdir}/**/*', recursive=True):
        if os.path.isfile(filename):
            # Output line numbers with a match
            with open(filename, 'r') as f:
                for i, line in enumerate(f):
                    if pattern in line:
                        print(f'{filename}:{i}')
                
if __name__ == '__main__':
    main()

