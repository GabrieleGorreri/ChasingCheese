import numpy as np

Ricompense = np.zeros((16,16))
Qualità = np.zeros_like(Ricompense)
yota = 1
gamma = 0.8

def Varco(cella1, cella2):
    global Ricompense
    Ricompense[cella1-1, cella2-1] = 1
    Ricompense[cella2-1, cella1-1] = 1

def VarcoSensoUnico(cella1, cella2):
    global Ricompense
    Ricompense[cella1-1, cella2-1] = 1
    
def Bellman(stato, azione):
    global Ricompense, Qualità, yota, gamma
    return yota * Ricompense[stato,azione] + gamma * max(Qualità[azione,:])
    
def Formaggio(cella):
    global Ricompense, Qualità
    Ricompense = np.zeros((16,16))

		VarcoSensoUnico(1,2)
		VarcoSensoUnico(2,3)
		VarcoSensoUnico(3,7)
		VarcoSensoUnico(7,6)
		VarcoSensoUnico(6,5)
		VarcoSensoUnico(5,1)
		VarcoSensoUnico(3,4)
		VarcoSensoUnico(4,8)
		VarcoSensoUnico(8,12)
		VarcoSensoUnico(12,16)
		VarcoSensoUnico(16,15)
		VarcoSensoUnico(15,14)
		VarcoSensoUnico(13,9)
		VarcoSensoUnico(12,11)
		VarcoSensoUnico(11,10)
		VarcoSensoUnico(10,9)
		VarcoSensoUnico(14,13)
		VarcoSensoUnico(9,5)

    Ricompense[cella-1,cella-1] = 100
    Qualità = np.zeros_like(Ricompense)
    for epoca in range(100):
        for stato in range(16):
            for azione in range(16):
                if Ricompense[stato,azione] != 0:
                    Qualità[stato,azione] = Bellman(stato,azione)

Formaggio(2)
          
def StampaPercorso(posizione = 1):
    global Qualità
    stato = posizione - 1
    arrivo = np.max(Qualità)  # l'arrivo coincide con il valore massimo di Qualità, dov'è la miglior qualità
    print('Il formaggio e\' nella posizione' + str(i))
    print(posizione)
    # Ora scorro il vettore Qualità per cercare il valore migliore nello stato in cui sono.
    passaggi = 0
    while Qualità[stato,stato] < arrivo and passaggi < 16:
        stato = list(Qualità[stato,:]).index(max(Qualità[stato,:]))  # trasformo Qualità in una lista, prendo il massimo valore, e mi restituisce l'indice di dov'è.
        passaggi += 1
        print(stato+1)
        
     
def StampaSalti(posformaggio-1, posizione=1):
    global Qualità
    stato = posizione - 1
    arrivo = np.max(Qualità[posformaggio-1, stato, :])
    salti = 0    
    while Qualità[posformaggio-1, stato, stato] < arrivo and salti < 16:
        stato = list(Qualità[posformaggio-1, stato, :]).index(max(Qualità[posformaggio-1, stato, :]))
        salti += 1    
    return salti     
    
for i in ragen(16):
	if StampaSalti(12,i+1) == 3:
		 print(i+1)  
    