import matplotlib.pyplot as plt

# 1) Organize os dados em listas
# --------------------------------------------------
# LISTA PEQUENA
tempo_seq_peq = [0.255, 1, 3, 19, 43]   # Sequencial
tempo_par_peq = [89, 85, 134, 149, 156] # Paralelo

# LISTA GRANDE
tempo_seq_gra = [532, 1188, 1945, 2584, 3306]   # Sequencial
tempo_par_gra = [417, 750, 1185, 1496, 1859]    # Paralelo

# 2) Crie uma figura e um eixo
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

# 3) Gere os boxplots
#    Cada elemento da lista 'data' vira uma "caixa" (box) no gráfico
# --------------------------------------------------
data = [tempo_seq_peq, tempo_par_peq, tempo_seq_gra, tempo_par_gra]

# Cria o boxplot e define os rótulos para cada grupo
bp = ax.boxplot(data, patch_artist=True, labels=[
    "Pequena\nSeq.", "Pequena\nPar.", "Grande\nSeq.", "Grande\nPar."
])

# 4) Personalize as cores (opcional)
# --------------------------------------------------
colors = ["lightblue", "lightgreen", "lightblue", "lightgreen"]
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# 5) Ajuste o layout do gráfico
# --------------------------------------------------
ax.set_title("Comparação de Tempos de Execução (ms)\nMerge Sort Sequencial vs. Paralelo")
ax.set_ylabel("Tempo (ms)")

# 6) Exiba o gráfico
# --------------------------------------------------
plt.tight_layout()
plt.show()