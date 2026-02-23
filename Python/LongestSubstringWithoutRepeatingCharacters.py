# Given a string s, find the length of the longest substring without duplicate characters.

#Sai ở chỗ xóa là reset lại toàn bộ mảng, nếu như có chuỗi ở giữa thuộc vào chuỗi dài nhất thì sẽ sai
# Ví dụ: abcbed => chuỗi dài nhất là cbed nhưng nếu chạy code này sẽ ra abc 
# My first solution
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         highest = 0
#         crrLen = 0
#         arr = []
#         for i in s:
#             if i in arr:
#                 highest = crrLen if highest < crrLen else highest
#                 crrLen = 0
#                 del arr[:]
#             arr.append(i)
#             crrLen+=1
#         return highest

#Tối ưu tạo 1 con trỏ trái và phải
#Kiểm tra ký tự đã có trong mảng chưa, có thì xóa đến khi mất phần tử trùng.
#So sánh độ dài nhất và tiếp tục
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            a.add(s[right])

        return max_len
