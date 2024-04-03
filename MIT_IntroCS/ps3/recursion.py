
VOWELS = {"a", "e", "i", "o", "u"}
list = ["h*llo"] #, "h*ll*", "p*c*fic", "*br*"]


permutations = []

def permuter (word_list):

    for i in range(len(word_list)):
        for j in VOWELS:
            permutations.append(word_list[i].replace('*', j, 1))
    return permuter(permutations)


permuter(list)
print(list)