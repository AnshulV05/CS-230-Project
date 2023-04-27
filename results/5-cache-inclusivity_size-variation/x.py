import matplotlib.pyplot as plt
import os
import numpy as np

L1_sz = [16,64,256]
L2_sz = [256, 1024, 4096]
L3_sz = [512, 2048, 8192]

L = [L1_sz, L2_sz , L3_sz]

IPC = [[0,0,0], [0,0,0], [0,0,0]]

HITS = [[0,0,0],[0,0,0], [0,0,0]]

NAME = ["I", "N", "E"]

trace = "134"

for filename in os.listdir(f"{trace}/L1"):
    for a in range(3):
        for b in range(3):

            if filename.endswith(f"{NAME[a]}-set-{L1_sz[b]}.txt") or filename.endswith(f"{NAME[a]}-set{L1_sz[b]}.txt"):
                # Open the file and extract the IPC and L1 hits
                with open(os.path.join(f"{trace}/L1", filename)) as f:
                    lines = f.readlines()
                    IPC[b][a] = float(lines[27].split()[4])
                    HITS[b][a] = float(lines[28].split()[5])
data = np.array(HITS)
x_labels = L1_sz
bar_labels = ['inclusive', 'non-inclusive', 'exclusive']
y_label = 'HITS'

x = np.arange(len(x_labels))
width = 0.25

fig, ax = plt.subplots()

for i in range(data.shape[1]):
    ax.bar(x - width/2 + i*width/data.shape[1], data[:,i], width/data.shape[1], label=bar_labels[i])

ax.set_ylabel(y_label)
ax.set_xlabel('L1 Sets')
ax.set_title("HITS vs L1 size with different Inclusion Policies")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()
plt.savefig("L1-inc-size-hit")

plt.show()

for filename in os.listdir(f"{trace}/L2"):
    for a in range(3):
        for b in range(3):
            if filename.endswith(f"{NAME[a]}-set-l2{L2_sz[b]}.txt") or filename.endswith(f"{NAME[a]}-set{L2_sz[b]}.txt"):
                # Open the file and extract the IPC and L1 hits
                with open(os.path.join(f"{trace}/L2", filename)) as f:
                    lines = f.readlines()
                    IPC[b][a] = float(lines[27].split()[4])
                    HITS[b][a] = float(lines[42].split()[5])



data = np.array(HITS)
x_labels = L2_sz
bar_labels = ['inclusive', 'non-inclusive', 'exclusive']
y_label = 'HITS'

x = np.arange(len(x_labels))
width = 0.25

fig, ax = plt.subplots()

for i in range(data.shape[1]):
    ax.bar(x - width/2 + i*width/data.shape[1], data[:,i], width/data.shape[1], label=bar_labels[i])

ax.set_ylabel(y_label)
ax.set_xlabel('L2 Sets')
ax.set_title("HITS vs L2 size with different Inclusion Policies")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()
# plt.savefig()
plt.savefig("L2-inc-size-hit")

plt.show()

for filename in os.listdir(f"{trace}/L3"):
    for a in range(3):
        for b in range(3):
            if filename.endswith(f"{NAME[a]}-set-l3{L3_sz[b]}.txt") or filename.endswith(f"{NAME[a]}-set{L3_sz[b]}.txt"):
                # Open the file and extract the IPC and L1 hits
                with open(os.path.join(f"{trace}/L3", filename)) as f:
                    lines = f.readlines()
                    IPC[b][a] = float(lines[27].split()[4])
                    HITS[b][a] = float(lines[49].split()[5])


data = np.array(HITS)
x_labels = L3_sz
bar_labels = ['inclusive', 'non-inclusive', 'exclusive']
y_label = 'HITS'

x = np.arange(len(x_labels))
width = 0.25

fig, ax = plt.subplots()

for i in range(data.shape[1]):
    ax.bar(x - width/2 + i*width/data.shape[1], data[:,i], width/data.shape[1], label=bar_labels[i])

ax.set_ylabel(y_label)
ax.set_xlabel('L3 Sets')
ax.set_title("HITS vs L3 size with different Inclusion Policies")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()
plt.savefig("L3-inc-size-hit")
plt.show()

