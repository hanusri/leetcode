def lps_construction(pattern):
    j = 0
    M = len(pattern)

    lps = [0] * M
    i = 1

    while i < M:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

def kmp_pattern_search(text, pattern):
    result = []
    N = len(text)
    M = len(pattern)

    lps = lps_construction(pattern)
    i = 0
    j = 0
    while i < N:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == M:
            result.append(i-j)
            j = lps[j-1]
        elif i < N and text[i] != pattern[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j -1]
    return result


        