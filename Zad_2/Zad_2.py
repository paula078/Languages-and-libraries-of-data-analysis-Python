from collections import deque
class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertices(self, new_vertex):
        if new_vertex not in self.graph:
            self.graph[new_vertex] = []

    def remove_vertex(self, vertex):
        try:
            del self.graph[vertex]

            # Usuniecie przyleglych krawedzi
            for key in self.graph.keys():
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)
        except KeyError:
            print("remove_vertex ERROR: The vertex was not found in the graph")

    def add_edge(self, source, destination):  # Graf skierowany
        if source in self.graph and destination in self.graph:
            self.graph[source].append(destination)

    def remove_edge(self, source, destination):
        try:
            self.graph[source].remove(destination)
        except KeyError:
            print("remove_edge ERROR: The source node was not found in the graph")
        except ValueError:
            print("remove_edge ERROR: The destination node was not found in the graph")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_outgoing_neighbors(self, vertex):
        return self.graph[vertex]

    def __str__(self):
        return "\n".join(" ".join(map(str, (key, ':', self.graph[key]))) for key in self.graph)

    def dfs(self, root):
        if root in self.graph:
            return DfsIterator(self.graph, root)
        else:
            raise ValueError(f"The vertex '{root}' does not exist in the graph.")

    def bfs(self, root):
        if root in self.graph:
            return BfsIterator(self.graph, root)
        else:
            raise ValueError(f"The vertex '{root}' does not exist in the graph.")

class DfsIterator:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = set()
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_vertex = self.stack.pop()

            if current_vertex not in self.visited:
                self.visited.add(current_vertex)
                neighbors = sorted(self.graph[current_vertex], reverse=True)
                self.stack.extend(neighbor for neighbor in neighbors if neighbor not in self.visited)
                return current_vertex
        raise StopIteration


class BfsIterator:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = set()
        self.queue = deque([root])

    def __iter__(self):
        return self

    def __next__(self):
        while self.queue:
            current_vertex = self.queue.popleft()

            if current_vertex not in self.visited:
                self.visited.add(current_vertex)
                neighbors = self.graph[current_vertex]
                self.queue.extend(neighbor for neighbor in neighbors if neighbor not in self.visited)
                return current_vertex
        raise StopIteration


graph = Graph()
for node in [1, 2, 7, 8, 3, 6, 9, 12, 4, 5, 10, 11]:
    graph.add_vertices(node)
graph.add_edge(1, 7)
graph.add_edge(1, 2)
graph.add_edge(1, 8)
graph.add_edge(2, 3)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(8, 9)
graph.add_edge(8, 12)
graph.add_edge(9, 10)
graph.add_edge(9, 11)
graph.remove_vertex(44)
graph.remove_edge(2, 66)

print("\nGraph")
print(graph.__str__(), '\n')

print("Neighbors")
for node in [8, 7]:
    print("for {}:".format(node))
    print(graph.get_outgoing_neighbors(node))

print("\nDFS:")
for vertex in graph.dfs(1):
    print(vertex)

print("\nBFS:")
for vertex in graph.bfs(1):
    print(vertex)



