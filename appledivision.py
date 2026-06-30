def solve():
    n = int(input())
    weights = list(map(int, input().split()))
    
    # Ye function recursively minimum difference find karega
    def find_min_diff(index, group1_sum, group2_sum):
        # Base Case: Agar saare apples check ho gaye
        if index == n:
            return abs(group1_sum - group2_sum)
        
        # Option 1: Current apple ko Group 1 mein daalo
        diff1 = find_min_diff(index + 1, group1_sum + weights[index], group2_sum)
        
        # Option 2: Current apple ko Group 2 mein daalo
        diff2 = find_min_diff(index + 1, group1_sum, group2_sum + weights[index])
        
        # Dono options mein se jo minimum difference de, wo return karo
        return min(diff1, diff2)
    
    # Recursion ko 0th index se start karte hain, initial sums 0, 0 hain
    ans = find_min_diff(0, 0, 0)
    print(ans)

solve()