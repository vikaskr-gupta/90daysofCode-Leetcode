class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            n=str(i)
            m=len(n)
            if m % 2 == 0:
                count+=1
        return count
            
