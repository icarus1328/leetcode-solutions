class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        out = []
        gr = 0

        for i in range(len(candies)):
            candy_sum = candies[i] + extraCandies
            gr = max(candy_sum, *candies)
            out.append(candy_sum == gr)
        
        return out