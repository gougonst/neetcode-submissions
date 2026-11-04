class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();

        int l = 0;
        int r = n - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (target == nums[m]) {
                return m;
            } 
            
            // target in left side
            if (target >= nums[0]) {
                // cut in right side
                if (nums[m] < nums[0]) {
                    r = m - 1;
                }
                // cut in left side 
                else {
                    if (target > nums[m]) {
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
            }
            // target in right side 
            else {
                // cut in right side
                if (nums[m] < nums[0]) {
                    if (target > nums[m]) {
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
                // cut in left side 
                else {
                    l = m + 1;
                }
            }
        }
        return -1;
    }
};
