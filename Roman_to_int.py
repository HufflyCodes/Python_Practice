class Solution:
    def romanToInt(self, s: str) -> int: #-> is an annotation saying this function should output an integer
        
        strList = [*s] #unpack list to work with individual chars
        print("Original input:", s) #show original input

        RomanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # print(RomanDict)
        intList = [RomanDict[x] for x in strList]
        intList.append(0)
        print(intList)
        # print(type(len(intList)))

        sum = 0
        for i in range(len(intList)-1):
            if intList[i+1] > intList[i]:
                sum -= intList[i]
            else:
                sum += intList[i]
        print("Integer Output:", sum)
        return(sum)




sol = Solution()
sol.romanToInt("IV")
