class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();

        int l = 0;
        int r = n - 1;

        int smallestIndex = findMinIndex(nums);
        if (smallestIndex != 0) {
            if (target > nums[n - 1]) {
                r = smallestIndex - 1;
            } else {
                l = smallestIndex;
            }
        }
        
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (target == nums[m]) {
                return m;
            } else if (target > nums[m]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }
private:
    int findMinIndex(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) {
            return 0;
        }

        if (nums[0] < nums[n - 1]) {
            return 0;
        }

        int l = 0;
        int r = n - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid + 1] < nums[mid]) {
                return mid + 1;
            }
            if (nums[mid - 1] > nums[mid]) {
                return mid;
            }

            if (nums[mid] > nums[0]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return 0;
    }
};
