class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        if (nums[0] < nums[nums.size() - 1]) {
            return nums[0];
        }

        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid + 1] < nums[mid]) {
                return nums[mid + 1];
            }
            
            if (nums[mid - 1] > nums[mid]) {
                return nums[mid];
            }

            if (nums[mid] < nums[l]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }
};
