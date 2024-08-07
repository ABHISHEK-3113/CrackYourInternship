
class Solution:
    def productExceptSelf(self, nums, n):
        
        
        pre = [1]*n 
        suf = [1]*n 
        
        for i in range(1, n):
            pre[i] = pre[i-1]*nums[i-1] 
        
        for i in range(n-2,-1, -1):
            suf[i] = suf[i+1]*nums[i+1] 
        
        
        res = [pre[i]*suf[i] for i in range(n)] 
        
        return res
