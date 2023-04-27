import fileinput
import os
import math

data_points = [(16,12),(32,12),(64,12),(128,12),(256,12)]

# calculate the latency of cache block given size and way
def latency(set, way):
    lat = int(0.0067*set + 0.35852*way + 0.43979)
    return lat   

latencies = [latency(i[0], i[1]) for i in data_points]

str_set = "#define L1D_SET "
str_lat = "#define L1D_LATENCY "


# Path to the files
file_path_size= "./inc/cache.h"
file_path_inclusivity="./src/cache.cc"


# The list of the replacement policies to use
replacement_policies = ['lru']


# Lines to replace
new_lines = ["int inclusiveness = NONINCLUSIVE"]

# Build and run Champsim for each fixed value of the L1D_way

for j in range(len(data_points)):

    for i, new_line in enumerate(new_lines):

        for repl in replacement_policies:

            with open(file_path_size, 'r') as f1: 
                lines = f1.readlines()
                lines[54] = str_set + str(data_points[j][0]) + "\n"
                lines[60] = str_lat + str(latencies[j]) + "\n"

            with open(file_path_size, 'w') as f1_w:
                f1_w.writelines(lines)

            with open(file_path_inclusivity, 'r') as f2:

                lines = f2.readlines()
                lines[22] = new_line + ";\n"

            with open(file_path_inclusivity, 'w') as f2_w:
                f2_w.writelines(lines)

            # Build the Champsim executable
            os.system(f"./run.sh {repl} set{data_points[j][0]}")


## Collect the results from the graphs
