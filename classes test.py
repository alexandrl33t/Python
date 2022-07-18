from sys import prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minSize = len(min(strs, key=len))
        common_prefix = ''    
        for i in range(0, minSize+1):
            for j in range(1,len(strs)):
                if strs[j][:i] != strs[j-1][:i]:
                    return common_prefix
            common_prefix = strs[0][:i]  
        return common_prefix   

                


a = Solution()
print(a.longestCommonPrefix(["flog","flight","flowers"]))       

