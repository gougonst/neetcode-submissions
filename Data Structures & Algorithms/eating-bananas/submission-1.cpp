class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Actual hour cost: 1 ~ h hours
        // Use k as target to do binary search from 1 ~ max(k)
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());

        int k = -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            int hours = consumePiles(piles, mid);
            if (hours > h) {
                l = mid + 1;
            } else {
                k = mid;
                r = mid - 1;
            }
        }
        return k;
    }
private:
    int consumePiles(vector<int>& piles, int rate) {
        int hours = 0;
        for (int i = 0; i < piles.size(); i++) {
            hours += ceil(piles[i] / double(rate));
        }
        return hours;
    }
};
