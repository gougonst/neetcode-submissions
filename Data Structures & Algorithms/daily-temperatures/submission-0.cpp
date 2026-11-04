class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> futureWarmers(n, 0);

        for (int i = n - 2; i >= 0; i--) {
            int curTemp = temperatures[i];
            int warmerIndex = i + 1;
            while (curTemp >= temperatures[warmerIndex] && 
                   futureWarmers[warmerIndex] != 0) {
                warmerIndex += futureWarmers[warmerIndex];
            }
            futureWarmers[i] = (curTemp < temperatures[warmerIndex]) ? warmerIndex - i : 0;
        }

        return futureWarmers;
    }
};
