import fileinput
import os

# Path to the cache.cc file
file_path_block = "./inc/champsim.h"
file_path_size = "./inc/cache.h"

str_block_size = "#define BLOCK_SIZE "
str_logblock_size = "#define LOG2_BLOCK_SIZE "

traces = ["134.xz", "1227.xz", "1802.xz"]

# Tuple is (blocksize, logblocksize)
data_points = [(16,4),(32,5),(64,6),(128,7),(256,8),(512,9)]

# Build and run Champsim for each value of inclusiveness
for j in range(len(data_points)):

    with open(file_path_block, 'r') as f1:
        lines = f1.readlines()

        # Replace the 43rd and the 44th line with the new line, ie the cache line size
        lines[42] = str_block_size + str(data_points[j][0]) + "\n"
        lines[43] = str_logblock_size +  str(data_points[j][1]) + "\n"

    with open(file_path_block, 'w') as f1_w:
        f1_w.writelines(lines)

    with open(file_path_size, 'r') as f2:
        lines = f2.readlines()

        if (data_points[j][0] < 64):
            # Replace the 43rd and the 44th line with the new line, ie the cache line size
            if(lines[54][-3] == "*"):
                lines[54] = lines[54][:-2] + str(int(64/data_points[j][0])) + "\n"
                lines[63] = lines[63][:-2] + str(int(64/data_points[j][0])) + "\n"
                lines[72] = lines[72][:-2] + str(int(64/data_points[j][0])) + "\n"
            else:
                lines[54] = lines[54][:-1] + "*" + str(int(64/data_points[j][0])) + "\n"
                lines[63] = lines[63][:-1] + "*" + str(int(64/data_points[j][0])) + "\n"
                lines[72] = lines[72][:-1] + "*" + str(int(64/data_points[j][0])) + "\n"
        else:
            if (lines[54][-3] == "/" or lines[54][-3] == "*"):
                # Replace the 43rd and the 44th line with the new line, ie the cache line size
                lines[54] = lines[54][:-2] + str(int(data_points[j][0]/64)) + "\n"
                lines[63] = lines[63][:-2] + str(int(data_points[j][0]/64)) + "\n"
                lines[72] = lines[72][:-2] + str(int(data_points[j][0]/64)) + "\n"
            else:
                # Replace the 43rd and the 44th line with the new line, ie the cache line size
                lines[54] = lines[54][:-1] + "/" + str(int(data_points[j][0]/64)) + "\n"
                lines[63] = lines[63][:-1] + "/" + str(int(data_points[j][0]/64)) + "\n"
                lines[72] = lines[72][:-1] + "/" + str(int(data_points[j][0]/64)) + "\n"
    with open(file_path_size, 'w') as f2_w:
        f2_w.writelines(lines)

    # Build the Champsim executable
    os.system(f"./build_champsim.sh bimodal no no no no lru 1 line{data_points[j][0]}")

    # Run Champsim with each trace
    for trace in traces:
        os.system(f"./run_champsim.sh bimodal-no-no-no-no-lru-1core-line{data_points[j][0]} 30 30 {trace}")

## Collect the results from the graphs
