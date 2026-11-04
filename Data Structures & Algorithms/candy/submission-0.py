class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Do 2 times linear search to search the uphill from both sides
        [1, 2, 3, 3, 4, 3, 3, 1, 1, 3, 3, 3]
        u: uphill from left
        v: uphill from right
        [., u, u, ., u, ., ., ., ., u, ., .]
        [., ., ., ., v, ., v, ., ., ., ., .]

        Initialize candies as 1 array
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        1. From left, the uphill element should be left + 1
            [1, 2, 3, 1, 2, 1, 1, 1, 1, 2, 1, 1]
        2. From right, the uphill element should be max(right + 1, self)
            [1, 2, 3, 1, 2, 1, 2, 1, 1, 2, 1, 1]
                         ^
                         |
                         max(2, 2)
        """
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            # Uphill
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            # Uphill
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
