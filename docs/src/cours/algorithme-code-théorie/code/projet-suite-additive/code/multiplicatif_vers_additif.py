from utilitaire import trie_et_sans_doublons, coefficient_additif

def naif(n):
    a = [1]

    while a[-1] < n:
        a.append(a[-1] + a[0])
    
    return a


def test_naif():
    assert naif(5) == [1, 2, 3, 4, 5]


def indienne(n):
    a = [1]

    c = a[-1] + a[-1]
    while c < n:
        a.append(c)
        c = a[-1] + a[-1]

    c = n-1
    i = 0
    r = a[i]
    while c > 0:
        if c % 2 == 1:
            r = r + a[i]
            a.append(r)
            c = c - 1
        else:
            i = i + 1
            c = c / 2
    return a

print(indienne(15))
def test_indienne():
    assert indienne(15) == [1, 2, 4, 8, 3, 7, 15]

def opti_indienne(n):
    return trie_et_sans_doublons(indienne(n))

def test_opti_indienne():
    assert opti_indienne(15) == [1, 2, 3, 4, 7, 8, 15]


if __name__ == "__main__":
    print(indienne(15), coefficient_additif(indienne(15)))
    print(opti_indienne(15), coefficient_additif(opti_indienne(15)))