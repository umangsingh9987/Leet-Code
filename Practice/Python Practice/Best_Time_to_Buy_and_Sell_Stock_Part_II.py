class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = []

        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            if current_profit > 0:
                max_profit.append(current_profit)
                min_price = price

        return max_profit


obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([1,2,3,4,5]))