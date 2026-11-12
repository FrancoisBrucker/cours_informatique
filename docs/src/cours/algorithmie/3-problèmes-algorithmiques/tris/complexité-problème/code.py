def permutation_rec(T, i):
    if i >= len(T) - 1:
        print(T)
        return
    for j in range(i, len(T)):
        T[i], T[j] = T[j], T[i]
        permutation_rec(T, i + 1)
        T[i], T[j] = T[j], T[i]


def permutations(T):
    permutation_rec(T, 0)


def est_trie(T):
    for i in range(1, len(T)):
        if T[i] < T[i-1]:
            return False
    return True

def tri_rec(T, i):
    if est_trie(T):
        return True
    if i >= len(T) - 1:
        return False
    for j in range(i, len(T)):
        T[i], T[j] = T[j], T[i]
        if tri_rec(T, i + 1):
            return True
        T[i], T[j] = T[j], T[i]


def tri(T):
    tri_rec(T, 0)

permutations(list(range(4)))

print("-" * 20)
T = list(reversed(range(4)))
print("Tableau initial :", T)
tri(T)
print("Tableau trié :", T)

