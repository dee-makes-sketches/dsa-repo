class Solution:
  def validPalindrome(self, s: str) -> bool:
      def ispalin(l, r):
          while l < r:
              if s[l] != s[r]:
                  return False
              l += 1   l,r=l+1,r-1
              r -= 1
          return True

      i = 0
      j = len(s) - 1
      while i < j :
          if s[i] != s[j]:
              return ispalin(i+1, j) or ispalin(i , j-1)  # breaking it into left and right strings , ie skipping mismatched charc while keeping other pointer fixed and check whether it is palindrome or not
          i += 1
          j -= 1
      return True   
