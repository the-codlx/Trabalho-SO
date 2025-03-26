<<<<<<< Updated upstream
=======
import matplotlib.pyplot as plt

tempo_seq = [21]
tempo_par = [230]

fig, ax = plt.subplots(figsize=(6, 4))

data = [tempo_seq, tempo_par]
bp = ax.boxplot(data, patch_artist=True, labels=["Sequencial", "Paralelo"])

colors = ["lightblue", "lightgreen"]
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title("Comparação de Tempos de Execução (ms)\nMerge Sort Sequencial vs. Paralelo\n(Ordenação de 10000 elementos)")
ax.set_ylabel("Tempo (ms)")

plt.show()
>>>>>>> Stashed changes
