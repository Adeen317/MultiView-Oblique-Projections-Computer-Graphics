import tkinter as tk
from tkinter import Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def multiview_projection(cube, matrix):
    viewed_matrix = np.dot(matrix, cube)
    return viewed_matrix

def draw_plot(ax, view, edges, labels):
    ax.clear()
    for edge in edges:
        ax.plot([view[0, edge[0]], view[0, edge[1]]],
                [view[1, edge[0]], view[1, edge[1]]], 'b')
    ax.set_title(labels['title'])
    ax.set_xlabel(labels['xlabel'])
    ax.set_ylabel(labels['ylabel'])
    canvas.draw()

def show_plot(plot_func):
    fig.clf()
    ax = fig.add_subplot(111)
    plot_func(ax)
    canvas.draw()

def plot_original_3d(ax):
    ax = fig.add_subplot(111, projection='3d')
    for edge in edges:
        ax.plot([cube[0, edge[0]], cube[0, edge[1]]],
                [cube[1, edge[0]], cube[1, edge[1]]],
                [cube[2, edge[0]], cube[2, edge[1]]], 'b')
    ax.set_title("Original 3D")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

def plot_front_view(ax):
    draw_plot(ax, front_view, edges, {'title': "Front View", 'xlabel': 'X', 'ylabel': 'Z'})

def plot_side_view(ax):
    draw_plot(ax, side_view, edges, {'title': "Side View", 'xlabel': 'Y', 'ylabel': 'Z'})

def plot_top_view(ax):
    draw_plot(ax, top_view, edges, {'title': "Top View", 'xlabel': 'X', 'ylabel': 'Y'})

def plot_new_view(ax):
    draw_plot(ax, new_view, edges, {'title': "New View (Rotation 1)", 'xlabel': 'X', 'ylabel': 'Y'})

def plot_new_view2(ax):
    draw_plot(ax, new_view2, edges, {'title': "New View (Rotation 1 + Rotation 2)", 'xlabel': 'X', 'ylabel': 'Y'})

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
                  [0, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

side = np.array([[0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

rotation1 = np.array([[0.707, 0, 0.707, 0],
                      [0, 1, 0, 0],
                      [-0.707, 0, 0.707, 0],
                      [0, 0, 0, 1]])

rotation2 = np.array([[1, 0, 0, 0],
                      [0, 0.814, -0.580, 0],
                      [0, 0.580, 0.814, 0],
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

# Create main window
root = tk.Tk()
root.title("3D Cube Projections")

# Create a figure
fig = plt.figure(figsize=(6, 4))

# Create a canvas to draw the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create a menu
menu = Menu(root)
root.config(menu=menu)

# Create a submenu
sub_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Views", menu=sub_menu)
sub_menu.add_command(label="Original 3D", command=lambda: show_plot(plot_original_3d))
sub_menu.add_command(label="Front View", command=lambda: show_plot(plot_front_view))
sub_menu.add_command(label="Side View", command=lambda: show_plot(plot_side_view))
sub_menu.add_command(label="Top View", command=lambda: show_plot(plot_top_view))
sub_menu.add_command(label="New View (Rotation 1)", command=lambda: show_plot(plot_new_view))
sub_menu.add_command(label="New View (Rotation 1 + Rotation 2)", command=lambda: show_plot(plot_new_view2))

# Start with the Original 3D plot
show_plot(plot_original_3d)

# Run the application
root.mainloop()
