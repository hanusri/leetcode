from collections import defaultdict
import heapq
from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_score_map = defaultdict(list)
        for id, score in items:
            if len(student_score_map[id]) < 5:
                heapq.heappush(student_score_map[id], score)
            else:
                heapq.heappushpop(student_score_map[id], score)
        
        result = []
        for id, scores in student_score_map.items():
            total_sum = sum(scores)
            avg = total_sum // 5
            result.append([id, avg])

        return sorted(result)    
        
