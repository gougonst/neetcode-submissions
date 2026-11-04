bool compareFreq(pair<int, int> lhs, pair<int, int> rhs) {
    return lhs.second > rhs.second;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for (auto& num: nums) {
            freqs[num]++;
        }

        vector<pair<int, int>> sortFreqs;
        for (auto& freq: freqs) {
            sortFreqs.push_back({freq.first, freq.second});
        }
        sort(sortFreqs.begin(), sortFreqs.end(), compareFreq);

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(sortFreqs[i].first);
        }
        return ans;
    }
};
