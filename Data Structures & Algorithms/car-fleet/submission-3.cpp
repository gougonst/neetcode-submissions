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

        vector<pair<int, int>> posSpeedPairs;
        for (int i = 0; i < n; i++) {
            posSpeedPairs.push_back({position[i], speed[i]});
        }
        sort(posSpeedPairs.begin(), posSpeedPairs.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.first > rhs.first;
        });

        vector<float> rounds;
        for (int i = 0; i < n; i++) {
            rounds.push_back((target - posSpeedPairs[i].first) / float(posSpeedPairs[i].second));
        }

        int fleetCount = 1;
        float curRound = rounds[0];
        for (int i = 0; i < n; i++) {
            int position = posSpeedPairs[i].first;
            int speed = posSpeedPairs[i].second;
            float round = rounds[i];
            cout << "position: " << position << endl;
            cout << "speed: " << speed << endl;
            cout << "round: " << round << endl;
            cout << "curRound: " << curRound << endl;
            if (round > curRound) {
                curRound = round;
                fleetCount++;
            }
        }
        return fleetCount;
    }
};
