# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).



#Y tuong ban dau, gop 2 mang, tim phan tu trung vi va tinh trung vi
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         arr = []
#         i = j = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 arr.append(nums1[i])
#                 i+=1
#             else:
#                 arr.append(nums2[j])
#                 j+=1
#         while i < len(nums1):
#             arr.append(nums1[i])
#             i+=1
#         while j < len(nums2):
#             arr.append(nums2[j])
#             j+=1
#         l = len(arr)
#         if l % 2 ==0:
#             return (arr[l//2] + arr[l//2 -1]) / 2.0
#         else: 
#             return arr[l//2]


# Chia 2 mảng thành 2 nửa sao cho:

# Tổng số phần tử bên trái = bên phải (hoặc lệch 1 nếu tổng lẻ)

# Mọi phần tử bên trái ≤ mọi phần tử bên phải

# Khi thỏa điều kiện này → ta tìm được median ngay.
# B1: Đảm bảo nums1 là mảng ngắn hơn
# B2: Đặt left = 0, right = len(nums1)
# B3: Tính half = (m + n + 1) // 2

# B4: Lặp khi left <= right:

#     i = (left + right) // 2
#     j = half - i

#     L1 = nums1[i-1] nếu i > 0, ngược lại -∞
#     R1 = nums1[i]   nếu i < m, ngược lại +∞

#     L2 = nums2[j-1] nếu j > 0, ngược lại -∞
#     R2 = nums2[j]   nếu j < n, ngược lại +∞

#     Nếu L1 <= R2 và L2 <= R1:
#         Nếu tổng số phần tử là chẵn:
#             median = (max(L1,L2) + min(R1,R2)) / 2
#         Nếu lẻ:
#             median = max(L1, L2)
#         Trả về median

#     Nếu L1 > R2:
#         Dịch sang trái → right = i - 1
#     Ngược lại:
#         Dịch sang phải → left = i + 1
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1)// 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i
            L1 = nums1[i-1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')
            L2 = nums2[j-1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:
                if(m + n) % 2 ==0:
                    return ((max(L1, L2) + min (R1,R2) )/ 2.0)
                else:
                    return max(L1,L2)
            elif L1 > R2:
                right =i - 1
            else:
                left = i + 1
        


        