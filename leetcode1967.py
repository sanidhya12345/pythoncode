# bruteforce approach:

def numOfStrings(patterns,word):
        poss_subs=[]
        for i in range(0,len(word)):
            for j in range(i,len(word)):
                poss_subs.append(word[i:j+1])
        count=0
        for i in patterns:
            if i in poss_subs:
                count+=1
        return count

#second approach

def numOfStrings2(patterns,word):
        count=0
        for i in patterns:
            if i in word:
                count+=1
        return count