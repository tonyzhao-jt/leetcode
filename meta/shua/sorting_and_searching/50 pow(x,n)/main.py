class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n < 0: x, n = 1/x, -n

        ans = 1
        while n:
            if n & 1:
                ans *= x 
            x *= x 
            n >>= 1
        return ans 
    

# original dp 
# if n == 0:
#     return 1
# if n % 2 == 1:
#     return myPow(x, n-1) * x 
 
# else;
#    tmp = myPower(x, n-1)
#    return tmp * tmp;
