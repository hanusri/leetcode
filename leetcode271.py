class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = []
        for str in strs:
            result.append(len(str)+"#"+str)
        return ''.join(result)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            
            length = int(str[i:j])
            word = str[j+1: j + 1 + length]
            result.append(word)
            i = j + 1 + length

        return result