def trouve(T):
    if T[0] <= T[1]:
        return 0
    
    if T[-1] <= T[-2]:
        return len(T) - 1
    
    for i in range(1, len(T) - 1):
        if T[i] <= min(T[-1], T[i+1]):
            return i


def test_trouve():
    assert 0 == trouve([1, 3])
    assert 1 == trouve([3, 1])
    assert 2 == trouve([3, 2, 1, 2])


def trouve_vite(T):
    if T[0] <= T[1]:
        return 0
    
    if T[-1] <= T[-2]:
        return len(T) - 1

    début = 0
    fin = len(T) - 1

    while True:
        milieu = (fin + début) // 2
        if T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            return milieu
        
        if T[milieu] > T[milieu - 1]:
            fin = milieu
        else:
            début = milieu
    

def test_trouve_vite():
    assert 0 == trouve([1, 3])
    assert 1 == trouve([3, 1])
    assert 2 == trouve([3, 2, 1, 2])
    