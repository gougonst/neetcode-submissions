class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        s.push(val);
        mins.push(mins.empty() ? val : min(mins.top(), val));
    }
    
    void pop() {
        s.pop();
        mins.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return mins.top();
    }
private:
    stack<int> s;
    stack<int> mins;
};
