# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


# Ý tưởng ban đầu, tạo một mảng 2 chiều, lưu theo chiều dọc và lưu theo chiều ngang, xong đọc từ trái qua từ trên xuống
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        
        matrix = [[] for _ in range(numRows)]
#         matrix = [
        #   [],   # row 0
        #   [],   # row 1
        #   []    # row 2
        #]
        countNumberPassBy, j = 0, 0
        
        while (countNumberPassBy < len(s)):
            # Đi xuống
            for i in range(numRows):
                if countNumberPassBy >= len(s):
                    break
                matrix[i].append(s[countNumberPassBy])
                countNumberPassBy+=1
            # Đi chéo lên
            for i in range(numRows -2, 0, -1):
                if countNumberPassBy >= len(s):
                    break
                matrix[i].append(s[countNumberPassBy])
                countNumberPassBy+=1
        s = ""
        for row in matrix:
            for char in row:
                s+= char
        return s


# Giải thuật tối ưu, xử lý từng ký tự
# Duy trì:
# - current_row
# - direction (1 hoặc -1)

# Mỗi ký tự:
# 1. append vào row hiện tại
# 2. nếu chạm top hoặc bottom → đổi direction
# 3. current_row += direction
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        currentRow, c = 0, 0
        # 1 là đi xuống, -1 là đi chéo
        direction = 1
        matrix = [[] for _ in range(numRows)]
        while c < len(s):
            matrix[currentRow].append(s[c])
            c+=1
            if (currentRow == 0):
                direction = 1
            elif (currentRow == numRows -1):
                direction = -1
            currentRow+= direction
            
        s = ""
        for row in matrix:
            for char in row:
                s+= char
        return s
