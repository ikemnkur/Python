# Problem: Implement the Breadth-First Search (BFS), Depth-First Search (DFS) 
# and Greedy Best-First Search (GBFS) algorithms on the graph from Figure 1 in hw1.pdf.


# Instructions:
# 1. Represent the graph from Figure 1 in any format (e.g. adjacency matrix, adjacency list).
# 2. Each function should take in the starting node as a string. Assume the search is being performed on
#    the graph from Figure 1.
#    It should return a list of all node labels (strings) that were expanded in the order they where expanded.
#    If there is a tie for which node is expanded next, expand the one that comes first in the alphabet.
# 3. You should only modify the graph representation and the function body below where indicated.
# 4. Do not modify the function signature or provided test cases. You may add helper functions. 
# 5. Upload the completed homework to Gradescope, it must be named 'hw1.py'.

# Examples:
#     The test cases below call each search function on node 'S' and node 'A'
# -----------------------------


# def BFS(start: str) -> list:
#     # START: Your code here
#     return []
#     # END: Your code here

import csv
from collections import defaultdict, deque


# CSV content as a string
csv_content = """
,A,B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,S
A,0,4,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
B,4,0,2,-1,-1,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
C,-1,2,0,-1,-1,-1,-1,4,-1,-1,-1,-1,-1,-1,-1,-1,3
D,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,8,-1,-1,-1,-1,2
E,1,-1,-1,-1,0,3,-1,-1,6,-1,-1,-1,-1,-1,-1,-1,-1
F,-1,2,-1,-1,3,0,-1,-1,-1,6,4,-1,-1,-1,-1,-1,-1
G,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,4,4,-1,10,-1
H,-1,-1,4,-1,-1,-1,-1,0,-1,-1,3,7,-1,-1,-1,-1,-1
I,-1,-1,-1,-1,6,-1,-1,-1,0,1,-1,-1,5,-1,-1,-1,-1
J,-1,-1,-1,-1,-1,6,-1,-1,1,0,3,-1,-1,3,-1,-1,-1
K,-1,-1,-1,-1,-1,4,-1,3,-1,3,0,9,-1,-1,3,-1,-1
L,-1,-1,-1,8,-1,-1,-1,7,-1,-1,9,0,-1,-1,-1,10,-1
M,-1,-1,-1,-1,-1,-1,4,-1,5,-1,-1,-1,0,-1,-1,-1,-1
N,-1,-1,-1,-1,-1,-1,4,-1,-1,3,-1,-1,-1,0,2,-1,-1
P,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,2,0,-1,-1
Q,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,10,-1,-1,-1,0,-1
S,-1,-1,3,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0
"""

# def create_graph_from_csv(file_content):
#     graph = defaultdict(dict)
#     reader = csv.reader(file_content.strip().split('\n'))
#     nodes = next(reader)[1:]  # Skip the first empty cell
#     for i, row in enumerate(reader):
#         for j, weight in enumerate(row[1:]):  # Skip the first cell (node name)
#             if weight != '-1':
#                 graph[row[0]][nodes[j]] = int(weight)
#     return graph

def create_graph_from_csv(file_content):
    graph = defaultdict(dict)
    reader = csv.reader(file_content.strip().split('\n'))
    
    # Get node names from the first row, skipping the first empty cell
    nodes = next(reader)[1:]
    
    for i, row in enumerate(reader):
        node = row[0]  # Current node is the first column of each row
        for j, weight in enumerate(row[1:]):
            if weight != '-1':
                graph[node][nodes[j]] = int(weight)
    
    return graph

def BFS(start: str) -> list:
    graph = create_graph_from_csv(csv_content)
    queue = deque([start])
    visited = set([start])
    expanded = []

    while queue:
        node = queue.popleft()
        expanded.append(node)

        # Get all neighbors
        all_neighbors = list(graph[node].keys())
        
        # Sort neighbors alphabetically
        all_neighbors.sort()

        for neighbor in all_neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return expanded


# def BFS(start: str) -> list:
#     graph = create_graph_from_csv(csv_content)
#     queue = deque([start])
#     visited = set([start])
#     expanded = []

#     while queue:
#         node = queue.popleft()
#         expanded.append(node)

#         neighbors = sorted(graph[node].keys())
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

#     return expanded

def DFS(start: str) -> list:
    # START: Your code here
    return []
    # END: Your code here


def GBFS(start: str) -> list:
    # START: Your code here
    return []
    # END: Your code here


# Test cases
print(BFS('A'))
print(BFS('S'))


# test cases - DO NOT MODIFY THESE
def run_tests():
    # Test case 1: BFS starting from node 'A'
    assert BFS('A') == ['A', 'B', 'E', 'C', 'F', 'I', 'H', 'S', 'J', 'K', 'M', 'G'], "Test case 1 failed"
    
    # Test case 2: BFS starting from node 'S'
    assert BFS('S') == ['S', 'C', 'D', 'B', 'H', 'L', 'A', 'F', 'K', 'Q', 'G'], "Test case 2 failed"

    # # Test case 3: DFS starting from node 'A'
    # assert DFS('A') == ['A', 'B', 'C', 'H', 'K', 'F', 'E', 'I', 'J', 'N', 'G'], "Test case 3 failed"
    
    # # Test case 4: DFS starting from node 'S'
    # assert DFS('S') == ['S', 'C', 'B', 'A', 'E', 'F', 'J', 'I', 'M', 'G'], "Test case 4 failed"

    # # Test case 5: GBFS starting from node 'A'
    # assert GBFS('A') == ['A', 'B', 'F', 'J', 'N', 'G'], "Test case 5 failed"
    
    # # Test case 6: GBFS starting from node 'S'
    # assert GBFS('S') == ['S', 'C', 'B', 'F', 'J', 'N', 'G'], "Test case 6 failed"

    
    
    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
