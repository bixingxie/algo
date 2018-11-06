def blend(s1, s2, c):
    #returns true if c is a blend of s1 and s2
    if len(s1) + len(s2) != len(c): return False

    memo = [[0 for i in range (len(s1)+1)] for j in range(len(s2)+1)]

    #initializes the first row (base case)
    for i in range(len(s1)):
        if i == 0:
            if s1[i] == c[i]:
                memo[0][i+1] = 1
        else:
            if s1[i] == c[i] and memo[0][i] == 1:
                memo[0][i+1] = 1

    #initializes the first column (base case)
    for i in range(len(s2)):
        if i == 0:
            if s2[i] == c[i]:
                memo[i+1][0] = 1
        else:
            if s2[i] == c[i] and memo[i][0] == 1:
                memo[i+1][0] = 1

    #recursive formulation
    for i in range(len(s1)):
        for j in range(len(s2)):
            if (c[i+j+1] == s1[i] and memo[j+1][i]):
                memo[j+1][i+1] = 1
            if (c[i+j+1] == s2[j] and memo[j][i+1]):
                memo[j+1][i+1] = 1

    return memo[-1][-1]


def main():
    print(blend("DYNOGRASOAMA", "AMICPRMMINGISZING", "DYNAMICPROGRAMMINGISSOAMAZING"))

main()
