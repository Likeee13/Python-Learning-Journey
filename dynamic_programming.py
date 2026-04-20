n, m, a, b = map(int, input().split())
horse_location = []

def is_horse_loc(a, b):
    if(0 <= a <= n and 0 <= b <= m):
        horse_location.append((a,b))

horse_location.append((a, b))
is_horse_loc(a - 2, b - 1)
is_horse_loc(a - 2, b + 1)
is_horse_loc(a - 1, b - 2)
is_horse_loc(a - 1, b + 2)
is_horse_loc(a + 2, b - 1)
is_horse_loc(a + 2, b + 1)
is_horse_loc(a + 1, b - 2)
is_horse_loc(a + 1, b + 2)

dp = [[0] * (m + 1) for _ in range(0, n + 1)]

dp[0][0] = 1

for x in range(0, n + 1):
    for y in range(0, m + 1):

        if (x, y) in horse_location:
            continue

        if y > 0:
            dp[x][y] += dp[x][y-1]
        if x > 0:
            dp[x][y] += dp[x-1][y]

print(dp[n][m])