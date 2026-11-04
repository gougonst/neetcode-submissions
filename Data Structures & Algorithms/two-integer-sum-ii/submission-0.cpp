class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        
        while (numbers[l] + numbers[r] != target) {
            int curSum = numbers[l] + numbers[r];
            if (curSum > target) {
                r--;
            }
            else if (curSum < target) {
                l++;
            }
        }
        return {l + 1, r + 1};
    }
};
