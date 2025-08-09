
from typing import List

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Find the cheapest price to reach destination city from source city with at most k stops.
    Uses a modified BFS approach to explore paths with increasing number of stops.
    
    Args:
        n: Number of cities
        flights: List of flights [from, to, price]
        src: Source city
        dst: Destination city
        k: Maximum number of stops allowed
    
    Returns:
        Cheapest price to reach destination, or -1 if not possible
    """
    # Create adjacency list representation of the graph
    # graph[i] contains list of (destination, price) for flights from city i
    graph = [[] for _ in range(n)]
    for flight in flights:
        graph[flight[0]].append((flight[1], flight[2]))
    
    # Initialize queue with (city, cost) and track minimum costs to each city
    # queue contains (city, accumulated_cost) pairs to explore
    # minimum_costs[i] tracks the minimum cost to reach city i
    queue = [(src, 0)]
    minimum_costs = [float('inf') for _ in range(n)]
    stops_count = 0
    
    # BFS with limited stops - explore all paths with exactly stops_count stops
    # Continue until we've used all allowed stops (k) or queue is empty
    while queue and stops_count <= k:
        # Process all nodes at the current level (same number of stops)
        queue_size = len(queue)
        for _ in range(queue_size):
            # Get the next city and cost to reach it
            current_city, current_cost = queue.pop(0)
            
            # Explore all outgoing flights from current city
            for next_city, flight_price in graph[current_city]:
                # Calculate new total cost to reach next_city via current_city
                new_cost = flight_price + current_cost
                
                # Skip if we've already found a cheaper path to next_city
                if new_cost >= minimum_costs[next_city]:
                    continue
                
                # Update minimum cost and add to queue for further exploration
                minimum_costs[next_city] = new_cost
                queue.append((next_city, minimum_costs[next_city]))
        # Move to the next level (one more stop)
        stops_count += 1
    
    # Return the minimum cost to reach destination, or -1 if not reachable
    return -1 if minimum_costs[dst] == float('inf') else minimum_costs[dst]