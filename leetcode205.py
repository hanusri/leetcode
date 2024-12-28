class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()
        
        for c1, c2 in zip(s, t):
            if c1 not in mapping:
                if c2 in mapped:
                    return False
                mapping[c1] = c2
                mapped.add(c2)
            elif mapping[c1] != c2:
                return False
        return True