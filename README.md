# YusufProMatcher Algorithim
## A String Matching Algorithm
```
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
```
## Benchmark Results :-
### Test Case 1 : `text = "a" * 10_000 + "b"` & `pattern = "a" * 10_000 + "b"` 
```
Benchmarking Results (Fastest First):
Naive Matcher             | 0.00000 sec,  Matches: 1
Built-in str.find()       | 0.00000 sec,  Matches: 1
YusufProMatcher           | 0.00105 sec,  Matches: 1
Boyer-Moore Matcher       | 0.00405 sec,  Matches: 1
KMP Matcher               | 0.00774 sec,  Matches: 1
Regex Matcher             | 0.02777 sec,  Matches: 1
```
### Test Case 2 : `text = generate_text(100000, pattern, insert_every=300)` & `pattern = "abcDE"` 
```
Benchmarking Results (Fastest First):
Built-in str.find()       | 0.00000 sec,  Matches: 334
Regex Matcher             | 0.00000 sec,  Matches: 334
YusufProMatcher           | 0.00859 sec,  Matches: 334
Boyer-Moore Matcher       | 0.01622 sec,  Matches: 334
Naive Matcher             | 0.02955 sec,  Matches: 334
KMP Matcher               | 0.04086 sec,  Matches: 334
```
### Test Case 3 : `text = "x" * 5000 + "hello"` & `pattern = "hello"` 
```
Benchmarking Results (Fastest First):
YusufProMatcher           | 0.00000 sec,  Matches: 1
Built-in str.find()       | 0.00000 sec,  Matches: 1
Regex Matcher             | 0.00000 sec,  Matches: 1
Boyer-Moore Matcher       | 0.00000 sec,  Matches: 1
Naive Matcher             | 0.00104 sec,  Matches: 1
KMP Matcher               | 0.00208 sec,  Matches: 1
```
