def permut(T, k, P):
    if k == len(T):
        print(T)
        P.add(tuple(T))
    else:
        for i in range(k, len(T)):
            T[k], T[i] = T[i], T[k]
            permut(T, k + 1, P)
            T[k], T[i] = T[i], T[k]


def heap(T, k, P):
    if k == 1:
        print(T)
        P.add(tuple(T))
    else:
        heap(T, k - 1, P)
        for i in range(k-1):
            if k % 2 == 0:
                T[i], T[k - 1] = T[k - 1], T[i]
            else:
                T[0], T[k - 1] = T[k - 1], T[0]
            heap(T, k - 1, P)


N = 5
# L = list(range(N))
# s = set()
# permut(L, 0, s)
# print(len(s))

# print("----------------")
L = list(range(N))
s = set()
heap(L, len(L) - 2, s)
print(len(s))
