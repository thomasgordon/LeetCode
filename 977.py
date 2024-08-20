class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(result) - 1

        for resIdx in range(len(nums) - 1, -1, -1):
            val1 = nums[left]
            val2 = nums[right]

            if abs(val1) > abs(val2):
                result[resIdx] = val1 ** 2
                left += 1
            else:
                result[resIdx] = val2 ** 2
                right -= 1

            resIdx -= 1

        return result

