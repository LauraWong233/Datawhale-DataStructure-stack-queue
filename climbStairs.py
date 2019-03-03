#斐波那契数列，爬楼梯问题
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0,1,2]
        if n==1:
            return a[1]
        if n==2:
            return a[2]
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]

 ##递归的方法
 class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0,1,2]
        if n==1:
            return a[1]
        if n==2:
            return a[2]
        return self.climbStairs(n-1)+self.climbStairs(n-2)