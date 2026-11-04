class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        vector<unordered_map<char, int>> freqList;

        for (auto& str: strs) {
            unordered_map<char, int> freq = countFreq(str);
            bool isUnique = true;
            for (int j = 0; j < freqList.size(); j++) {
                if (isSameFreq(freqList[j], freq)) {
                    ans[j].push_back(str);
                    isUnique = false;
                }
            }
            if (isUnique) {
                ans.push_back({str});
                freqList.push_back(freq);
            }
        }

        return ans;
    }
private:
    unordered_map<char, int> countFreq(string& str) {
        unordered_map<char, int> freq;
        for (auto& c: str) {
            freq[c]++;
        }
        return freq;
    }

    bool isSameFreq(unordered_map<char, int>& lhs, unordered_map<char, int>& rhs) {
        if (lhs.size() != rhs.size())
            return false;

        for (auto& iter: lhs) {
            char key = iter.first;
            int freq = iter.second;
            if (rhs.find(key) == rhs.end() || rhs[key] != freq) 
                return false;
        }

        return true;
    }
};
