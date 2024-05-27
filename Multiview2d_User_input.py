import matplotlib.pyplot as plt
import numpy as np

def multiview_projection(cube, matrix):
    viewed_matrix = np.dot(matrix, cube)
    return viewed_matrix

# Define the cube vertices and projection matrices
cube = np.array([[0, 1, 1, 0, 0, 1, 1, 0],  # x-coordinates
                 [0, 0, 1, 1, 0, 0, 1, 1],  # y-coordinates
                 [0, 0, 0, 0, 1, 1, 1, 1],  # z-coordinates
                 [1, 1, 1, 1, 1, 1, 1, 1]]) # homogeneous coordinates

top = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]])

front = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 1]])

side = np.array([[0, 0, 1, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 1]])

rotation1 = np.array([[0.707, 0, 0.707, 0],
                      [0, 1, 0, 0],
                      [-0.707, 0, 0.707, 0],
                      [0, 0, 0, 1]])

rotation2 = np.array([[1, 0, 0, 0],
                      [0, 0.829, -0.559, 0],
                      [0, 0.559, 0.829, 0],
                      [0, 0, 0, 1]])

# Edges of the cube
edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
         (4, 5), (5, 6), (6, 7), (7, 4),  # top face
         (0, 4), (1, 5), (2, 6), (3, 7)]  # vertical lines

# Get the projections
front_view = multiview_projection(cube, front)
top_view = multiview_projection(cube, top)
side_view = multiview_projection(cube, side)
new_view = multiview_projection(cube, rotation1)
new_view2 = multiview_projection(new_view, rotation2)

# Function to plot a specific view
def plot_view(view_matrix, edges, title, xlabel, ylabel):
    plt.figure()
    for edge in edges:
        plt.plot([view_matrix[0, edge[0]], view_matrix[0, edge[1]]],
                 [view_matrix[1, edge[0]], view_matrix[1, edge[1]]])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis('equal')
    plt.show()

# Continuously ask user for input until they choose to exit
while True:
    print("Which view would you like to see? Options are: 'top', 'front', 'side', 'rotation1', 'rotation2', or 'exit' to quit")
    choice = input("Enter your choice: ").strip().lower()

    if choice == 'top':
        plot_view(top_view, edges, 'Top View', 'X', 'Y')
    elif choice == 'front':
        plot_view(front_view, edges, 'Front View', 'X', 'Z')
    elif choice == 'side':
        plot_view(side_view, edges, 'Side View', 'Z', 'Y')
    elif choice == 'rotation1':
        plot_view(new_view, edges, 'Rotation by y-axis', 'X', 'Y')
    elif choice == 'rotation2':
        plot_view(new_view2, edges, '2D Orthographic View', 'X', 'Y')
    elif choice == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
