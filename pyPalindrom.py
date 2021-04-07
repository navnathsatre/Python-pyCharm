# Write a Python program to check whether a string is a palindrome or not
# Madam
# Malayalam

# M a l a y a l a m
# 0 1 2 3 4 5 6 7 8

# def isPalindrome(s):
#     s = s.lower()
#     for item in range(len(s)//2):
#         if s[item] != s[len(s) - item - 1]:
#             return False
#     return True

def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]

s = "Malayalam"
print(isPalindrome(s))