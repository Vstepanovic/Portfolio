# %%
import math
from scipy.stats import norm

# %%
#Prix d'un call

def black_scholes_calls(S, K, T, r, sigma):
    d1 = (math.log(S/ K) + (r + x + sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price

# %%
#Prix d'un put

def black_scholes_puts(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + x + sigma**2) *T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# %%
#Paramètres
x = 0.05
S = int(input("entrez le prix actuel de l'action"))
K = int(input("entrez le prix strike"))
T = float(input("entrez le temps jusqu'à expiration"))
r = float(input("entrez le taux d'intérêt sans risque"))
sigma = float(input("entrez la volatilité de l'action"))

print("Le prix actuel de l'action est", S, "€ avec un prix d'exercice de", K, "€ , il reste", T, 
"année avant expiration et on a un taux d'intérêt sans risque de", r*100, "%, avec une volatilité de", sigma, ".")

#calcul des prix des options
call_price = black_scholes_calls(S, K, T, r, sigma)
put_price = black_scholes_puts(S, K, T, r, sigma)

print("Prix de l'option call européenne (Black-Schles):", call_price,"€.")
print("Prix de l'option put européenne (Black-Scholes):", put_price,"€.")




# %%
