import math
# recursion brute force: O(2^n)
# def cut_rod(n,p):
#     if n == 0:
#         return 0
#     q = float("-INF")
    
#     for i in range(1, n+1):
#         q = max(p[i] + cut_rod(n-i, p), q)
       
#     return q
# n = 2
# p = [0,1,55]
# print(cut_rod(n,p))


# top-down approach (tc = number of subproblem * time per subproblem = n^2)
# def top_down(revenue, n, p):
#     if n == 0:
#         return 0
#     if revenue[n] != -1:
#         return revenue[n]
#     q = float("-inf")
#     for i in range(1, n+1):
#         q = max(q, p[i] + top_down(revenue,n-i, p))
#     revenue[n] = q
#     return q

# n = 2
# p = [0,101,55]
# revenue = [-1] * (n+1)
# print(top_down(revenue, n,p))

# bottom-up approach  == remained to learn

def bottom_up(n, p):
    revenue = [-1] * (n+1)
    revenue[0] = 0
        
    for i in range(1, n+1):
        q = float("-inf")
        for j in range(1, i+1):
            q = max(q,p[j]+revenue[i-j])
        revenue[i] = q

    return revenue[n]

n = 2
p = [0,101,55]

print(bottom_up(n,p))

