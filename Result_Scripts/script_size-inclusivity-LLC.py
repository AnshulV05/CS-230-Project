import fileinput
import os
import math

data_points = [512,2048,8192]  

# Path to the files
file_path_inclusivity="./src/cache.cc"
file_path_size ="./inc/cache.h"

# The list of the replacement policies to use
replacement_policies = ['lru']

# Line to replace in the cache.h
str_set = "#define LLC_SET NUM_CPUS*"

# Lines to replace
new_lines = [ "int inclusiveness = INCLUSIVE"]

# Build and run Champsim for different INCLUSIVENESS and the EXCLUSIVENESS
for j in range(len(data_points)):

    with open(file_path_size, 'r') as f1:
        lines = f1.readlines()
        lines[72] = str_set + str(data_points[j]) + "\n"
    
    with open(file_path_size, 'w') as f1_w:
        f1_w.writelines(lines)

    for i, new_line in enumerate(new_lines):

        for repl in replacement_policies:

            with open(file_path_inclusivity, 'r') as f2:

                lines = f2.readlines()
                lines[22] = new_line + ";\n"

            with open(file_path_inclusivity, 'w') as f2_w:
                f2_w.writelines(lines)

            # Build the Champsim executable
            os.system(f"./run.sh {repl} inc-l3{new_line[20]}-set-l3{data_points[j]}")


## Collect the results from the graphs
