# Lists files in the subdirectory specified on the command line
import sys, os, glob

def main():
    # Verify that user supplies subdirectory as command line argument(s)
    if len(sys.argv) < 2:
        print(f'''
                Must provide subdirectory name.   
                Usage: python3 {sys.argv[0]} subdirectory
                ''')
        sys.exit(1) # terminate the program

    # Verify that subdirectory exists
    subdir = sys.argv[1]
    if not os.path.exists(subdir):
        print(f'{subdir} does not exist.')
        sys.exit(1)

    # Iterate through all subdirectory contents.  Recsursive allows us
    # to go to sub-subdirectories. ** needed for recursive mode.
    # Change * to *.txt to match only files with .txt extension    
    for filename in glob.glob(f'./{subdir}/**/*', recursive=True):
        if os.path.isfile(filename):
            print(filename)

if __name__ == '__main__':
    main()

