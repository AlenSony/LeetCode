import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        
        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []

        current_time = 0

        for t, task in enumerate(tasks):



            current_time = max(current_time, t)

            while busy and busy[0][0] <= current_time:
                end, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Assign task and calculate finishing time
            heapq.heappush(
                busy,
                (current_time + task, weight, index)
            )

        return ans


            