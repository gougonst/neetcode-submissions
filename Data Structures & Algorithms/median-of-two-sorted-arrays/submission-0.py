class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a_list = nums1
        b_list = nums2
        if len(a_list) > len(b_list):
            a_list, b_list = b_list, a_list

        total = len(a_list) + len(b_list)
        half = total // 2
        l, r = 0, len(a_list) - 1
        while True:
            a_m = l + (r - l) // 2
            # half = 6, a_m = 1, b needs 4 element, index is 3
            b_m = half - a_m - 2

            a_left = a_list[a_m] if a_m >= 0 else -math.inf
            a_right = a_list[a_m + 1] if (a_m + 1) < len(a_list) else math.inf
            b_left = b_list[b_m] if b_m >= 0 else -math.inf
            b_right = b_list[b_m + 1] if (b_m + 1) < len(b_list) else math.inf

            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = a_m - 1
            else:
                l = a_m + 1