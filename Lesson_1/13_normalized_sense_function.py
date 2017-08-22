p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    greenMul = pHit if Z == 'green' else pMiss
    redMul = pHit if Z == 'red' else pMiss

    q = [x * (greenMul if world[idx] == 'green' else redMul)
         for (idx, x) in enumerate(p)]
    return [float(x) / sum(q) for x in q]

print(sense(p,Z))
