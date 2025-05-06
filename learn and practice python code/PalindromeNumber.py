class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    try:
        x_input = int(input("Nhập vào một số nguyên x: "))
        solution = Solution()
        result = solution.isPalindrome(x_input)
        print(f"Input: x = {x_input}, Output: {result}")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")