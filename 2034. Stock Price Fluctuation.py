""" You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock. 

Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

"""

class StockPrice:

    def __init__(self):
        self.mp = collections.defaultdict(int)
        self.mx_t = -math.inf
        self.mxhp = []
        self.mnhp = []

    def update(self, timestamp: int, price: int) -> None:
        
        self.mp[timestamp] = price
        heapq.heappush(self.mxhp, (-price, timestamp))
        heapq.heappush(self.mnhp, (price, timestamp))
        self.mx_t = max(timestamp, self.mx_t)
        return 

    def current(self) -> int:
        return self.mp[self.mx_t]

    def maximum(self) -> int:
        p, t = self.mxhp[0]
        p = -p
        while self.mp[t] != p:
            heapq.heappop(self.mxhp)
            p, t = self.mxhp[0]
            p = -p
        
        return p

    def minimum(self) -> int:
        p, t = self.mnhp[0]
        while self.mp[t] != p:
            heapq.heappop(self.mnhp)
            p, t = self.mnhp[0]

        
        return p


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
