from fonctions import parenthèses, suite, bon_parenthésage

s = input("Entrez une chaîne de caractères : ")
s_restriction = parenthèses(s)
print("La chaîne contient la suite de parenthèses :", s_restriction)

suite_1 = suite(s_restriction)
print("La suite associée est : , ", suite_1)

if bon_parenthésage(suite_1):
    print("La suite correspond à un bon parenthésage")
else:
    print("La suite ne correspond pas à un bon parenthésage")