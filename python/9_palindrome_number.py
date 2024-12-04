class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_pal = True
        x_string = str(x)
        for i in range(len(x_string)//2):
            if x_string[i] != x_string[len(x_string) -1 -i]:
                is_pal = False

        return is_pal
    

test = Solution()
print(test.isPalindrome(1001))
print(test.isPalindrome(121))
print(test.isPalindrome(-121))