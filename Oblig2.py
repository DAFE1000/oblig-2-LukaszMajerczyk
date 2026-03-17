import numpy as np
import matplotlib.pyplot as plt


#x = 1.6907

# Definerer et område. 400 punkter mellom 0 og 5
x = np.linspace(0, 5, 400)


# Beregner funksjonen for alle x verdier
# np.arctan = tan^-1
funksjon =  np.exp(-x/4) * np.arctan(x)

#Merkerer toppunktet. med rød farge
x_punkt = 1.6907
y_punkt = np.exp(-x_punkt/4) * np.arctan(x_punkt)

# Plotter funksjonen
plt.plot(x,funksjon, label='Funksjonen')


#Merkerer toppunktet
plt.plot(x_punkt, y_punkt, 'ro', label='Toppunket')


plt.xlabel('x') # Legger til x ved x aksen
plt.ylabel('f(x)') # Legger til f(x) ved y aksen
plt.grid(True) #Legger til rutenett
plt.legend()
plt.show()
