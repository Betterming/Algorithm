import sys
import re


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    array = re.split(r'\s*[^a-zA-Z0-9]\s*', line.strip())
    s = ''
    for item in array:
        if not item:
            continue
        ele = ''
        for i in range(len(item)):
            if item[i].isalnum():
                ele += item[i]

        if not s:
            s += ele.lower()
            continue
        else:
            s += ele[0].upper() + ele[1:].lower()
    print(s)