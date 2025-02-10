import numpy as np

num_stati = 10
num_azioni = num_stati
Ricompense = -np.ones((num_stati,num_azioni)) 
Qualità = np.zeros_like(Ricompense)
yota = 1 #Peso per stare fermo
gamma = 0.8 #Peso per muovermi

# creo funzione varco

def Varco(cella1,cella2):
    global Ricompense
    Ricompense[cella1-1, cella2-1] = 1
    Ricompense[cella2-1, cella1-1] = 1

def SetFormaggio(cella):
    global Ricompense
    Ricompense[cella-1, cella-1] = 100

#Da un certo stato io capisco qual è la miglior azione che posso fare
def Bellman(stato, azione):
    global Ricompense, Qualità, yota, gamma
    
    #Ritorniamo la ricompensa attuale, di quello stato e azione (cioè stare fermo),
    #più la ricompensa dello stato successivo se percorriamo quell'azione.
    return yota * Ricompense[stato,azione] + gamma * max(Qualità[azione,:])


#Ora descrivo tutti i passaggi che si possono fare
Varco(1,2)
Varco(2,3)
Varco(3,8)
Varco(3,4)
Varco(4,5)
Varco(5,6)
Varco(6,7)
Varco(7,8)
Varco(8,9)
Varco(9,10)
#Ora dico dove sta la ricompensa
SetFormaggio(10)


# Aggiungiamo un ciclo per le epoche
for epoca in range(100):  # Eseguiamo 100 epoche di training
    for stato in range(num_stati):
        for azione in range(num_azioni):
            if Ricompense[stato, azione] != -1:
                Qualità[stato, azione] = Bellman(stato, azione)

print(Qualità)  # Stampiamo la matrice Qualità finale