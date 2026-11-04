class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();

        unordered_map<int, int> freqs;
        for (auto& num: nums) {
            freqs[num]++;
        }

        vector<vector<int>> freqBuckets(n + 1);
        for (auto& freq: freqs) {
            freqBuckets[freq.second].push_back(freq.first);
        }

        vector<int> ans;
        int count = 0;
        for (int i = n; i >= 0; i--) {
            if (freqBuckets[i].size() == 0) {
                continue;
            }
            for (auto& topi: freqBuckets[i]) {
                ans.push_back(topi);
                count++;
            }
            if (count >= k) {
                break;
            }
        }
        return ans;
    }
};
