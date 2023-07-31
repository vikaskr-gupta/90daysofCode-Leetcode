class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        A=[]
        for i in nums:
            A.append(i*i)
        return sorted(A)
