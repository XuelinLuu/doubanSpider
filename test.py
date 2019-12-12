class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s = str(x)
        len_x = len(x_s)
        left, right = 0, 0
        if len_x % 2 == 1:
            left, right = len_x // 2, len_x // 2
        else:
            left, right = len_x // 2 - 1, len_x // 2
        for i in range(right, len_x):
            j = left - i + right
            if x_s[i] != x_s[j]:
                return False
        return True

s = Solution()
print(s.isPalindrome(10))