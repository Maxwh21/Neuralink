import subprocess
import os

def run_bash_script(script_path):
    # Path to Git Bash executable based on your provided location
    git_bash_path = 'C:\\Users\\MaxW\\AppData\\Local\\Programs\\Git\\usr\\bin\\bash.exe'
    
    # Check if Git Bash path exists
    if not os.path.exists(git_bash_path):
        print(f"Git Bash not found at {git_bash_path}. Please verify the installation path.")
        return None
    
    # Check if the script path exists
    if not os.path.exists(script_path):
        print(f"Script not found at {script_path}. Please verify the script path.")
        return None

    # Run the bash script
    result = subprocess.run([git_bash_path, script_path], capture_output=True, text=True)
    
    # Capture the output and error (if any)
    output = result.stdout
    error = result.stderr

    # Check if there were any errors
    if result.returncode != 0:
        print(f"Error running the bash script: {error}")
        return None
    
    return output

def extract_compression_ratio(output):
    # Extract the compression ratio from the script output
    lines = output.split('\n')
    for line in lines:
        if "Compression ratio" in line:
            ratio = line.split(":")[1].strip()
            return float(ratio)
    return None

def main():
    script_path = 'C:\\Users\\MaxW\\Neuralink\\eval.sh'
    
    # Run the bash script and get the output
    output = run_bash_script(script_path)
    if output is None:
        print("Failed to run the bash script.")
        return
    
    # Print the entire output for debugging purposes
    print("Script Output:\n", output)
    
    # Extract the compression ratio from the output
    compression_ratio = extract_compression_ratio(output)
    if compression_ratio is not None:
        print(f"Compression Ratio: {compression_ratio}")
    else:
        print("Failed to extract the compression ratio from the output.")

if __name__ == "__main__":
    main()
