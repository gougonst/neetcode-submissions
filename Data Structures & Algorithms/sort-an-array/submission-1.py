class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums

    def heapSort(self, nums: List[int]) -> None:
        def buildMaxHeap(nums: List[int]) -> None:
            for i in range(len(nums) // 2 - 1, -1, -1):
                maxHeapify(nums, len(nums), i)

        def maxHeapify(nums: List[int], boundary: int, root: int) -> None:
            left = 2 * root + 1
            right = 2 * root + 2
            maxNode = root

            if left < boundary and nums[left] > nums[maxNode]:
                maxNode = left
            if right < boundary and nums[right] > nums[maxNode]:
                maxNode = right
            
            if maxNode != root:
                nums[maxNode], nums[root] = nums[root], nums[maxNode]
                maxHeapify(nums, boundary, maxNode)

        buildMaxHeap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            maxHeapify(nums, i, 0)