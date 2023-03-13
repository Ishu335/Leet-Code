
class Solution(object):
    def romanToInt(self, s):
        sum=0
        s=s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in str(list(s)):
            if i == "I":
                 sum= sum+1
            elif i == "V":
                 sum= sum+5
            elif i == "X":
                 sum= sum+10
            elif i == "L":
                 sum= sum+50
            elif i == "C":
                 sum= sum+100
            elif i == "D":
                 sum= sum+500
            elif i == "M":
                 sum= sum+1000
        print(sum)                                                                  

obj= Solution()
obj.romanToInt("M")

