# YusufProMatcher Algorithim
## A String Matching Algorithm (v2 updated with Skip Heuristic)
```
def yusuf_pro_matcher(text: str, pattern: str) -> list:
    matches = []
    n = len(text)
    m = len(pattern)
    
    if m == 0 or n == 0 or m > n:
        return matches

    # Preprocessing: Build last occurrence table for characters in pattern
    last_occurrence = {}
    for i in range(m):
        last_occurrence[pattern[i]] = i

    mid = m >> 1
    first_char = pattern[0]
    mid_char = pattern[mid]
    last_char = pattern[-1]

    i = 0
    while i <= n - m:
        # Pre-check key characters (first, mid, last)
        if (text[i] == first_char and
            text[i + mid] == mid_char and
            text[i + m - 1] == last_char):

            # Full match check
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                matches.append(i)
                i += m  # Skip full pattern length on match
                continue

        # Skip heuristic based on last character in pattern
        next_char = text[i + m - 1]  # Char that caused mismatch
        skip = last_occurrence.get(next_char, -1)
        shift = max(1, m - skip - 1)
        i += shift

    return matches
```
<img width="2378" height="1180" alt="image" src="https://github.com/user-attachments/assets/94c02be7-bf61-4986-9b16-426be245aa37" />

```
# Comparison Table
| Feature / Algorithm         | `yusuf_pro_matcher (v1)`                                          | **Naïve Matching**                                 | **Knuth-Morris-Pratt (KMP)**                 | **Boyer-Moore (BM)**                                  | **Rabin-Karp (RK)**                 |
| --------------------------- | ------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------- | ----------------------------------- |
| **Idea / Approach**         | Optimized Naïve with 3-char fast-check (first, middle, last) | Brute-force comparison of pattern at each position | Prefix table avoids rechecking known matches | Heuristic-based skipping (bad character, good suffix) | Hash-based comparison of substrings |
| **Time Complexity (Worst)** | O(n·m)                                                       | O(n·m)                                             | O(n + m)                                     | O(n·m) (rare, worst case)                             | O(n·m) (due to hash collisions)     |
| **Time Complexity (Best)**  | O(n) (if checks filter fast)                                 | O(n) (if first match early)                        | O(n + m)                                     | O(n/m) (when heuristics succeed)                      | O(n + m) (ideal case)               |
| **Space Complexity**        | O(1)                                                         | O(1)                                               | O(m) (prefix table)                          | O(m + alphabet size)                                  | O(1) or O(n) (depending on hash)    |
| **Preprocessing Needed**    | None                                                         | None                                               | Yes (build prefix table)                     | Yes (build bad character / suffix tables)             | Yes (compute hash of pattern)       |
| **Heuristics Used**         | First, middle, last char check                               | None                                               | Failure function                             | Bad character, good suffix                            | Hashing                             |
| **Best Use Case**           | Short patterns, large text, few matches expected             | Any case (educational/simple)                      | Frequent pattern matching                    | Large alphabets, long patterns                        | Searching multiple patterns         |
| **Ease of Implementation**  | Very Easy                                                    | Very Easy                                          | Moderate                                     | Complex                                               | Moderate                            |
| **Deterministic?**          | Yes                                                          | Yes                                                | Yes                                          | Yes                                                   | No (hash collisions possible)       |
| **Adaptability**            | Hard-coded heuristic                                         | General-purpose                                    | General-purpose                              | Highly optimized for long patterns                    | Good for many patterns              |
