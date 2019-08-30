class Solution:
    def checkPalindrome(self, s):
        length = len(s)
        aRetornar = True
        for i in range(0,length):
            if(s[i] != s[length-i-1]):
                aRetornar = False
        return aRetornar
    def checkPalindrome2(self, s):
        arr = s[::-1]
        aRetornar = False
        if str(arr) == s:
            aRetornar = True
        return aRetornar



nuevo =  "gbgbgbg"
print(Solution().checkPalindrome2(nuevo))