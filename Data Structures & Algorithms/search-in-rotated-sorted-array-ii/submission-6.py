class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binarySearch(l: int, r: int) -> bool:
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return True
                elif nums[m] > nums[l]:
                    if target < nums[m] and target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < nums[l]:
                    if target > nums[m] and target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    l += 1
            return False

        return binarySearch(0, len(nums) - 1)

"""
3, 4, 5, 6, 1, 2
Find 1
3 is pivot

If target == pivot: True

If target < pivot, there are three possibilities after we divided from middle
1. middle > pivot: Find right side
2. middle < pivot: 
    1) middle < target: Find right side
    2) middle > target: Find left side
3. middle == pivot: Binary Search for left and right

If target > pivot, there are three possibilities after we divided from middle
1. middle > pivot: 
    1) middle < target: Find right side
    2) middle > target: Find left side
2. middle < pivot: Find left side
3. middle == pivot: Binary Search for left and right
"""