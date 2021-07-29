class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                                                  # consider nums = [2,7,11,15], target = 9 
        m = {}                                    # used to store indexes of nums which fulfills the target
        n = len(nums)                             
        for i in range(0, n):                    
            goal = target - nums[i]               # go through each element in nums and update the goal variable, if target = 9, then goal will be: 9-2 , 9-7 ,9-11, 9-15 ;      
            if(goal in m):                        # if the caluclated goal is in m dictionary 
                return [m[goal], i]               # return the index i and goal index of dictionary 'm'
            m[nums[i]] = i                        # if goal not in 'm' then dictionay of array m[nums[i]] is set to i 
        