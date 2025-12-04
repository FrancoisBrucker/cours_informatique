MA_CONSTANTE = 42
va_variable = None

d = vars()
print("Espace de nommage courant :", d["__name__"], "MA_CONSTANTE" in d)