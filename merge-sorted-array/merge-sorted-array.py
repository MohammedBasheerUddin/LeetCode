class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # consider for explaination nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        
        one = m-1                                        # if m =3 and n = 3, then one = 2, two = 2
        two = n-1
        
        for i in reversed(range(m+n)):                   # iterate from last to first element m+n times
            if two < 0:                                  # if nums2 array is empty then return
                return
                                                         # sorting by comparing arrays and alter only nums1 array
            if nums1[one] < nums2[two] or one < 0:       # if nums1[2] < nums2[2] .i.e 3 < 6  
                nums1[i] = nums2[two]                    # if yes then set nums[2] to last postion in nums1 array
                two -= 1                                 # decrement only two pointer value
            else:                                        # if if nums1[2] > nums2[0] .i.e 3 > 2
                nums1[i] = nums1[one]                    # if true then set nums1[2] to last second or other position in nums1 array
                one -= 1                                 # decrement only one pointer value
                
                