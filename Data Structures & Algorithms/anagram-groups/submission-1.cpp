class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> freqMap;

        for (const auto& str: strs) {
            vector<int> counts(26, 0);
            for (auto& c: str) {
                counts[c - 'a']++;
            }
            string key = "";
            for (auto& count: counts) {
                key += to_string(count) + ",";
            }
            freqMap[key].push_back(str);
        }

        for (const auto& pair: freqMap) {
            ans.push_back(pair.second);
        }

        return ans;
    }
};
