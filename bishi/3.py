import sys

if __name__ == '__main__':
    line = .strip()
    a = []
    for i in line:
        if i not in a:
            a.append(i)
    print(''.join(a))