from fonctions import parenthèses, suite, bon_parenthésage

def test_parenthèses():
    assert "()" == parenthèses("(1+2)-3")
    assert "" == parenthèses("coucou !")
    assert "())" == parenthèses("coucou (toi) :)")

def test_suite():
    assert [1, -1] == suite("()")
    assert [] == suite("")
    assert [1, -1, -1] == suite("())")    

def test_bon_parenthésage():
    assert bon_parenthésage([1, -1])
    assert bon_parenthésage([])
    assert not bon_parenthésage([1, -1, -1, 1])