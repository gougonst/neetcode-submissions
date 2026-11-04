class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // [n1, n2, n3, ...]
        // Current: ni
        // Goal: nj = target = ni
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int cur = nums[i];
            if (indices.find(target - cur) != indices.end() &&
                indices[target - cur] != i) {
                return {i, indices[target - cur]};
            }
        }
        return {};
    }
};
