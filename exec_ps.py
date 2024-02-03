import subprocess

def main():
    print("Running 'ps ux'")
    result = subprocess.run(['ps', 'ux'], capture_output=True)
        
    # convert result to utf-8 (from bytes)
    result_str = result.stdout.decode('utf-8')
    print(result_str)
    
if __name__ == '__main__':
    main()
