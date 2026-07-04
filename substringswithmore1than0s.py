import collections
def countsubstringswithmoreones(s):

    freq_dict=collections.defaultdict(int)
    freq_dict[0]=1
    current_prefix_sum=0
    smaller_count=0
    total_substrings=0

    for ch in s:
        if ch=='1':
            current_prefix_sum+=1

            smaller_count+=freq_dict[current_prefix_sum-1]

        else:
            current_prefix_sum-=1
            smaller_count-=freq_dict[current_prefix_sum]
        
        total_substrings+=smaller_count

        freq_dict[current_prefix_sum]+=1
    
    return total_substrings

s="10000000"
print(countsubstringswithmoreones(s))