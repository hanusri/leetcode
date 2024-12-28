class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diff = 0

            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False