class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // [n1, n2, n3, ...]
        // Current: ni
        // Goal: nj = target = ni
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            int cur = nums[i];
            int complement = target - cur;
            if (indices.find(complement) != indices.end()) {
                return {indices[complement], i};
            }
            indices[cur] = i;
        }
        return {};
    }
};
