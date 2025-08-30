class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k+1):
            tempPrice = prices[:]
            for source,destination,price in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < tempPrice[destination]:
                    tempPrice[destination] = prices[source] + price
            
            prices = tempPrice

        return -1 if prices[dst] == float("inf") else prices[dst]


        