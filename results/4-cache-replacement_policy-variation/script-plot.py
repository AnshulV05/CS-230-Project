import matplotlib.pyplot as plt
import os

policies = ["lru", "mru", "random", "lfu", "fifo", "lifo", "segmented_lru"]

ipc = [0,0,0,0,0,0,0]
hits = [0,0,0,0,0,0,0]

for filename in os.listdir("134"):
    for a in range(len(policies)):
        if filename.endswith(f"-{policies[a]}-1core-.txt"):
            # Extract the line size from the filename
            line_size = a

            # Open the file and extract the IPC and L1 hits
            with open(os.path.join("134", filename)) as f:
                lines = f.readlines()
                ipc[a] = float(lines[27].split()[4])
                hits[a] = float(lines[28].split()[5])
                # print(a, hits[a])



# Plot the IPC graph
f1 = plt.plot(policies, ipc, marker = 'o', markersize=12)
plt.xticks(policies)
plt.xlabel("Replacement-Policy", fontweight='bold', fontsize= 15)
plt.ylabel("IPC", fontweight='bold', fontsize= 15)
t = plt.title("IPC vs. Replacement-Policy", weight = "bold", fontsize= 20)
plt.grid("on")
plt.show()
# plt.savefig("134_ipc.png")

# Plot the L1 hits graph
f2 = plt.plot(policies, hits, marker = 'o', markersize=12)
plt.xticks(policies)
plt.xlabel("Replacement-Policy", fontweight='bold', fontsize= 15)
plt.ylabel("L1 Hits", fontweight='bold', fontsize= 15)
plt.title("L1 Hits vs. Replacement-Policy", weight = "bold", fontsize= 20)
plt.grid("on")
plt.show()
# plt.savefig("134_hits.png")
