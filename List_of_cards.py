import random
random.seed(1)   #een vaste seed voor makkelijker debuggen Deze later verwijderen!!!!!
alle_kaarten=[]   #wordt de lijst met alle 81 kaarten 
kleur=['green', 'purple', 'red']
vorm=['diamond','oval', 'squigle']
inhoud=['empty', 'shaded','filled']
hoeveelheid=[1,2,3]
kaart=[]   #wordt een lijst met telkens 1 kaart erin 
for i in kleur:
    for j in vorm:
        for k in inhoud:
            for l in hoeveelheid:
                kaart=[i,j,k,l]
                alle_kaarten.append(kaart)
random.shuffle(alle_kaarten)   #zet de kaarten in een random volgorde in de lijst, is vergelijkbaar met schudden van een stapel kaarten   
