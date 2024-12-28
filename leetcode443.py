class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars is None or len(chars) == 0:
            return 0
        i = 0
        count = 1
        curr_char = chars[0]

        for cur_index in range(1, len(chars)):
            if str[cur_index] != curr_char:
                str[i] = curr_char
                i += 1
                if count != 1:
                    str[i] = count
                    i += 1
                count = 1
                curr_char = str[cur_index]
            else:
                count += 1
        
        return i
                    
                
