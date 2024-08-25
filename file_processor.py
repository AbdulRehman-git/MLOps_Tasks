def count_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        line_count = len(lines)
        
        with open(output_file, 'w') as outfile:
            outfile.write(f"Number of lines: {line_count}\n")
        
        print(f"Line count written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except IOError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    count_lines(input_file, output_file)
