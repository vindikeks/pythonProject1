n = 42
k = 2
ans = 0
while n:
    n, res = divmod(n, k)
    ans += res
print(ans)