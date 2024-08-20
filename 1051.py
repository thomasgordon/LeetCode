class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        counter = 0

        for i in range(len(sortedHeights)):
            if sortedHeights[i] != heights[i]:
                counter += 1
        return counter
