def Check_Palindrome(n: int,s:str) -> bool:
   for i in range(n):
      t = s[:i] + s[i+1:]
      if t == t[::-1]:
         return True
   return s == s[::-1]


if __name__ == '__main__':
   n = int(input())
   s = input()
   print(Check_Palindrome(n,s))
