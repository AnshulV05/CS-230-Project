import matplotlib.pyplot as plt
import os
import math

ipc_1 = [0,0,0,0,0]
ipc_2 = [0,0,0,0,0]
ipc_3 = [0,0,0,0,0]


IPC = [ipc_1 , ipc_2 , ipc_3]

hits_1 = [0,0,0,0,0]
hits_2 = [0,0,0,0,0]
hits_3 = [0,0,0,0,0]

HITS = [hits_1, hits_2, hits_3]

l1 = [3,6,12,24,48] 
l2 = [2,4,8,16,32]
l3 = [4,8,16,32,64]

L = [l1,l2,l3]

trace = "134"

for filename in os.listdir(f"{trace}/L1"):
    for a in range(5):
        if filename.endswith(f"-way{l1[a]}.txt"):

            # Open the file and extract the IPC and L1 hits
            with open(os.path.join(f"{trace}/L1", filename)) as f:
                lines = f.readlines()
                ipc_1[a] = float(lines[27].split()[4])
                hits_1[a] = float(lines[28].split()[5])

for filename in os.listdir(f"{trace}/L2"):
    for a in range(5):
        if filename.endswith(f"way-l2{l2[a]}.txt"):

            # Open the file and extract the IPC and L2 hits
            with open(os.path.join(f"{trace}/L2", filename)) as f:
                lines = f.readlines()
                ipc_2[a] = float(lines[27].split()[4])
                hits_2[a] = float(lines[42].split()[5])

for filename in os.listdir(f"{trace}/L3"):
    for a in range(5):
        if filename.endswith(f"way-l3{l3[a]}.txt"):
            # Extract the line size from the filename
            line_size = a

            # Open the file and extract the IPC and L3 hits
            with open(os.path.join(f"{trace}/L3", filename)) as f:
                lines = f.readlines()
                ipc_3[a] = float(lines[27].split()[4])
                hits_3[a] = float(lines[49].split()[5])

for a in range(3):
    # Plot the IPC graph
    f1 = plt.bar([str(b) for b in L[a]], IPC[a])
    # plt.xticks([str(b) for b in L[a]])
    plt.xlabel(f"L{a+1} Ways", fontweight='bold', fontsize= 15)
    plt.ylabel("IPC", fontweight='bold', fontsize= 15)
    t = plt.title(f"IPC vs. L{a+1} Ways", weight = "bold", fontsize= 20)
    # plt.grid("on")
    plt.savefig(f"134_ipc_L{a+1}_ways_var-lat.png")
    plt.show()

    # Plot the L1 hits graph
    f2 = plt.bar([str(b) for b in L[a]], HITS[a])
    # plt.xticks([str(b) for b in L[a]])
    plt.xlabel(f"L{a+1} Ways", fontweight='bold', fontsize= 15)
    plt.ylabel(f"L{a+1} Hits", fontweight='bold', fontsize= 15)
    plt.title(f"L{a+1} Hits vs. L{a+1} Ways", weight = "bold", fontsize= 20)
    # plt.grid("on")
    plt.savefig(f"134_hits_L{a+1}_ways_var-lat.png")
    plt.show()
