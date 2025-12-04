import mon_module

print(mon_module.MA_CONSTANTE)

d = vars()
print("Espace de nommage courant :", d["__name__"], "MA_CONSTANTE" in d)
