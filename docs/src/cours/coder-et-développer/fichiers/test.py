import os.path

import requests

if not os.path.exists("mon_fichier.py"):
    page = requests.get("https://www.gutenberg.org/ebooks/14155.txt.utf-8")
    f = open("mon_fichier.py", "w", encoding="utf-8")
    f.write(page.text)
    f.close()