import numpy as np

# Wydatki na reklamę w mld $ (Zadanie 5)
ads = np.array([5.00, 3.08, 2.91, 2.56, 2.44, 2.34, 2.19, 2.15, 2.09, 1.97, 1.96, 1.88])

# a. Średnia
mean_val = np.mean(ads)

# b. Mediana
median_val = np.median(ads)

# c. Kwartyle Q1 i Q3
q1 = np.percentile(ads, 25)
q3 = np.percentile(ads, 75)

print("--- Zadanie 5: Statystyki wydatków na reklamę ---")
print(f"a. Średnia kwota: {mean_val:.2f} mld $")
print(f"b. Mediana: {median_val:.2f} mld $")
print(f"c. Pierwszy kwartyl (Q1): {q1:.2f} mld $")
print(f"c. Trzeci kwartyl (Q3): {q3:.2f} mld $")