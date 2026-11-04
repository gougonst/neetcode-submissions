class Solution {
public:
    // [6, 4, 5, 3, 2, 0, 1, 1]
    // 2:1 + 4 = 5
    // 0:1 + 1 = 2
    // 1:1
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());

        int maxLen = 0;
        for (int num: nums) {
            if (numSet.find(num - 1) != numSet.end()) 
                continue;

            int length = 1;
            while (numSet.find(num + length) != numSet.end()) {
                length++;
            }
            maxLen = max(length, maxLen);
        }
        return maxLen;
    }
};
