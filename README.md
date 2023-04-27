## Team A.K.A- 
Kevin Baua-210050084 

Anshul Verma-210050015 

Akshat Goyal-210050009

# CS-230-Project
## Memory Hierarchy Optimization for SAT-Solvers

The project was done as part of the CS-230 course. 

Our task was to Evaluate different cache hierarchies (different sizes of L1, L2, LLC,inclusive/non-inclusive/Exclusive) and cache replacement policies and compare with a baseline cache hierarchy, and improve cache performance.

We used the champsim simulator.

The traces that we evaluated our program on can be found at- https://www.dropbox.com/sh/xs2t9y4cuqlgrlp/AACpzGOj6BcSB-BUolGaBjbta?dl=0

(Check the last 3 traces of the backend folder)

### Directory Description- 

The final Champsim folder can be downloaded by extracting the ChampSim.zip file.

The results (champsim output txt files and plots) are in the results folder.

The scripts used for getting the results and generating the plots are in the Result_scripts folder.

### Knobs of interest- 
We varied the following parameters and observed the change in IPC and hit rate-

1) Line Size
2) Cache Size- for each of L1,L2 and LLC
3) Cache Associativity- for each of L1,L2 and LLC
4) Cache Inclusion Policies- Inclusive, Exclusive and Non-Inclusive cache hierarchy
5) Replacement Policies- lru, mru, lifo, fifo, random, lfu, segmented_lru

The Inclusion Policies can be toggled by changing the global variable inclusiveness in the cache.cc file. Other variations can be done by changing the respective macros in the cache.h and the champsim.h file.

### Final results-

We were able to achieve an average improvement of almost 6% from the baseline hierarchy (default champsim parameters+lru). We used the parameters line_size=128 and replacement strategy =segmented_lru and number of sets = 32,512,1024(L1,L2,LLC).

### Presentation- 

The presentation we made as a part of out project can be found here- https://docs.google.com/presentation/d/1qyROqspSuc6ZsRb_AsjX4wbj8ZK2yVTB5Fdeao2mMQk/edit#slide=id.g23ab625106d_3_136


### Video-

The link to the video presentation can be found here-


