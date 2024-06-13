import sys

def sort_file(input_file, output_file):
    try:
        # Read lines from the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Sort the lines
        sorted_lines = sorted(lines)

        # Write the sorted lines to the output file
        with open(output_file, 'w') as f:
            f.writelines(sorted_lines)

        print(f"The sorted lines from '{input_file}' are written to '{output_file}'.")
    except FileNotFoundError:
        print("File not found. Please check the path to the input file.")
    except PermissionError:
        print("Permission denied. Please make sure you have permission to read the input file or write to the output file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 3:
        print("Use python3 hrusav_L9_T1.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the sorting function
    sort_file(input_file, output_file)

