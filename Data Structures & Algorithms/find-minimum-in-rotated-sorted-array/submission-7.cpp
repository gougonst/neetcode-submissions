class Solution {
public:
    int findMin(vector<int> &nums) {
        int n = nums.size();

        if (nums.size() == 1) {
            return nums[0];
        }

        if (nums[0] < nums[n - 1]) {
            return nums[0];
        }

        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            
            /* 
            These two conditions cannot switch, because when we calculate mid, 
            we always calculate the lower bound.

            Under the situation l = 0 and r = 1, the mid will be nums[0] rather 
            than nums[1].

            Therefore, we need to compare mid + 1 first. If it doesn't match, it 
            means the mid isn't 0 so that we can compare mid - 1.
            */
            if (nums[mid + 1] < nums[mid]) {
                return nums[mid + 1];
            }
            if (nums[mid - 1] > nums[mid]) {
                return nums[mid];
            }

            if (nums[mid] > nums[0]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return nums[0];
    }
};
