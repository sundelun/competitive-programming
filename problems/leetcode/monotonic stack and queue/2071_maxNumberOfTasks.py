# https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/
from typing import List
from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # why we cannot just use greedy strategy of match smallest strength workers with easiest work
        # consider the example of tasks = [5, 5, 8] and workers = [4, 6, 6] and pills = 1, strength = 5
        # it is obvious that the answer is 3 since we can use pill to first woker
        # but in this strategy it will not give the right answer
        # solution: use monotonic queue
        # another greedy: use the most powerful k workers to finish k easiest job
        # we need to use a monotonic queue and binary search technique to solve this problem
        # the idea is to first sort both tasks and workers for use the most powerful k workers to finish k easiest job
        # Each phase we will be inserted all tasks that can be completed by each worker w(after eating the pills)
        # if w >= q[0](smallest tasks in the current phase), then the current worker would just complete the easiset work
        # otherwise w < q[0], if we still have enough pill, the current worker would just take the biggest task in queue
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        def check(num: int) -> bool:
            rest = pills
            q = deque([])
            i = 0
            for w in workers[-num:]:
                # insert all tasks that can be accomplished after grow strength
                while i < num and tasks[i] <= w + strength:
                    q.append(tasks[i])
                    i += 1
                # you cannot complete a job after grow strength, return False
                if not q: return False
                # take the easiest job if you can finish it without grow strength
                if w >= q[0]:
                    q.popleft()
                    continue
                # run out of pills
                if rest == 0: return False
                rest -= 1
                # take the hardest work that can be accomplished after take strength
                q.pop()
            return True
        # general binary search to solve it
        left = 1
        right = min(n, m)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1