class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        for (int r = 0; r < rows; r++) {
            vector<int> row = matrix[r];
            if (target <= row[cols - 1]) {
                return binarySearch(row, target);
            }
        }
        return false;
    }
private:
    bool binarySearch(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            
            if (nums[mid] < target) {
                l = mid + 1;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
