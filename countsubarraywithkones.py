from typing import List

def subarrayWithSum(arr: List[int], k: int) -> int:
    count_ones = 0
    freq_map = {0: 1}  
    result = 0
    for num in arr:
        count_ones += num
        target = count_ones - k
        if target in freq_map:
            result += freq_map[target]
        freq_map[count_ones] = freq_map.get(count_ones, 0) + 1
    return result