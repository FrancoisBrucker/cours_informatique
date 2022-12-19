def augmente(a):
    nouvel_élément = set()

    i = len(a) - 1
    j = k = i
    while j >= 0:
        if a[k] + a[j] > a[-1]:
            nouvel_élément.add(a[k] + a[j])

        if k > 0:
            k = k - 1
        else:
            j = j - 1
            k = j

    nouvel_élément = list(nouvel_élément)
    nouvel_élément.sort()
    return [a + [x] for x in nouvel_élément]

def augmente_tous(la):
    l = []
    for a in la:
        l.extend(augmente(a))
    return l

# print(augmente([1, 2, 3, 4]))
print(augmente([1]))

# print(augmente_tous([[1, 2]]))
# print(augmente_tous(augmente_tous(augmente_tous(augmente_tous([[1, 2]])))))


def l(n):
    l = [0] * (n+1)
    nb_vues = 0

    a = [[1]]

    while nb_vues < n - 1:
        a = augmente_tous(a)
        for x in a:
            if x[-1] <= n and l[x[-1]] == 0:
                l[x[-1]] = len(x) - 1
                nb_vues += 1
    
    return l

print(l(100))

from multiplicatif_vers_additif import indienne

def l_expo(n):
    l = [0] * (n+1)
    for i in range(2, n+1):
        l[i] = len(indienne(i)) - 1
    return l

N = 100
l_opt = l(N)
l_exp = l_expo(N)

for i in range(2, N + 1):
    print(i, l_opt[i], l_exp[i])