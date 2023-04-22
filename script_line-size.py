import fileinput
import os

# Path to the cache.cc file
file_path = "inc/champsim.h"

# Line number to modify from
line_number = 43

# Lines to replace
new_lines = [["#define BLOCK_SIZE 64", "#define LOG2_BLOCK_SIZE 6"], ["#define BLOCK_SIZE 128", "#define LOG2_BLOCK_SIZE 7"], ["#define BLOCK_SIZE 256", "#define LOG2_BLOCK_SIZE 8"]]

# List of traces to use
traces = ["cadical-high-60K-134B.champsimtrace.xz"]

# Build and run Champsim for each value of inclusiveness
for i, new_line in enumerate(new_lines):
    with open(file_path, 'r') as file:

        lines = file.readlines()

        # Replace the 43rd and the 44th line with the new line, ie the cache line size
        lines[42] = new_line[0] + "\n"
        lines[43] = new_line[1] + "\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)

    # Build the Champsim executable
    os.system("./build_champsim.sh bimodal no no no no lru 1")

    # Run Champsim with each trace
    for trace in traces:
        os.system(f"./run_champsim.sh bimodal-no-no-no-no-lru-1core 30 30 {trace}")
    
    # Rename the files that are present in the results folder
    folder_path = 'results_30M'

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a text file
        if file_name.endswith('core.txt'):
            # Construct the new file name with "inclusive"
            new_file_name = file_name.replace('.txt', f'_{new_line[0][19:]}.txt')

            # Rename the file
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))


## Collect the results from the graphs
