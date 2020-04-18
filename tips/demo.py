import re

a = " jjj jk , ajg l aj; a k"
array = re.split(r'\s*[,;\s]\s*', a.strip())
print(array)
print(''.join(array))
