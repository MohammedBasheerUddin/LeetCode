class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort the given array
        people.sort()
        left = 0                    #keeps track of lowest value
        right = len(people)-1       #keeps track of highest value
        boats_no = 0                #keeps track of no of boats used
        
        while(left<=right):         #loop through sorted array
            if left == right:       #condition to carry single person
                boats_no += 1       #increment the no. of boats required
                break               # break will exit the loop and return no. of boats required
                
            if people[left] + people[right] <= limit:   #if lowest + highest value <= given limit then update lowest value (left).                                                     
                left += 1                                
                    
            right -= 1             #right will be updated to second highest value every interval even if condn is statisfied or not.
            boats_no += 1          #boats are incremented after every interval even if condition is satisfied or not
            
        return boats_no