class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = {}
        ans = 0
        lenA = len(nums1)
        lenB = len(nums2)
        lenC = len(nums3)
        lenD = len(nums4)
        
        for i in range(0, lenA):
            x = nums1[i]
            for j in range(0, lenB):
                y = nums2[j]
                
                if x+y not in m:            # if key is not in m then initially add value as 0
                    m[x+y] = 0              # if key is present increment value, if found more occurences
                m[x+y] += 1
                                            # for now, our m dict will be like this {-1: 1, 0: 2, 1: 1} .

        for k in range(0, lenC):
            x = nums3[k]
            for l in range(0, lenD):
                y = nums4[l]
                target = -(x+y)             #target = - (-1+0) = 1 , so negative will be turned to positive and vice versa
                print(ans)
                if target in m:             #target in dict m ? yes then increment ans
                    ans += m[target]
                    
        return ans
        