class Solution:
    
    def findHash(self, s):              # additional function defined for sorting strings
        return ''.join(sorted(s))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}
        
        
        for s in strs:                 
            hashed = self.findHash(s)  # contains sorted version of s and use it as key in dictionary
            if hashed not in m:        # every string is sorted and stored as key 
                m[hashed] = []         # creates list structure within dictionary with key and values as lists     
            m[hashed].append(s)        # add string in list format
                                       # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
                                        
        
        for i in m.values():           # now add dictionary values in already creatd answers list and return answers list
            answers.append(i)
        return answers