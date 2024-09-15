import turtle
import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Default settings
DEFAULT_SEED = 42
DEFAULT_NUM_COLORS = 5
DEFAULT_NUM_LOOPS = 30
DEFAULT_RECURSION_DEPTH = 3
DEFAULT_LINE_THICKNESS = 2  # Default line thickness

# Color palette resembling urban environments (greys, blues, greens, beiges)
COLOR_PALETTE = ['#708090', '#2f4f4f', '#d3d3d3', '#4682b4', '#778899', 
                 '#a9a9a9', '#696969', '#bdb76b', '#8b4513', '#556b2f']
# Neon-inspired color palette
COLOR_PALETTE = ['#ff00ff', '#00ffff', '#ff4500', '#32cd32', '#ff1493', 
                 '#00ff00', '#ff6347', '#8a2be2', '#ffb6c1', '#00fa9a']


class UrbanCamoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Urban Camouflage Pattern Generator")
        self.root.geometry("300x300")

        # Initialize the turtle graphics
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600)
        self.t.speed(0)  # Fastest drawing speed
        self.screen.bgcolor("white")
        self.canvas = self.screen.getcanvas()

        # Create the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Define font size
        font = ('Arial', 12)

        # Seed
        tk.Label(self.root, text="Seed:", font=font).grid(row=0, column=0, padx=10, pady=5)
        self.seed_entry = tk.Entry(self.root, font=font)
        self.seed_entry.insert(0, str(DEFAULT_SEED))
        self.seed_entry.grid(row=0, column=1, padx=10, pady=5)

        # Number of colors
        tk.Label(self.root, text="Number of Colors:", font=font).grid(row=1, column=0, padx=10, pady=5)
        self.num_colors_entry = tk.Entry(self.root, font=font)
        self.num_colors_entry.insert(0, str(DEFAULT_NUM_COLORS))
        self.num_colors_entry.grid(row=1, column=1, padx=10, pady=5)

        # Number of loops
        tk.Label(self.root, text="Number of Loops:", font=font).grid(row=2, column=0, padx=10, pady=5)
        self.num_loops_entry = tk.Entry(self.root, font=font)
        self.num_loops_entry.insert(0, str(DEFAULT_NUM_LOOPS))
        self.num_loops_entry.grid(row=2, column=1, padx=10, pady=5)

        # Recursion depth
        tk.Label(self.root, text="Recursion Depth:", font=font).grid(row=3, column=0, padx=10, pady=5)
        self.recursion_depth_entry = tk.Entry(self.root, font=font)
        self.recursion_depth_entry.insert(0, str(DEFAULT_RECURSION_DEPTH))
        self.recursion_depth_entry.grid(row=3, column=1, padx=10, pady=5)

        # Line thickness
        tk.Label(self.root, text="Line Thickness:", font=font).grid(row=4, column=0, padx=10, pady=5)
        self.line_thickness_entry = tk.Entry(self.root, font=font)
        self.line_thickness_entry.insert(0, str(DEFAULT_LINE_THICKNESS))
        self.line_thickness_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Draw Pattern", font=font, command=self.draw_pattern).grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Save Pattern", font=font, command=self.save_pattern).grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Clear Pattern", font=font, command=self.clear_pattern).grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Exit", font=font, command=self.root.quit).grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    def setup(self):
        """Setup the random seed, background color, turtle colors, and line thickness."""
        random.seed(int(self.seed_entry.get()))
        
        # Pick a random background color and set it as screen background
        bg_color = random.choice(COLOR_PALETTE)
        self.screen.bgcolor(bg_color)
        
        # Remove the background color from the palette
        color_palette = COLOR_PALETTE.copy()
        color_palette.remove(bg_color)
        
        # Choose the colors for drawing from the remaining palette
        colors = random.sample(color_palette, int(self.num_colors_entry.get()))
        
        # Set the turtle line thickness
        self.t.pensize(int(self.line_thickness_entry.get()))
        
        return colors

    def wrap_position(self, x, y):
        """Wrap the position to create a torus-like effect."""
        if x > self.screen.window_width() // 2:
            x = -self.screen.window_width() // 2 + (x - self.screen.window_width() // 2)
        elif x < -self.screen.window_width() // 2:
            x = self.screen.window_width() // 2 + (x + self.screen.window_width() // 2)
        
        if y > self.screen.window_height() // 2:
            y = -self.screen.window_height() // 2 + (y - self.screen.window_height() // 2)
        elif y < -self.screen.window_height() // 2:
            y = self.screen.window_height() // 2 + (y + self.screen.window_height() // 2)
        
        return x, y

    def draw_shape(self, x, y, size, color, depth):
        """Recursively draw a pattern at position (x, y) with the specified size, color, and depth."""
        if depth == 0:
            return

        # Ensure position wraps around if the shape goes out of bounds
        x, y = self.wrap_position(x, y)  
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

        # Choose a random geometric shape
        shape_choice = random.choice(['rectangle', 'circle', 'triangle', 'line'])

        self.t.color(color)
        
        # Start filling the shape with color for closed shapes
        if shape_choice in ['rectangle', 'circle', 'triangle']:
            self.t.begin_fill()

        if shape_choice == 'rectangle':
            for _ in range(2):
                self.t.forward(size)
                self.t.left(90)
                self.t.forward(size / 2)
                self.t.left(90)
        elif shape_choice == 'circle':
            self.t.circle(size / 2)
        elif shape_choice == 'triangle':
            # Randomly rotate triangle to be in different orientations
            angle = random.choice([0, 90, 180, 270])
            self.t.setheading(angle)  # Set turtle's heading to rotate the triangle
            for _ in range(3):
                self.t.forward(size)
                self.t.left(120)
        elif shape_choice == 'line':
            # Randomly choose line orientation: horizontal, vertical, or diagonal
            angle = random.choice([0, 90, 45, -45])
            self.t.setheading(angle)
            self.t.forward(size)
        
        # End filling the shape for closed figures
        if shape_choice in ['rectangle', 'circle', 'triangle']:
            self.t.end_fill()

        # Draw wrapping shapes if the current shape crosses boundaries
        self.draw_wrapping_shape(x, y, size, color, shape_choice)

        # Recursively draw smaller shapes inside
        next_size = size * 0.7  # Scale down size
        next_depth = depth - 1  # Decrease recursion depth

        # Draw at a new location with wrap-around effect
        new_x = x + random.randint(-100, 100)
        new_y = y + random.randint(-100, 100)
        self.draw_shape(new_x, new_y, next_size, random.choice(self.colors), next_depth)

    def draw_wrapping_shape(self, x, y, size, color, shape_choice):
        """Handle wrapping shapes around screen boundaries."""
        wrap_positions = []

        # Check if the shape crosses the right or left boundary
        if x + size > self.screen.window_width() // 2:  # Crosses right
            wrap_positions.append((-self.screen.window_width() // 2 + (x - self.screen.window_width() // 2), y))
        elif x - size < -self.screen.window_width() // 2:  # Crosses left
            wrap_positions.append((self.screen.window_width() // 2 + (x + self.screen.window_width() // 2), y))

        # Check if the shape crosses the top or bottom boundary
        if y + size > self.screen.window_height() // 2:  # Crosses top
            wrap_positions.append((x, -self.screen.window_height() // 2 + (y - self.screen.window_height() // 2)))
        elif y - size < -self.screen.window_height() // 2:  # Crosses bottom
            wrap_positions.append((x, self.screen.window_height() // 2 + (y + self.screen.window_height() // 2)))

        # Draw the shapes that wrap around
        for wrap_x, wrap_y in wrap_positions:
            self.t.penup()
            self.t.goto(wrap_x, wrap_y)
            self.t.pendown()

            self.t.color(color)
            if shape_choice in ['rectangle', 'circle', 'triangle']:
                self.t.begin_fill()

            if shape_choice == 'rectangle':
                for _ in range(2):
                    self.t.forward(size)
                    self.t.left(90)
                    self.t.forward(size / 2)
                    self.t.left(90)
            elif shape_choice == 'circle':
                self.t.circle(size / 2)
            elif shape_choice == 'triangle':
                angle = random.choice([0, 90, 180, 270])
                self.t.setheading(angle)
                for _ in range(3):
                    self.t.forward(size)
                    self.t.left(120)
            elif shape_choice == 'line':
                angle = random.choice([0, 90, 45, -45])
                self.t.setheading(angle)
                self.t.forward(size)

            if shape_choice in ['rectangle', 'circle', 'triangle']:
                self.t.end_fill()

    def draw_pattern(self):
        """Main function to draw the pattern based on user input."""
        self.colors = self.setup()

        num_loops = int(self.num_loops_entry.get())
        recursion_depth = int(self.recursion_depth_entry.get())

        for _ in range(num_loops):
            # Uniformly select positions anywhere on the screen
            x = random.randint(-self.screen.window_width() // 2, self.screen.window_width() // 2)
            y = random.randint(-self.screen.window_height() // 2, self.screen.window_height() // 2)
            size = random.randint(50, 150)
            color = random.choice(self.colors)
            self.draw_shape(x, y, size, color, recursion_depth)

        # Hide turtle after drawing
        self.t.hideturtle()
        self.screen.update()

    def save_pattern(self):
        """Save the pattern to a file."""
        # Prompt user for file name
        file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_name:
            return

        # Ensure proper canvas initialization
        self.root.update()
        
        # Save the screen output to an EPS file
        self.canvas.postscript(file="temp_output.eps")

        # Convert EPS to PNG using Pillow
        img = Image.open("temp_output.eps")
        img.save(file_name, "png")

        print(f"Pattern saved as {file_name}.")

    def clear_pattern(self):
        """Clear the current pattern."""
        self.t.clear()  # Clear the drawing on the canvas
        self.screen.update()  # Update the screen to reflect changes

if __name__ == "__main__":
    root = tk.Tk()
    app = UrbanCamoApp(root)
    root.mainloop()

