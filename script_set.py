import fileinput
import os
import math

data_points = [16,32,64,128,256,512]

latencies = [3,4,5,6,7,8]

str_set = "#define L1D_SET "
str_lat = "#define L1D_LATENCY "


# Path to the files
file_path_size= "./inc/cache.h"

file_path_inclusivity="./src/cache.cc"
# Lines to replace for the sizes of the caches and the corresponding latencies


# The list of the replacement policies to use
# replacement_policies = ['drrip', 'fifo', 'random', 'lru', 'ship', 'srrip', 'lfu']

replacement_policies = ['lru']


# Lines to replace
# new_lines = ["int inclusiveness = NONINCLUSIVE",
#              "int inclusiveness = INCLUSIVE",
#              "int inclusiveness = EXCLUSIVE"]

new_lines = ["int inclusiveness = NONINCLUSIVE"]

# Build and run Champsim for each fixed value of the L1D_way

for j in range(len(data_points)):

    for i, new_line in enumerate(new_lines):

        for repl in replacement_policies:

            with open(file_path_size, 'r') as f1: 
                lines = f1.readlines()
                lines[54] = str_set + str(data_points[j]) + "\n"
                lines[60] = str_lat + str(latencies[j]) + "\n"

            with open(file_path_size, 'w') as f1_w:
                f1_w.writelines(lines)

            with open(file_path_inclusivity, 'r') as f2:

                lines = f2.readlines()

                lines[10] = new_line + ";\n"

            with open(file_path_inclusivity, 'w') as f2_w:
                f2_w.writelines(lines)

            # Build the Champsim executable
            os.system(f"./run.sh {repl} set{data_points[j]}")


## Collect the results from the graphs
