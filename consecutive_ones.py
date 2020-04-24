def maxConsecutiveOnes(x):
    count = 0
    while (x != 0):
        x = (x & (x << 1))
        count = count + 1

    return count


print(maxConsecutiveOnes(12))
