#bruteforce approach it will give tle 

def numberOfSubstrings(s: str) -> int:

    char_count={'a':0,'b':0,'c':0}
    res=0
    i=0;

    for j in range(len(s)):
        char_count[s[j]]+=1

        while char_count['a']>0 and char_count['b']>0 and char_count['c']>0:
            char_count[s[i]]-=1
            i+=1
        
        # the current value of i will give you the count of valid substrings which are ending at j

        res+=i

    return res

def sliding_window(s: str, window: int) -> int:
    char_map = {}
    i = 0
    j = 0
    n = len(s)
    count = 0
    
    while j < n:
        ch = s[j]
        char_map[ch] = char_map.get(ch, 0) + 1
        
        while (j - i + 1) > window:
            c = s[i]
            char_map[c] -= 1
            if char_map[c] == 0:
                del char_map[c]  
            i += 1
        if (j - i + 1) == window:
            if 'a' in char_map and 'b' in char_map and 'c' in char_map:
                count += 1
                
        j += 1
        
    return count

if __name__ == "__main__":
    s = "abcabc"
    final_count = 0
    for k in range(3, len(s) + 1):
        final_count += sliding_window(s, k)
        
    #print(final_count)  # Output: 10
    print(numberOfSubstrings(s))