class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        s.push(val);

        if (mins.size() == 0 || val < mins.top().first) {
            mins.push({val, 1});
        } else if (val == mins.top().first) {
            mins.top().second++;
        }
    }
    
    void pop() {
        int popVal = s.top();
        s.pop();

        if (popVal != mins.top().first) {
            return;
        }
        if (mins.top().second == 1) {
            mins.pop();
        } else {
            mins.top().second--;
        }
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return mins.top().first;
    }
private:
    stack<int> s;
    stack<pair<int, int>> mins;
};
