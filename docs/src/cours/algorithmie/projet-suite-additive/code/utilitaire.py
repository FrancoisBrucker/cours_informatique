def est_une_suite_additive(u):

    if u[0] != 1:
        return False
    for i in range(1, len(u)):
        ok = False
        for k in range(i):
            for l in range(k, i):
                if u[i] == u[k] + u[l]:
                    ok = True

        if not ok:
            return False

    return True


def test_début():
    assert not est_une_suite_additive([2, 4])


def test_oui():
    assert est_une_suite_additive([1, 2, 3, 4])


def test_non():
    assert not est_une_suite_additive([1, 2, 4, 7])


def trie_et_sans_doublons(a):
    b = []

    for x in sorted(a):
        if len(b) == 0 or b[-1] != x:
            b.append(x)

    return b


def test_triée():
    a = [1, 2, 4, 8, 3, 2, 11]
    b = trie_et_sans_doublons(a)

    assert a == [1, 2, 4, 8, 3, 2, 11]
    assert b == [1, 2, 3, 4, 8, 11]


def coefficient_additif(a):

    b = [None]

    for i in range(1, len(a)):
        j = k = i
        while j >= 0:
            if a[i] == a[k] + a[j]:
                b.append((k, j))
                break

            if k > 0:
                k = k - 1
            else:
                j = j - 1
                k = j

    return b


def test_coefficient_additif():
    assert coefficient_additif([1, 2, 3, 4]) == [None, (0, 0), (0, 1), (0, 2)]
    assert coefficient_additif([1, 2, 4, 8, 2, 10]) == [
        None,
        (0, 0),
        (1, 1),
        (2, 2),
        (0, 0),
        (3, 4),
    ]
