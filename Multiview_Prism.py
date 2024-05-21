import matplotlib.pyplot as plt
import numpy as np

def multiview_projection(prism, matrix):
    viewed_matrix = np.dot(matrix, prism)
    return viewed_matrix

# Define the triangular prism vertices and projection matrices
prism = np.array([[0, 1, 2, 0, 1, 2],  # x-coordinates
                  [0, 1, 0, 0, 1, 0],  # y-coordinates
                  [0, 0, 0, 1, 1, 1],  # z-coordinates
                  [1, 1, 1, 1, 1, 1]]) # homogeneous coordinates

top = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]])

front = np.array([[1, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

side = np.array([[0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

# Edges of the prism
edges = [(0, 1), (1, 2), (2, 0),    # triangular base
         (3, 4), (4, 5), (5, 3),    # triangular top
         (0, 3), (1, 4), (2, 5)]    # vertical lines

# Get the projections
front_view = multiview_projection(prism, front)
top_view = multiview_projection(prism, top)
side_view = multiview_projection(prism, side)

# Plot the original 3D prism and its projections
fig = plt.figure(figsize=(10, 8))

# Original 3D points with edges
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
for edge in edges:
    ax1.plot([prism[0, edge[0]], prism[0, edge[1]]],
             [prism[1, edge[0]], prism[1, edge[1]]],
             [prism[2, edge[0]], prism[2, edge[1]]], 'b')
ax1.set_title("Original 3D")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Front view with edges
ax2 = fig.add_subplot(2, 2, 2)
for edge in edges:
    ax2.plot([front_view[0, edge[0]], front_view[0, edge[1]]],
             [front_view[2, edge[0]], front_view[2, edge[1]]], 'r')
ax2.set_title("Front View")
ax2.set_xlabel('X')
ax2.set_ylabel('Z')

# Side view with edges
ax3 = fig.add_subplot(2, 2, 3)
for edge in edges:
    ax3.plot([side_view[1, edge[0]], side_view[1, edge[1]]],
             [side_view[2, edge[0]], side_view[2, edge[1]]], 'g')
ax3.set_title("Side View")
ax3.set_xlabel('Y')
ax3.set_ylabel('Z')

# Top view with edges
ax4 = fig.add_subplot(2, 2, 4)
for edge in edges:
    ax4.plot([top_view[0, edge[0]], top_view[0, edge[1]]],
             [top_view[1, edge[0]], top_view[1, edge[1]]], 'b')
ax4.set_title("Top View")
ax4.set_xlabel('X')
ax4.set_ylabel('Y')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
