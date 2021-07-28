class Solution:
    def countPrimes(self, n: int) -> int:
        # Math@2
        # Prime numbers for input 10 are 2, 3, 5, 7.
        if n < 2:
            return 0
        
        isPrime = [True] * n                     #set as true for all initially, later change first two elements to false
        isPrime[0] = isPrime[1] = False
                                                 #prime number starts from 2
        for i in range(2,n):
            
            if isPrime[i]:                       #if i index is prime go to next line
                                                 #goes for indexs 4,6,8 etc and set it to false as these are not prime
                for j in range(2*i, n, i):
                    isPrime[j] = False
                                                 #for input 10 isPrime array would be,
        return sum(isPrime)                      #[False, False, True, True, False, True, False, True, False, False]
                                                 #[ 0   ,  1   ,  2  ,  3  ,   4  ,  5  ,   6  ,   7 ,   8 ,    9  ]   
                                                 #sum or count no. of True is 4 
                
        