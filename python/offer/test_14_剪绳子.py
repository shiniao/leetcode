class Solution:
    """
    dp[n] = max(dp[i]*dp[n-i])
    """

    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [i for i in range(n+1)]
        max = 0
        for i in range(4, n+1):
            for j in range(1, i//2+1):
                temp = dp[j] * dp[i-j]
                if max < temp:
                    max = temp
            dp[i] = max

        return dp[n]

    def cuttingRope2(self, n: int) -> int:
        """
        时间：O(n**2)
        空间：O(n)
        """
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            for j in range(i):
                dp[n] = max(dp[i], max((i-j)*j, dp[i-j]*j))
        return dp[n]
