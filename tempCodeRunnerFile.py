 graph1 = defaultdict(list)
    graph2 = defaultdict(list)
    
    for i, (start, target) in enumerate(pairs1):
        graph1[start].append((target, rates1[i]))
        graph1[target].append((start, 1 / rates1[i]))
    
    for i, (start, target) in enumerate(pairs2):
        graph2[start].append((target, rates2[i]))
        graph2[target].append((start, 1 / rates2[i]))
    
    dp_day1 = defaultdict(lambda: -math.inf)
    
    dp_day1[initialCurrency] = 1.0
    
    for _ in range(len(graph1)):
        for curr in graph1:
            for neighbor, rate in graph1[curr]:
                dp_day1[neighbor] = max(dp_day1[neighbor], dp_day1[curr] * rate)
    dp_day2 = defaultdict(lambda: -math.inf)
    for currency, amount in dp_day1.items():
        dp_day2[currency] = amount
    for _ in range(len(graph2)): 
        for curr in graph2:
            for neighbor, rate in graph2[curr]:
                dp_day2[neighbor] = max(dp_day2[neighbor], dp_day2[curr] * rate)
    return max(dp_day2.values())