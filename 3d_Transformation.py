import matplotlib.pyplot as plt
import numpy as np

def transformation(cube, matrix):
    transformed = np.dot(matrix, cube)
    return transformed

# Define the cube vertices and projection matrices
cube = np.array([[0, 1, 1, 0, 0, 1, 1, 0],  # x-coordinates
                 [0, 0, 1, 1, 0, 0, 1, 1],  # y-coordinates
                 [0, 0, 0, 0, 1, 1, 1, 1],  # z-coordinates
                 [1, 1, 1, 1, 1, 1, 1, 1]]) # homogeneous coordinates

#================================================================================================================================================
#Rotation matrix x,y,z axis

#Rotation by x-axis, Theta=45
rotation_x= np.array([[1, 0, 0, 0],
                      [0, 0.707, -0.707, 0],
                      [0, 0.707, 0.707, 0],
                      [0, 0, 0, 1]])
#Rotation by y-axis, Theta=45
rotation_y = np.array([[0.707, 0, 0.707, 0],
                      [0, 1, 0, 0],
                      [-0.707, 0, 0.707, 0],
                      [0, 0, 0, 1]])

#Rotation by z-axis, Theta=45
rotation_y = np.array([[0.707, -0.707, 0, 0],
                      [0.707, 0.707, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])



#================================================================================================================================================
#Cube structure
#2D

rotation1 = np.array([[0.707, 0, 0.707, 0],
                      [0, 1, 0, 0],
                      [-0.707, 0, 0.707, 0],
                      [0, 0, 0, 1]])

rotation2 = np.array([[1, 0, 0, 0],
                      [0, 0.829, -0.559, 0],
                      [0, 0.559, 0.829, 0],
                      [0, 0, 0, 1]])





# Scaling matrix
scaling = np.array([[0.5, 0, 0, 0],
                    [0, 0.5, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

# Translation matrix
translation = np.array([[1, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

# Prompt user for sequence of transformations
sequence = input("Enter the sequence of transformations (e.g., 'scaling rotation translation'): ").split()

# Apply composite transformation based on user input sequence
composite_matrix = np.eye(4)
for transform in sequence:
    if transform == 'scaling':
        composite_matrix = np.dot(scaling, composite_matrix)
    elif transform == 'rotation':
        #Choose b/w rotation on x,y,z axis
        composite_matrix = np.dot(rotation_x, composite_matrix)
    elif transform == 'translation':
        composite_matrix = np.dot(translation, composite_matrix)
    else:
        print("Invalid transformation:", transform)

# Get the projections
new_view = transformation(cube, rotation1)
new_view2 = transformation(new_view, rotation2)
new_view3 = transformation(new_view2, composite_matrix)

# Edges of the cube
edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
         (4, 5), (5, 6), (6, 7), (7, 4),  # top face
         (0, 4), (1, 5), (2, 6), (3, 7)]  # vertical lines

#Plot
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
for edge in edges:
    plt.plot([new_view2[0, edge[0]], new_view2[0, edge[1]]],
             [new_view2[1, edge[0]], new_view2[1, edge[1]]], 'b')
plt.title("Cube")
plt.xlabel('X')
plt.ylabel('Y')

# Plot after composite transformation
plt.subplot(1, 2, 2)
for edge in edges:
    plt.plot([new_view3[0, edge[0]], new_view3[0, edge[1]]],
             [new_view3[1, edge[0]], new_view3[1, edge[1]]], 'c')
plt.title("After Composite Transformation")
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()
