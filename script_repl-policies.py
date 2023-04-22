import fileinput
import os

# Path to the cache.cc file
file_path = "src/cache.cc"

replacement_policies = ['drrip', 'fifo', 'random', 'lru', 'ship', 'srrip', 'lru']


# List of traces to use
traces = ["cadical-high-60K-134B.champsimtrace.xz"]

for repl in replacement_policies:

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
            new_file_name = file_name.replace('.txt', f'_{repl}.txt')

            # Rename the file
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))


## Collect the results from the graphs
