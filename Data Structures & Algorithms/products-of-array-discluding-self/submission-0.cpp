class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // [-1, 4, 1, 2, 3]
        // [24, -6, -24, -12, -8]
        // from r: [24, 6, 6, 3, 1]
        // from l: [1, -1, -4, -4, -8]
        int n = nums.size();
        vector<int> leftProducts(n, 1);
        vector<int> rightProducts(n, 1);
        for (int i = 1; i < n; i++) {
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1];
        }
        for (int i = n - 2; i >= 0; i--) {
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1];
        }

        vector<int> products(n, 1);
        for (int i = 0; i < n; i++) {
            products[i] = leftProducts[i] * rightProducts[i];
        }
        return products;
    }
};
