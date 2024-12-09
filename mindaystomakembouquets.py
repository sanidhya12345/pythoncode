def checkBlossom(bloomday, m, k):
    b = 0
    count = 0
    for day in bloomday:
        if day == 'x':  # Check for valid 'x' markers
            count += 1
            if count == k:  # Form one bouquet
                b += 1
                count = 0
        else:
            count = 0  # Reset the count if not 'x'
    return b >= m

def binaryHelper(bloomDay, bday, m, k, start, end):
    low = start
    high = end
    result = -1  # To store the minimum number of days
    
    while low <= high:
        mid = (low + high) // 2
        # Mark bloom days less than or equal to mid as 'x'
        for i in range(len(bloomDay)):
            bday[i] = 'x' if bloomDay[i] <= mid else '_'
        
        if checkBlossom(bday, m, k):
            result = mid  # Update result with current mid
            high = mid - 1  # Try for a smaller mid
        else:
            low = mid + 1  # Try for a larger mid
    
    return result

# Example usage
bloomDay = [1, 10, 3, 10, 2]
bday = ['_' for _ in range(len(bloomDay))]
m = 3
k = 1
print(binaryHelper(bloomDay, bday, m, k, min(bloomDay), max(bloomDay)))
