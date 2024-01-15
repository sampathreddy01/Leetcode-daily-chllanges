class Solution(object):
    def binary_search(self, jobs, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if jobs[mid][1] <= target:
                if mid + 1 <= end and jobs[mid + 1][1] <= target:
                    start = mid + 1
                else:
                    return mid
            else:
                end = mid - 1
        return -1

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        self.dp = [0] * n
        self.dp[0] = jobs[0][2]

        for i in range(1, n):
            incl_prof = jobs[i][2]
            l = self.binary_search(jobs, 0, i - 1, jobs[i][0])
            if l != -1:
                incl_prof += self.dp[l]

            self.dp[i] = max(incl_prof, self.dp[i - 1])

        return self.dp[-1]
