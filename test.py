 def yusuf_pro_matcher(text: str, pattern: str) -> list:
    matches = []
    n = len(text)
    m = len(pattern)
    
    if m == 0 or n == 0 or m > n:
        return matches

    mid = m >> 1  # Faster than m // 2

    first_char = pattern[0]
    mid_char = pattern[mid]
    last_char = pattern[-1]

    for i in range(n - m + 1):
        if (text[i] != first_char or
            text[i + mid] != mid_char or
            text[i + m - 1] != last_char):
            continue

        # Avoid slicing, compare character-by-character
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            matches.append(i)

    return matches

import time
start = time.time()
print(yusuf_pro_matcher(text, pattern))
print("YusufProMatcher Exec time:", time.time() - start)
