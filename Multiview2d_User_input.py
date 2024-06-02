import matplotlib.pyplot as plt
import numpy as np

def multiview_projection(vertices, matrix):
    viewed_matrix = np.dot(matrix, vertices)
    return viewed_matrix

def define_vertices(shape):
    if shape == 'cube':
        vertices = np.array([[0, 1, 1, 0, 0, 1, 1, 0],  # x-coordinates
                             [0, 0, 1, 1, 0, 0, 1, 1],  # y-coordinates
                             [0, 0, 0, 0, 1, 1, 1, 1],  # z-coordinates
                             [1, 1, 1, 1, 1, 1, 1, 1]]) # homogeneous coordinates
        edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
                 (4, 5), (5, 6), (6, 7), (7, 4),  # top face
                 (0, 4), (1, 5), (2, 6), (3, 7)]  # vertical lines
    elif shape == 'wedge':
        vertices = np.array([[0, 2, 0, 2, 0, 2],  # x-coordinates
                             [0, 0, 0, 0, 2, 2],  # y-coordinates
                             [0, 0, 2, 2, 0, 0],  # z-coordinates
                             [1, 1, 1, 1, 1, 1]]) # homogeneous coordinates
        edges = [(0, 1), (0, 2), (1, 3), (2, 3),  # bottom face
                 (0, 4), (2, 4), (1, 5), (3, 5),  # vertical lines
                 (4, 5)]  # top face
    else:
        raise ValueError("Invalid shape")
    return vertices, edges

# Projection matrices
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

#Rotation by y-axis,Theta=45
rotation1 = np.array([[0.707, 0, 0.707, 0],
                      [0, 1, 0, 0],
                      [-0.707, 0, 0.707, 0],
                      [0, 0, 0, 1]])

#Rotation by x-axis,Theta=34
rotation2 = np.array([[1, 0, 0, 0],
                      [0, 0.829, -0.559, 0],
                      [0, 0.559, 0.829, 0],
                      [0, 0, 0, 1]])

# L=1, Theta=45 for cavalier
obl_cavalier = np.array([[1, 0, 0.707, 0],
                         [0, 1, 0.707, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 1]])

# L=1/2, Theta=45 for cabinet
obl_cabinet = np.array([[1, 0, 0.353, 0],
                        [0, 1, 0.353, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 1]])

# Function to plot specific views in subplots
def plot_views(top_view, front_view, side_view, rotation2_view, edges):
    fig, axes = plt.subplots(2, 2, figsize=(20, 5))


    # Rotation2 View
    axes[0,0].set_title('2D Orthographic View')
    axes[0,0].set_xlabel('X')
    axes[0,0].set_ylabel('Y')
    for edge in edges:
        axes[0,0].plot([rotation2_view[0, edge[0]], rotation2_view[0, edge[1]]],
                     [rotation2_view[1, edge[0]], rotation2_view[1, edge[1]]], 'b')
    axes[0,0].axis('equal')
    
    
    # Top View
    axes[0,1].set_title('Top View')
    axes[0,1].set_xlabel('X')
    axes[0,1].set_ylabel('Y')
    for edge in edges:
        axes[0,1].plot([top_view[0, edge[0]], top_view[0, edge[1]]],
                     [top_view[1, edge[0]], top_view[1, edge[1]]], 'b')
    axes[0,1].axis('equal')
    
    # Front View
    axes[1,0].set_title('Front View')
    axes[1,0].set_xlabel('X')
    axes[1,0].set_ylabel('Y')
    for edge in edges:
        axes[1,0].plot([front_view[0, edge[0]], front_view[0, edge[1]]],
                     [front_view[1, edge[0]], front_view[1, edge[1]]], 'b')
    axes[1,0].axis('equal')
    
    # Side View
    axes[1,1].set_title('Side View')
    axes[1,1].set_xlabel('Z')
    axes[1,1].set_ylabel('Y')
    for edge in edges:
        axes[1,1].plot([side_view[0, edge[0]], side_view[0, edge[1]]],
                     [side_view[1, edge[0]], side_view[1, edge[1]]], 'b')
    axes[1,1].axis('equal')
    
    

    plt.tight_layout()
    plt.show()

# Function to plot cavalier and cabinet views in subplots
def plot_oblique_views(cavalier_view, cabinet_view, edges):
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Cavalier View
    axes[0].set_title('Oblique Cavalier View')
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    for edge in edges:
        axes[0].plot([cavalier_view[0, edge[0]], cavalier_view[0, edge[1]]],
                     [cavalier_view[1, edge[0]], cavalier_view[1, edge[1]]], 'b')
    axes[0].axis('equal')
    
    # Cabinet View
    axes[1].set_title('Oblique Cabinet View')
    axes[1].set_xlabel('X')
    axes[1].set_ylabel('Y')
    for edge in edges:
        axes[1].plot([cabinet_view[0, edge[0]], cabinet_view[0, edge[1]]],
                     [cabinet_view[1, edge[0]], cabinet_view[1, edge[1]]], 'b')
    axes[1].axis('equal')

    plt.tight_layout()
    plt.show()

# Function to plot a single view
def plot_view(view_matrix, edges, title, xlabel, ylabel):
    plt.figure()
    for edge in edges:
        plt.plot([view_matrix[0, edge[0]], view_matrix[0, edge[1]]],
                 [view_matrix[1, edge[0]], view_matrix[1, edge[1]]], 'b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis('equal')
    plt.show()

# Ask user for shape
shape = input("Do you want to perform the operation on a 'cube' or a 'wedge'? ").strip().lower()
vertices, edges = define_vertices(shape)

# Get the projections
front_view = multiview_projection(vertices, front)
top_view = multiview_projection(vertices, top)
side_view = multiview_projection(vertices, side)
new_view = multiview_projection(vertices, rotation1)
new_view2 = multiview_projection(new_view, rotation2)
obl_cavalier_view = multiview_projection(vertices, obl_cavalier)
obl_cabinet_view = multiview_projection(vertices, obl_cabinet)

# Continuously ask user for input until they choose to exit
while True:
    print("Which view would you like to see? Options are: 'mulitview', 'oblique' or 'exit' to quit")
    choice = input("Enter your choice: ").strip().lower()
    if choice == 'multiview':
        plot_views(top_view, front_view, side_view, new_view2, edges)
    elif choice == 'oblique':
        plot_oblique_views(obl_cavalier_view, obl_cabinet_view, edges)
    elif choice == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
