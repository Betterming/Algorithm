import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    wts = list(map(int, sys.stdin.readline().strip().split()))
    vals = list(map(int, sys.stdin.readline().strip().split()))

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if j < wts[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wts[i - 1]] + vals[i - 1])
    print(dp[N][K])