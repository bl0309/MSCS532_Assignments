import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        # adjacency list: node -> list of (neighbor, weight, crowd, tip)
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, weight, crowd='medium', tip=''):
        self.adj_list[u].append((v, weight, crowd, tip))

    def dijkstra(self, start, end, learner_mode=False):
        """ 
        Computes path with safety bias (less crowd) and collects instructor tips. 
        """
        if start not in self.adj_list and start != end:
            return [], []

        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        pq = [(0, start)]
        previous = {node: None for node in self.adj_list}
        previous[start] = None
        tips = []

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances.get(current_node, float('inf')):
                continue
            if current_node == end:
                break
            for neighbor, weight, crowd, tip in self.adj_list.get(current_node, []):
                if neighbor not in distances:
                    distances[neighbor] = float('inf')
                    previous[neighbor] = None
                bias = 0 if crowd == 'low' else weight * 0.5  # Penalty for crowd
                distance = current_distance + weight + bias
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                    if learner_mode and tip:
                        tips.append(tip)

        # Reconstruct path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous.get(current)
        path = path[::-1]
        return (path if path and path[0] == start else [], tips)

# Demo script
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4, 'high')
    g.add_edge('A', 'C', 2, 'low', 'Check blind spots')
    g.add_edge('B', 'D', 5, 'medium')
    g.add_edge('C', 'B', 1, 'low')
    g.add_edge('C', 'E', 10, 'high')
    g.add_edge('D', 'E', 2, 'low')
    g.add_edge('E', 'F', 3, 'medium')

    path, tips = g.dijkstra('A', 'F', learner_mode=True)
    print("Safe Path from A to F:", path)
    print("Instructor Tips:", tips)
