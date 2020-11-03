import sys
import re

if __name__ == '__main__':
    a = " jjj jk , ajg l aj; a k"
    array = re.split(r'\s*[,;\s]\s*', a.strip())
    print(array)
    print(''.join(array))

    b = '123'
    b = b + '4'
    print(b)

    print(b[::])
    c = [[1, 2, 3], [4, 5, 6]]
    print(c[:][1])