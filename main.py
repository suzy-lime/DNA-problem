# Inputs a number of test cases, and in case it takes in a half strand of DNA, a number of possible suspects and for
# each possible suspect it takes in their full strand of DNA and their name. The program converts the half strand into a
# full strand, and then finds which suspect had the highest number of DNA matches. The program will return the name of
# the person with the highest number of matches, or multiple names in alphabetical order if people are tied for the
# highest number of matches.

dic = {"A": "T", "C": "G", "G": "C", "T": "A"}
t = int(input())
for _ in range(t):
    h_dna = input()
    n = int(input())
    k = []
    dna_l = []
    m = []
    for x in range(n):
        staff = input()
        dna_l.append(staff)
        m.append(0)
    f_dna = ""
    for char in h_dna:
        f_dna += char + dic[char]
    for x in range(n):
        s = dna_l[x].split()[0]
        for y in range(len(s)):
            if s[y] == f_dna[y]:
                m[x] += 1
    for x in range(n):
        if m[x] == max(m):
            k.append(dna_l[x].split()[1])
    k.sort()
    for name in k:
        print(name)
