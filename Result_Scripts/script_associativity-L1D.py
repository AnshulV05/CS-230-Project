import fileinput
import os
import math

# Strings to be replaced
str_set = "#define L1D_SET "
str_way = "#define L1D_WAY "
str_lat = "#define L1D_LATENCY "

# Path to the files
file_path_size= "inc/cache.h"
file_path_inclusivity = "src/cache.cc"

data_points = [(256,3),(128,6),(64,12),(32,24),(16,48)]

# calculate the latency of cache block given size and way
def latency(set, way):
    lat = math.log(way/3,2) + 3
    return lat  

latencies = [latency(i[0], i[1]) for i in data_points]


# The list of the replacement policies to use
replacement_policies = ['lru']

# List of traces to use
traces = ["cadical-high-60K-134B.champsimtrace.xz"]

new_lines = ["int inclusiveness = NONINCLUSIVE"]

# Build and run Champsim for each fixed value of the L1D_way

for j in range(len(data_points)):

    for i, new_line in enumerate(new_lines):

        for repl in replacement_policies:

            with open(file_path_size, 'r') as f1: 
                lines = f1.readlines()
                lines[54] = str_set + str(data_points[j][0]) + "\n"
                lines[55] = str_way + str(data_points[j][1]) + "\n"
                lines[60] = str_lat + str(latencies[j]) + "\n"

            with open(file_path_size, 'w') as f1_w:
                f1_w.writelines(lines)

            with open(file_path_inclusivity, 'r') as f2:

                lines = f2.readlines()
                lines[22] = new_line + ";\n"

            with open(file_path_inclusivity, 'w') as f2_w:
                f2_w.writelines(lines)

            # Build the Champsim executable
            os.system(f"./run.sh {repl} way{data_points[j][1]}")



## Collect the results from the graphs
