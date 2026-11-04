class Solution {
public:
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
