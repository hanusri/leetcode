from typing import List
from collections import defaultdict
class Solution:
    def dna_pattern(s: str) -> List[str]:
        sequences = defaultdict(int)
        result = []
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            sequences[seq] = sequences[seq] + 1
            if sequences[seq] == 2:
                result.append(seq)
        return result