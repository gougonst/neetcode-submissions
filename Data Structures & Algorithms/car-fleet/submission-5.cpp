class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // position: [4, 1, 0, 7, 2]
        // speed: [2, 2, 1, 1, 1.3]
        // remain: [6, 9, 10, 3, 8]
        // round: [3, 5, 10, 3, 5]
        // ans: [1, 2, 3, 1, 2]

        // Sort position and speed
        int n = position.size();
        if (n == 0) {
            return 0;
        }

        vector<pair<int, int>> pairs;
        for (int i = 0; i < n; i++) {
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.rbegin(), pairs.rend());

        int fleetCount = 1;
        float prevTime = float(target - pairs[0].first) / pairs[0].second;
        for (int i = 1; i < n; i++) {
            float curTime = float(target - pairs[i].first) / pairs[i].second;
            if (curTime > prevTime) {
                prevTime = curTime;
                fleetCount++;
            }
        }
        return fleetCount;
    }
};
