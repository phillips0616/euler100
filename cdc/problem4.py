import math

def isPalindrome(num):
    half_num = math.floor(len(str(num)) / 2)
    str_num = str(num)
    rev_str = ''.join(reversed(str_num[half_num: ]))
    if (len(str(num)) % 2 != 0):
        half_num += 1
    if (str_num[0 : half_num] == rev_str):
        return True
    else:
        return False

start = 999
largest_palindrome = 0
for x in range(start,0,-1):
    for y in range(x, 0, -1):
        if (isPalindrome(x*y)):
            if ((x*y) > largest_palindrome):
                largest_palindrome = x*y    
                break
            break


print(largest_palindrome)
