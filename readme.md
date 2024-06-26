
# 3D Shape Projection Visualizer

This Python script visualizes different projections of 3D shapes (cube and wedge) using Matplotlib and NumPy. It supports various views including multiview projections (top, front, side, and 2D orthographic view) and oblique projections (cavalier and cabinet views).

## Features

- **Define Vertices**: Define the vertices and edges of a cube or wedge.
- **Projection Matrices**: Use different matrices for projecting the vertices into various views.
- **Plotting Functions**: Plot multiple views of the shapes in subplots for comprehensive visualization.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Adeen317/MultiView-Oblique-Projections-Computer-Graphics.git
   ```

2. **Install dependencies**:
   ```sh
   pip install numpy matplotlib
   ```

## Usage

1. **Run the script**:
   ```sh
   python Multiview2d_User_input.py
   ```

2. **Select the shape**:
   - Enter `cube` or `wedge` to define the vertices of the chosen shape.

3. **Select the view**:
   - Choose `multiview` to see the top, front, side, and rotated 2D views.
   - Choose `oblique` to see the oblique cavalier and cabinet views.
   - Choose `exit` to terminate the program.

4. **Results**:
   ![Capture](https://github.com/Adeen317/MultiView-Oblique-Projections-Computer-Graphics/assets/112985225/8699b594-b008-40fb-adc5-ff32c1a8c65f)
   ![Capture1](https://github.com/Adeen317/MultiView-Oblique-Projections-Computer-Graphics/assets/112985225/272481e7-435c-41d4-895b-f0eb58cba292)