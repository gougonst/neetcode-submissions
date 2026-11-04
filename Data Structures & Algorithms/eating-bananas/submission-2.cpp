class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // The minimum value of k is 1, and the maximum value of k is the largest element in piles.
        // Because no matter how fast we eat the piles, we need at least len(piles) units of time.
        // Therefore, max(piles) is the smallest rate to eat all the piles as fast as possible.
        //
        // We can apply binary search in the range [1, max(piles)].
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
