from collections import defaultdict
import heapq
import matplotlib.pyplot as plt

# Recommendation engine with scoring and plotting
class RecommendationEngine:
    def __init__(self):
        self.user_profiles = {}  # User ID -> set of product IDs
        self.product_graph = defaultdict(dict)  # Product ID -> {related_product: weight}

    def add_interaction(self, user_id, product_id):
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = set()
        for other_product in self.user_profiles[user_id]:
            if other_product != product_id:
                self.product_graph[product_id][other_product] = self.product_graph[product_id].get(other_product, 0) + 1
                self.product_graph[other_product][product_id] = self.product_graph[other_product].get(product_id, 0) + 1
        self.user_profiles[user_id].add(product_id)

    def recommend(self, user_id, top_n=5):
        if user_id not in self.user_profiles:
            return []

        seen = self.user_profiles[user_id]
        scores = defaultdict(int)

        for product in seen:
            for neighbor, weight in self.product_graph[product].items():
                if neighbor not in seen:
                    scores[neighbor] += weight

        heap = [(-score, product) for product, score in scores.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(top_n, len(heap)))]

# Simulate interactions
engine = RecommendationEngine()
interactions = [
    ("user1", "A"), ("user1", "B"),
    ("user2", "B"), ("user2", "C"), ("user2", "D"),
    ("user3", "A"), ("user3", "C"), ("user3", "E"),
    ("user4", "B"), ("user4", "E"), ("user4", "F"),
    ("user5", "C"), ("user5", "D"), ("user5", "F"),
]

# Track recommendations for plotting
recommendation_counts = {}

for user, product in interactions:
    engine.add_interaction(user, product)

# Generate recommendations and count them
for user_id in engine.user_profiles:
    recs = engine.recommend(user_id, top_n=3)
    for rec in recs:
        recommendation_counts[rec] = recommendation_counts.get(rec, 0) + 1

# Plotting recommendations frequency
products = list(recommendation_counts.keys())
counts = [recommendation_counts[product] for product in products]

plt.figure(figsize=(10, 6))
plt.bar(products, counts, color='skyblue')
plt.title("Frequency of Product Recommendations")
plt.xlabel("Product")
plt.ylabel("Times Recommended")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
