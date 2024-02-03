filename = input('Input file name: ')

try:
    with open(filename, 'r') as f:
        for line in f:
            # strip to remove end-of-line character
            print(line.strip()) 
except IOError:
    print(f'Error reading {filename}.')
        
