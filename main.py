from matplotlib import pyplot as plt
from matplotlib import patches as patches
import math

from subprocess import Popen, PIPE, STDOUT

# Number of points to generate
n = 1000

ptsIn, ptsTotal = 0, 0
x, y = [], []

# Adjusting figure shape
fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable='box')

# Add square and circle to plot
ax.add_patch(patches.Rectangle((-1, -1), 2, 2, edgecolor='black', facecolor='none'))
ax.add_patch(patches.Circle((0,0), 1, edgecolor='black', facecolor='none'))

# Get random numbers from `./rng`
rng = Popen(['./rng', '-n', f'{n*2}'], stdout=PIPE, stderr=STDOUT)

while True:
    val = rng.stdout.readline()
    if not val: break
    x.append(float(val))
    print(val)
    
    val = rng.stdout.readline()
    if not val: break
    y.append(float(val))

# Plot points, red if in the circle, blue if outside the circle
for j in range(n):
    if (math.sqrt((x[j]**2)+(y[j]**2)) < 1):
        plt.scatter(x[j], y[j], color='red')
        ptsIn = ptsIn + 1
    else:
        plt.scatter(x[j], y[j], color='blue')
    ptsTotal = ptsTotal + 1

# Calculate pi and show scatterplot
pi = 4 * (ptsIn/ptsTotal)
plt.title("Pi = "+str(pi))
plt.show()
