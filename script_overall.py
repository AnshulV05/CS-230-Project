import fileinput
import os

# Path to the files
file_path_size= "inc/champsim.h"

file_path_inclusivity = "src/cache.cc"

# Lines to replace for the sizes of the caches and the corresponding latencies
l1 = [["#define L1D_WAY 6", "#define L1D_LATENCY 3"], ["#define L1D_WAY 12", "#define L1D_LATENCY 5"], ["#define L1D_WAY 18", "#define L1D_LATENCY 8"]]
l2 = [["#define L2C_WAY 4", "#define L2C_LATENCY 5"], ["#define L2C_WAY 8", "#define L2C_LATENCY 10"], ["#define L2C_WAY 12", "#define L2C_LATENCY 15"]]
l3 = [["#define LLC_WAY 8", "#define LLC_LATENCY 10"], ["#define LLC_WAY 16", "#define LLC_LATENCY 20"], ["#define LLC_WAY 24", "#define LLC_LATENCY 30"]]

# The list of the replacement policies to use
replacement_policies = ['drrip', 'fifo', 'random', 'lru', 'ship', 'srrip', 'lru']

# List of traces to use
traces = ["cadical-high-60K-134B.champsimtrace.xz"]

# List of names
inc = ["non","inc", "exc"]

# Lines to replace
new_lines = ["int inclusiveness = NONINCLUSIVE",
             "int inclusiveness = INCLUSIVE",
             "int inclusiveness = EXCLUSIVE"]

# Build and run Champsim for each fixed value of the L1D_way

for j in range(3):

    for i, new_line in enumerate(new_lines):

        for repl in replacement_policies:

            with open(file_path_size, 'r') as f1: 
                lines = f1.readlines()
                lines[55] = l1[j][0] + "\n"
                lines[60] = l1[j][1] + "\n"

                lines[64] = l2[j][0] + "\n"
                lines[69] = l2[j][1] + "\n"
    
                lines[73] = l3[j][0] + "\n"
                lines[78] = l3[j][1] + "\n"
            with open(file_path_size, 'w') as f1_w:
                f1_w.writelines(lines)

            with open(file_path_inclusivity, 'r') as f2:

                lines = f2.readlines()

                lines[10] = new_line + ";\n"

            with open(file_path_inclusivity, 'w') as f2_w:
                f2_w.writelines(lines)

            # Build the Champsim executable
            os.system(f"./build_champsim.sh bimodal no no no no {repl} 1")

            # Run Champsim with each trace
            for trace in traces:
                os.system(f"./run_champsim.sh bimodal-no-no-no-no-{repl}-1core 30 30 {trace}")

            # Rename the files that are present in the results folder
            folder_path = 'results_30M'

            # Iterate over all files in the folder
            for file_name in os.listdir(folder_path):
                # Check if the file is a text file
                if file_name.endswith('core.txt'):
                    # Construct the new file name with "inclusive"
                    new_file_name = file_name.replace('.txt', f'_way{j}_inc{inc[i]}.txt')

                    # Rename the file
                    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))


## Collect the results from the graphs
