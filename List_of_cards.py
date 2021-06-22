alle_sets=[]   #wordt de lijst met alle 81 kaarten 
kleur=['green', 'purple', 'red']
vorm=['diamond','oval', 'squigle']
binnenkant=['empty', 'shaded','filled']
hoeveelheid=[1,2,3]
set_kaarten=[]   #wordt een lijst met telkens 1 kaart erin 
for i in kleur:
    for j in vorm:
        for k in binnenkant:
            for l in hoeveelheid:
                set_kaarten=[i,j,k,l]
                alle_sets.append(set_kaarten)
