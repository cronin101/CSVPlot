import matplotlib as mpl
import matplotlib.pyplot as pp
import numpy
import sys

# Load matrix from CSV
csv_filename = sys.argv[1]
matrix = numpy.loadtxt(csv_filename, delimiter=",")

# Choose colours for plotting
cmap = mpl.colors.ListedColormap(['r', '1', '0.5', '0'])

# Draw matrix as 'pcolot' plot
grid = pp.pcolor(matrix, cmap=cmap)

pp.xlim(xmax=matrix.shape[1] - 1)
pp.xlabel('Time')

pp.ylim(ymin=1, ymax=matrix.shape[0])
pp.ylabel('State')

# Add key
pp.colorbar(boundaries=[x + 0.5 for x in range(4)], ticks=range(4))


pp.show()
