alle=[]
kleur=['green', 'purple', 'red']
vorm=['diamond','oval', 'squigle']
binnenkant=['empty', 'shaded','filled']
hoeveelheid=[1,2,3]
set_kaarten=[]
for i in kleur:
    for j in vorm:
        for k in binnenkant:
            for l in hoeveelheid:
                set_kaarten=[i,j,k,l]
                alle.append(set_kaarten)

print(alle)
print(len(alle))
