# brute force : tc = O(2^n
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     ans = fib(n-1) + fib(n-2)
#     return ans

# print("ans = ",fib(5))


# dp: top-down apprach : tc = O(n)
def better_fib(n, dp):
    if n <= 1:
        return n;
    if dp[n] != -1:
        return dp[n]
    dp[n] = better_fib(n-1, dp) + better_fib(n-2, dp)

    return dp[n]

n = 6
dp = [-1] * (n+1)
print(better_fib(n, dp))