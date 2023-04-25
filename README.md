# Distance_Vector_Socket_programming



# Bellman-Ford's Single Source Shortest Path Algorithm

This is a Python implementation of Bellman-Ford's single source shortest path algorithm. It calculates the shortest paths from a single source vertex to all of the other vertices in a weighted graph. The implementation includes a `Graph` class, which represents the graph and provides methods for adding edges and calculating the shortest paths using Bellman-Ford's algorithm.

## Dependencies

This implementation has the following dependencies:

- Python 3.x
- `broadcast.py` (included in the same directory as `bellmanford.py`)

The repository consists of the following files:

- `bellmanford.py`: This file contains the `Graph` class, which represents the graph data structure. It contains methods for adding nodes and edges to the graph, checking if a node or edge exists, and getting the neighbors of a node.

- `read.py`: This file contains a helper function that reads a graph from a text file. The text file should contain one edge per line, with the nodes separated by a comma. For example, the file could contain the following lines:

    ```
    A,B
    A,C
    B,D
    C,D
    D,E
    ```

- `node.py`: This file contains the `Node` class, which represents a node in the graph. It contains methods for adding and removing neighbors of the node.


## Usage

The `Graph` class can be used to create a graph and calculate its shortest paths using Bellman-Ford's algorithm. The class constructor takes the following parameters:

- `ip_list`: a list of IP addresses of the nodes in the network
- `routing_table`: a list of lists, where each inner list contains three elements: the source IP, the destination IP, and the distance between them
- `source_ip`: the IP address of the source node
- `port`: the port number to use for broadcasting messages

Here's an example usage:

```
from bellmanford import Graph

ip_list = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]
routing_table = [["192.168.0.1", "192.168.0.2", 5], ["192.168.0.2", "192.168.0.3", 3], ["192.168.0.3", "192.168.0.1", 1]]
source_ip = "192.168.0.1"
port = 8000

graph = Graph(ip_list, routing_table, source_ip, port)
```

The `Graph` class has a method called `printArr`, which can be used to print the shortest paths calculated by Bellman-Ford's algorithm. It takes the following parameters:

- `dist`: a list of the distances from the source node to each of the other nodes in the graph
- `mappedip`: a dictionary mapping each IP address to its corresponding index in the `dist` list
- `source_ip`: the IP address of the source node
- `port`: the port number to use for broadcasting messages
- `iplists`: a list of IP addresses of the nodes in the network

Here's an example usage:

```
graph.printArr(dist, mappedip, source_ip, port, iplists)
```

## License

This code is released under the MIT License. See `LICENSE` file for details.

## Credits

This implementation was developed by [Abhyudai Singh].


1. GeeksforGeeks, Bellman-Ford Algorithm - https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
2. OpenAI, GPT-3.5 Language Model - https://openai.com/blog/gpt-3-5b/ 

Please note that the code used from GeeksforGeeks was modified to fit the requirements of this project.















































