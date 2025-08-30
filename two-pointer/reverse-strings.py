
def reverseString(self, s: List[str]) -> None:
  j = len(s) - 1
  for i in range(len(s) // 2):
      s[i], s[j] = s[j], s[i]
      j -= 1


def reverseString(self, s: List[str]) -> None:
    i = 0 
     j = len(s) - 1
    while i <= j :
        s[i], s[j] = s[j] , s[i]
        i += 1
        j-= 1
