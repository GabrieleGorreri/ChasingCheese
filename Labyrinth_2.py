import numpy as np

Ricompense = np.zeros((16,16))
Qualità = np.zeros_like(Ricompense)
yota=1
gamma=0.8

def Varco(cella1,cella2):
    global Ricompense
    Ricompense[cella1-1,cella2-1]=1
    Ricompense[cella2-1,cella1-1]=1

def VarcoSensoUnico(cella1,cella2):
    global Ricompense
    Ricompense[cella1-1,cella2-1]=1
    
def Formaggio(cella):
		global Ricompense
		Ricompense[cella-1,cella-1]=100

VarcoSensoUnico(1,2)
VarcoSensoUnico(2,3)
VarcoSensoUnico(3,7)
VarcoSensoUnico(7,6)
VarcoSensoUnico(6,5)
VarcoSensoUnico(5,1)
Varco(3,4)
Varco(4,8)
Varco(8,12)
Varco(12,16)
Varco(12,11)
Varco(11,10)
Varco(10,9)
Varco(9,13)
Varco(13,14)
Varco(14,15)
Formaggio(15)

def Bellman(stato,azione):
    global Ricompense, Qualità, yota, gamma
    return yota * Ricompense[stato,azione] + gamma * max(Qualità[azione,:])

for epoca in range(100):
    for stato in range(16):
        for azione in range(16):
            if Ricompense[stato,azione] != 0:
	            Qualità[stato,azione] = Bellman(stato,azione)
	            
def StampaPercorso(posizione = 1):
    global Qualità
    stato = posizione - 1
    arrivo = np.max(Qualità) #l'arrivo coincide con il valore massimo di Qualità, dov'è la miglior qualità
    print(posizione)
    #Ora scorro il vettore Qualità per cercare il valore migliore nello stato in cui sono.
    passaggi= 0
    while Qualità[stato,stato] < arrivo and passaggi < 16:
        stato = list(Qualità[stato,:]).index(max(Qualità[stato,:])) #trasformo Qualità in una lista, prendo il massimo valore, e mi restituisce l'indice di dov'è.
        passaggi += 1
        print(stato+1)