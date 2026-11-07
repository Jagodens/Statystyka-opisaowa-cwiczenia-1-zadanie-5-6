import numpy as np

# Środki klas wiekowych
x_mids = np.array([19.5, 29.5, 39.5, 49.5, 59.5])

# Liczba bezrobotnych w tys.
kobiety = np.array([524.3, 455.1, 382.8, 132.0, 13.1])
mezczyzni = np.array([471.7, 369.6, 346.3, 152.2, 43.5])

# a) Średni wiek kobiet i mężczyzn
mean_k = np.sum(x_mids * kobiety) / np.sum(kobiety)
mean_m = np.sum(x_mids * mezczyzni) / np.sum(mezczyzni)

# b) Średni wiek ogółem
total_pop = kobiety + mezczyzni
mean_total = np.sum(x_mids * total_pop) / np.sum(total_pop)

print("--- Zadanie 6: Struktura bezrobotnych ---")
print(f"a. Średni wiek kobiet: {mean_k:.2f} lat")
print(f"a. Średni wiek mężczyzn: {mean_m:.2f} lat")
print(f"b. Średni wiek ogółem: {mean_total:.2f} lat")