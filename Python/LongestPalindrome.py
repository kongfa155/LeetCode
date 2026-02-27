# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Ý tưởng là sẽ kiểm tra từng phần tử i, nếu i-1 và i +1 giống nhau, ta mở rộng ra tiếp
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # lưu vị trí bắt đầu và kết thúc chuỗi palindrome
        start, end = 0, 0
        # Lấy từng kí tự làm tâm
        for i in range(len(s)):
            # Xét độ dài tâm lẻ
            len1 = self.expand(s,i,i)
            # Xét độ dài tâm chẳn
            len2 = self.expand(s, i, i+1)
            # Độ dài tâm lớn nhất
            max_len = max(len1, len2)
            # Nếu chuỗi này đối xứng dài hơn
            if max_len > end-start:
                # Tính lại vị trí ban đầu, tâm ở i và dời sang 2 bên một khoảng maxlen /2
                start = i - (max_len -1) //2
                end = i + max_len //2
        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        # Phải trừ 1 đi vì khi vòng lặp dừng lại right và left đã đi lố 1 
        return right - left - 1