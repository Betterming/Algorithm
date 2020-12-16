import sys
import math


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    slen = len(line)
    new_line = ""
    for ch in line:
        new_line += str(ord(ch) - ord('A'))
    sp = ["1", "2"]
    dp = [1] * slen
    if slen == 2:
        if new_line[0] == "1":
            dp[1] = 2
            print("1")
        if new_line[0] == "2" and new_line[1] <= "5":
            print("1")
            dp[1] = 2

    for i in range(2, slen):
        if new_line[i-1] == '1':
                if new_line[i-2] not in sp:
                    dp[i] = dp[i-1] * 2

