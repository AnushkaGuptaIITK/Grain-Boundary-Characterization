import matplotlib.pyplot as plt
import numpy as np

# Read data
data = np.genfromtxt("output.csv", delimiter=",", dtype=float)
voronoi_volumes = data[1:, -1]

mean = np.mean(voronoi_volumes)
sd = np.std(voronoi_volumes)

# Create a histogram of Voronoi volumes
plt.figure(figsize=(6, 6))
plt.hist(voronoi_volumes, bins=100, alpha=0.75, edgecolor='black')
plt.axvline(x=mean, linewidth=2, color='black', label='Mean')


# Add labels and title
plt.xlabel("Voronoi Volume ($\AA^3$)", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.figtext(
    0.15, 0.75, f"Mean = {mean:0.2f} $\AA^3$\n$\sigma$ = {sd:0.2f} $\AA^3$", fontsize=14)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim([30, 50])
plt.ylim([0, 500])

# Save the plot as an image
plt.savefig("voronoi_volumes_distribution.png")