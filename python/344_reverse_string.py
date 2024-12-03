class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        for i in range(len(s)//2):
            first = s[i]
            last = s[len(s)-1-i]
            s[i] = last
            s[len(s)-1-i] = first
        
        print(s)

test = Solution()
test.reverseString(["H","a","n","n","a","h"])