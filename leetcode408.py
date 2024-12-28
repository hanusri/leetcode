class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                else:
                    num = 0
                    while j < len(abbr) and (abbr[j].isdigit()):
                        num = num*10 + int(abbr[j])
                        j += 1
                    i += j
            else:
                if abbr[j] != word[i]:
                    return False
                else:
                    i += 1
                    j += 1
            
        return i == len(word) and j == len(abbr)