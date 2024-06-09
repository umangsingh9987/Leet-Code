class Solution:
    def maxProfit(self, prices):
        # Initialize maximum variable
        min_price = float('inf')

        max_profit = 0

        # Iterate through each price
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Calculate the current profit
            current_profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, current_profit)

        return max_profit


obj = Solution()
print(obj.maxProfit([2, 4, 1]))
print(obj.maxProfit([1,2]))
print(obj.maxProfit([1,2,4]))
print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([3,2,6,5,0,3]))
print(obj.maxProfit([7,6,4,3,1]))
print(obj.maxProfit([2,1,2,1,0,1,2]))

