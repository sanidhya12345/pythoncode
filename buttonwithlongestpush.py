import heapq
from collections import defaultdict

def maxCurrencyConversion(initialCurrency, pairs1, rates1, pairs2, rates2):
    def buildGraph(pairs, rates):
        graph = defaultdict(list)
        for (start, end), rate in zip(pairs, rates):
            graph[start].append((end, rate))
            graph[end].append((start, 1 / rate))
        return graph

    def dijkstra(graph, start):
        pq = [(-1, start)]
        maxAmount = {start: 1}
        while pq:
            currentAmount, currency = heapq.heappop(pq)
            currentAmount = -currentAmount
            for neighbor, rate in graph[currency]:
                newAmount = currentAmount * rate
                if newAmount > maxAmount.get(neighbor, 0):
                    maxAmount[neighbor] = newAmount
                    heapq.heappush(pq, (-newAmount, neighbor))
        return maxAmount

    # Build graphs for each day
    graph1 = buildGraph(pairs1, rates1)
    graph2 = buildGraph(pairs2, rates2)

    # Run Dijkstra's algorithm on each graph
    maxAmountDay1 = dijkstra(graph1, initialCurrency)
    maxAmountDay2 = defaultdict(float)
    
    # Day 2: Use the results of Day 1 as initial amounts
    for currency, amount in maxAmountDay1.items():
        day2Amounts = dijkstra(graph2, currency)
        for endCurrency, day2Amount in day2Amounts.items():
            maxAmountDay2[endCurrency] = max(maxAmountDay2[endCurrency], amount * day2Amount)
    
    return maxAmountDay2[initialCurrency]

# Example usage
initialCurrency = "EUR"
pairs1 = [["EUR", "USD"], ["USD", "JPY"]]
rates1 = [2.0, 3.0]
pairs2 = [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]]
rates2 = [4.0, 5.0, 6.0]

print(maxCurrencyConversion(initialCurrency, pairs1, rates1, pairs2, rates2))  # Output: 720.0
