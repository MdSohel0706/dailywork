class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        if(len(s) == 1):
            return 1
        else:
            for i in range(len(s)-1):
                for j in range(i,len(s)):
                    sub = s[i:j+1]
                    sub_set = set(sub)
                    print(sub_set)
                    if(len(sub) == len(sub_set)):
                        if(len(sub) > n):
                            n = len(sub)

        return n

ob = Solution()
print(ob.lengthOfLongestSubstring("abcabcab"))
