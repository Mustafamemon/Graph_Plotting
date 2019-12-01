# MH Graph Solver v2.0
First Install Dependencies Using Pipenv install:

    pipenv install
    pipenv shell 

 

To Run:

    python MHGraphCalculator.py


## Proposed System:
We used PyQt5, A Python GUI Library, to design the User Interface for our 'MH Graph Solver'. It takes the provided netsim input files, parses them and plots them using Networkx and Matplotlib.

We first Parse the given netsim files and insert into our networkx graph model that will help us manage the Graph Data Structure. The graph object is then utilized by different functions to calculate Minimum Cost based on required Algorithms.

We can display output of all above mentioned Algorithms. We can also Display Total Minimum Cost of all Methods in a simple table.

In case of Local Clustering Co-efficient, We color coded the vertex color in terms of the Local Clustering Co-efficient.

Higher the Local Clustering Co-efficient of vertex, Darker the color of the respective vertex.

A list of Local Clustering Co-efficient for all vertices is also generated.

**References:** 

http://www.centiserver.org/?q1=centrality&q2=Local_Clustering_Coefficient
https://towardsdatascience.com/graph-algorithms-part-2-dce0b2734a1d
https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.clustering.html#networkx.algorithms.cluster.clustering
https://networkx.github.io/documentation/stable/reference/introduction.html
https://github.com/kfoynt/LocalGraphClustering
