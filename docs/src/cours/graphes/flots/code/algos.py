def chaîne_augmentante(G, c, s, p, f):

    marque = {s: (s, None)}
    examiné = set()
    
    while (p not in marque) and (set(marque.keys()) - examiné):
        x = (set(marque.keys()) - examiné).pop()

        for y in G[x]:
            if y in marque:
                continue

            if c[(x, y)] > f[(x, y)]:
                if (marque[x][1] is None) or (abs(marque[x][1]) > c[(x, y)] > f[(x, y)]):
                    marque[y] = (x, c[(x, y)] > f[(x, y)])
                else:
                    marque[y] = (x, marque[x][1])
        
        for y in G[x]:
            if (y in marque) or (x not in G[y]):
                continue

            
