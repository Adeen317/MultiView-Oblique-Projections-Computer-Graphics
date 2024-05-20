import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to create the shear matrix for the transformation
def create_shear_matrix(xwmin, xwmax, ywmin, ywmax, znear):
    # Compute the shearing parameters
    shzx = -(xwmin + xwmax) / (2 * znear)
    shzy = -(ywmin + ywmax) / (2 * znear)
    
    # Define the shearing matrix
    shear_matrix = np.array([
        [1, 0, shzx, 0],
        [0, 1, shzy, 0],
        [0, 0,    1, 0],
        [0, 0,    0, 1]
    ])
    
    return shear_matrix

# Function to create the perspective projection matrix
def create_perspective_projection_matrix(znear, zfar):
    # Define the perspective-projection matrix parameters
    sz = zfar / (zfar - znear)
    tz = -znear * sz
    
    # Define the perspective-projection matrix
    perspective_matrix = np.array([
        [-znear,     0,     0,  0],
        [     0, -znear,     0,  0],
        [     0,      0,    sz, tz],
        [     0,      0,    -1,  0]
    ])
    
    return perspective_matrix

# Function to apply the transformation matrix to a point
def apply_transformation(matrix, point):
    # Convert point to homogeneous coordinates by appending 1
    point_homogeneous = np.append(point, 1)
    
    # Apply the transformation matrix
    transformed_point = matrix @ point_homogeneous
    
    # Convert back to Cartesian coordinates by dividing by the last element
    transformed_point_cartesian = transformed_point[:-1] / transformed_point[-1]
    
    return transformed_point_cartesian

# Function to plot a cube given its vertices
def plot_cube(vertices, title='Cube', color='b', alpha=0.1, edge_color='k', view_init=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the faces of the cube using the vertices
    faces = [[vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [7, 6, 2, 3]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]]]
    
    # Create a 3D polygon collection for the faces
    poly3d = [[tuple(face[i]) for i in range(len(face))] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, edgecolors=edge_color, alpha=alpha))
    
    if view_init:
        ax.view_init(elev=view_init[0], azim=view_init[1])
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    
    plt.show()

def main():
    # Define the view volume parameters
    xwmin, xwmax = -1, 1
    ywmin, ywmax = -1, 1
    znear, zfar = 1, 10
    
    # Create the shear and perspective projection matrices
    shear_matrix = create_shear_matrix(xwmin, xwmax, ywmin, ywmax, znear)
    perspective_matrix = create_perspective_projection_matrix(znear, zfar)
    
    # Concatenate the shear and perspective matrices to get the oblique perspective-projection matrix
    oblique_perspective_matrix = perspective_matrix @ shear_matrix
    
    # Define the vertices of a smaller cube centered at the origin
    cube_vertices = np.array([
        [0.25, 0.25, -0.25],  # Vertex 0
        [0.25, -0.25, -0.25],  # Vertex 1
        [-0.25, -0.25, -0.25],  # Vertex 2
        [-0.25, 0.25, -0.25],  # Vertex 3
        [0.25, 0.25, 0.25],  # Vertex 4
        [0.25, -0.25, 0.25],  # Vertex 5
        [-0.25, -0.25, 0.25],  # Vertex 6
        [-0.25, 0.25, 0.25]  # Vertex 7
    ])
    
    # Apply the transformation to each vertex of the cube
    transformed_vertices = np.array([apply_transformation(oblique_perspective_matrix, v) for v in cube_vertices])
    
    # Plot the original cube
    plot_cube(cube_vertices, title='Original Cube', color='b', edge_color='b')
    
    # Plot the transformed cube
    plot_cube(transformed_vertices, title='Oblique Perspective Projection', color='r', edge_color='r')
    
    # Plot the top view of the original cube
    plot_cube(cube_vertices, title='Top View of Original Cube', color='b', edge_color='b', view_init=(90, 0))
    
    # Plot the front view of the original cube
    plot_cube(cube_vertices, title='Front View of Original Cube', color='b', edge_color='b', view_init=(0, 0))

if __name__ == "__main__":
    main()
