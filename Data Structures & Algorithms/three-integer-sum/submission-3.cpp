class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        vector<vector<int>> ans;
        int i = 0;
        while (i < n - 2) {
            int complement = -nums[i];
            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[l] + nums[r];
                if (sum > complement) {
                    r--;
                } else if (sum < complement) {
                    l++;
                } else {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[++l]) {}
                    while (l < r && nums[r] == nums[--r]) {}
                }
            }

            while (i < n - 2 && nums[i] == nums[++i]) {}
        }
        return ans;
    }
};
