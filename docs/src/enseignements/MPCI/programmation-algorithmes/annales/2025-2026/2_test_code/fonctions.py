def parenthèses(chaîne):
    parenthèses = ""

    for c in chaîne:
        if c in "()":
            parenthèses += c
    return parenthèses


def suite(chaîne_de_parenthèses):
    suite = []

    for c in chaîne_de_parenthèses:
        if c == "(":
            suite.append(1)
        elif c == ")":
            suite.append(-1)
    return suite


def bon_parenthésage(suite_de_0_1):
    somme = 0

    for c in suite_de_0_1:
        somme += c

        if somme < 0:
            return False

    return True
