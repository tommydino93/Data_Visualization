import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate random data
np.random.seed(0)
age = np.random.randint(20, 80, 1000)
cognitive_score = np.random.normal(100 - age / 2, 10)

# Plot histogram
plt.hist(cognitive_score, bins=30, color='red', alpha=0.5, density=False)

# Fit curve to histogram
mu, std = norm.fit(cognitive_score)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p * len(cognitive_score), 'k', linewidth=2)

# Set plot parameters
plt.title("Invented Cognitive Score", fontsize=16, fontweight='bold')
plt.xlabel("Score")
plt.ylabel("Count")

# Show plot
plt.show()
