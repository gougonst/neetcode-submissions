Span = namedtuple("Span", ["price", "days"])

class StockSpanner:

    def __init__(self):
        self._spans: List[Span] = []

    def next(self, price: int) -> int:
        days = 1
        while self._spans and self._spans[-1].price <= price:
            days += self._spans[-1].days
            self._spans.pop()
        self._spans.append(Span(price=price, days=days))
        return self._spans[-1].days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)