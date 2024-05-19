import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_shear_matrix(xwmin, xwmax, ywmin, ywmax, znear):
    shzx = -(xwmin + xwmax) / (2 * znear)
    shzy = -(ywmin + ywmax) / (2 * znear)

    shear_matrix = np.array([
        [1, 0, shzx, 0],
        [0, 1, shzy, 0],
        [0, 0,    1, 0],
        [0, 0,    0, 1]
    ])

    return shear_matrix

def create_perspective_projection_matrix(znear, zfar):
    sz = zfar / (zfar - znear)
    tz = -znear * sz

    perspective_matrix = np.array([
        [-znear,     0,     0,  0],
        [     0, -znear,     0,  0],
        [     0,      0,    sz, tz],
        [     0,      0,    -1,  0]
    ])

    return perspective_matrix

def apply_transformation(matrix, point):
    point_homogeneous = np.append(point, 1)
    transformed_point = matrix @ point_homogeneous
    transformed_point_cartesian = transformed_point[:-1] / transformed_point[-1]
    return transformed_point_cartesian

def plot_cube(ax, vertices, color='b', alpha=0.1, edge_color='k'):
    faces = [[vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [7, 6, 2, 3]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]]]

    poly3d = [[tuple(face[i]) for i in range(len(face))] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, edgecolors=edge_color, alpha=alpha))

def main():
    xwmin, xwmax = -1, 1
    ywmin, ywmax = -1, 1
    znear, zfar = 1, 10

    shear_matrix = create_shear_matrix(xwmin, xwmax, ywmin, ywmax, znear)
    perspective_matrix = create_perspective_projection_matrix(znear, zfar)
    oblique_perspective_matrix = perspective_matrix @ shear_matrix

    cube_vertices = np.array([
        [0.5, 0.5, 2],
        [0.5, -0.5, 2],
        [-0.5, -0.5, 2],
        [-0.5, 0.5, 2],
        [0.5, 0.5, 3],
        [0.5, -0.5, 3],
        [-0.5, -0.5, 3],
        [-0.5, 0.5, 3]
    ])

    transformed_vertices = np.array([apply_transformation(oblique_perspective_matrix, v) for v in cube_vertices])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plot_cube(ax, cube_vertices, color='b', alpha=0.1, edge_color='b')
    plot_cube(ax, transformed_vertices, color='r', alpha=0.1, edge_color='r')

    for i in range(len(cube_vertices)):
        ax.plot([cube_vertices[i, 0], transformed_vertices[i, 0]],
                [cube_vertices[i, 1], transformed_vertices[i, 1]],
                [cube_vertices[i, 2], transformed_vertices[i, 2]], 'gray')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Oblique Perspective Projection Transformation of a Cube')
    plt.show()

if __name__ == "__main__":
    main()
