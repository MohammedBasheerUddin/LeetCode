# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1                       # use 2pointer to point start and end of array
        end = n

        while(start < end):             # binary Search logic used
            mid = (start + end)//2      # calculate mid of array
            if (not isBadVersion(mid)): # Check if mid is not a bad version by using isBadVersion which is  already defined API
                start = mid + 1         # if its a good version move mid to next
            else:                       # if its a bad version set end mid and break from loop as condition becomes false
                end = mid
                
        return start                    # start reaches the end so either end or start can be returned
                