class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = []                               # keeps track of distinct characters.
        count = 0                              # keeps count of total unique characters.
        for i in s:                            # for every character in string .
            if i in res:                       # if character is present in res array.
                res = res[res.index(i) + 1:]   # remove existing duplicate one from res array by shifting index to next element .
                                               # but append the new duplicate character in res array.
            res.append(i)                      # if character is not present in res array append it in res array.
            count = max(count,len(res))        # max(0, 3) .
        return count                           # return count