# bruteforce solutin accepted on leetcode because constraints are small
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
#         n=len(intervals)
#         intervals.sort()

#         print(intervals)
#         j=n-1
#         i=0
#         mergeset=set()
#         mergepossible=0
#         while j>=0:

#             a=intervals[j][0]
#             b=intervals[j][1]

#             while i<j:
#                 c=intervals[i][0]
#                 d=intervals[i][1]

#                 if (c<=a and b<=d):
#                     mergeset.add((a,b))
#                     mergepossible+=1
#                 if (a<=c and d<=b ):
#                     mergeset.add((c,d))
#                     mergepossible+=1
#                 i+=1

#             j-=1
#             i=0
#         print(mergepossible)
#         return len(intervals)-len(mergeset)
    


#Optimized: O(Nlogn) solution
class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_intervals = 0
        max_end = -1
        
        for _, end in intervals:
            if end > max_end:
                remaining_intervals += 1
                max_end = end  
                
        return remaining_intervals