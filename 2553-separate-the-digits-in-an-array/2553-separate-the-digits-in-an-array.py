class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
    
        ans = []

        for i in range(len(nums)):
            r = list(str(nums[i]))
            for j in r:
                ans.append(int(j))

        return ans
        