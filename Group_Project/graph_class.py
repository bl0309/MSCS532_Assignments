from collections import defaultdict
import heapq

class Graph:
    """
    Directed weighted graph for road network representation with safety features.
    """
    def __init__(self):
        self.adj_list = defaultdict(list)  # (neighbor, weight, crowd_level, tip)
    
    def add_edge(self, u, v, weight, crowd='low', tip=''):
        if weight < 0:
            raise ValueError("Negative weights not supported")
        self.adj_list[u].append((v, weight, crowd, tip))
    
    def dijkstra(self, start, end, learner_mode=False):
        if start not in self.adj_list and start != end:
            return [], []

        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        pq = [(0, start)]
        previous = {node: None for node in self.adj_list}
        tips = []

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances.get(current_node, float('inf')):
                continue
            if current_node == end:
                break
            for neighbor, weight, crowd, tip in self.adj_list.get(current_node, []):
                bias = 0 if crowd == 'low' else weight * 0.5
                distance = current_distance + weight + bias
                if distance < distances.get(neighbor, float('inf')):
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
        path.reverse()
        return (path if path and path[0] == start else [], tips)
