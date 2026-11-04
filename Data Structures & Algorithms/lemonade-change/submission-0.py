class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coinNumber = { 20: 0, 10: 0, 5: 0 }
        coins = [20, 10, 5]

        for bill in bills:
            exchange = bill - 5
            coinNumber[bill] += 1
            for coin in coins:
                if exchange >= coin:
                    required = exchange // coin
                    give = coinNumber[coin] if required > coinNumber[coin] else required
                    exchange -= give * coin
                    coinNumber[coin] -= give
            if exchange != 0:
                return False
        return True