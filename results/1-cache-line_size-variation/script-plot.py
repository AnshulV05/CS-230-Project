import matplotlib.pyplot as plt
import os

ipc = [0,0,0,0,0,0]
hits = [0,0,0,0,0,0]

x_axis = [16,32,64,128,256,512] 

for filename in os.listdir("1802"):
    for a in range(len(x_axis)):
        if filename.endswith(f"-line{x_axis[a]}.txt"):
            # Extract the line size from the filename
            line_size = a

            # Open the file and extract the IPC and L1 hits
            with open(os.path.join("1802", filename)) as f:
                lines = f.readlines()
                ipc[a] = float(lines[27].split()[4])
                hits[a] = float(lines[28].split()[5])
                # print(a, hits[a])
x = [4,5,6,7,8,9]

# Plot the IPC graph
f1 = plt.plot(x, ipc)
plt.xticks(x)
plt.xlabel("Log(Line Size)", fontweight='bold', fontsize= 15)
plt.ylabel("IPC", fontweight='bold', fontsize= 15)
t = plt.title("IPC vs. Line Size", weight = "bold", fontsize= 20)
plt.grid("on")
plt.show()
# plt.savefig("134_ipc.png")

# Plot the L1 hits graph
f2 = plt.plot(x, hits)
plt.xticks(x)
plt.xlabel("Log(Line Size)", fontweight='bold', fontsize= 15)
plt.ylabel("L1 Hits", fontweight='bold', fontsize= 15)
plt.title("L1 Hits vs. Line Size", weight = "bold", fontsize= 20)
plt.grid("on")
plt.show()
# plt.savefig("134_hits.png")

