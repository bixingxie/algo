## Dynamic Programming
1. Blend

    Suppose that you have two strings, S1, S2, each consisting of characters from some
    small alphabet. The lengths of the strings are k and n respectively. You can assume
    that n ≥ k but not that k is necessarily some small value.
    If we alternate reading characters from one string and then the other, we create a
    “blend” of the two strings. 
    
    For example if S1 = **DYNOGRASOAMA** and S2 = **AMICPRMMINGISZING**
    
    we can create this blend: **DYNAMICPROGRAMMINGISSOAMAZING**
    
    Note that the length of a blend is n+k, and there can be many blends.
    Now for the problem:
    Given three strings S1, S2 and C, determine if C is a blend of S1 and S2. If S1 and S2
    have size k and n respectively, the time complexity should be O(kn).
