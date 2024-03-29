import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        visited = []
        mintimes = dict()
        mintimes[k] = 0
        current_stack = []
        heapq.heappush(current_stack, (0, k))

        while True:
            if len(current_stack) == 0:
                break
            
            curr = heapq.heappop(current_stack)[1]
            visited.append(curr)

            for i in range(len(times)-1, -1, -1):
                t = times[i]
                if t[0] == curr:
                    
                    if t[2] + mintimes[curr] < mintimes.get(t[1], float('inf')):
                        mintimes[t[1]] = t[2] + mintimes[curr]
                    if t[1] not in visited:
                        heapq.heappush(current_stack, (mintimes[t[1]], t[1]))
                    del times[i]


        if len(mintimes) != n:
            return -1
        return max(mintimes.values())


if __name__ == "__main__":
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]] , 4, 2))
  