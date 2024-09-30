import tkinter as tk

# Example data for weight loss progress
weights = [80, 78, 77, 75, 73]
dates = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]

# Function to draw the progress chart using Canvas
def draw_progress_chart():
    canvas.delete("all")  # Clear any previous drawings
    max_weight = max(weights)
    min_weight = min(weights)
    width = 400
    height = 300
    padding = 20

    # Scale weights to fit within the canvas height
    def scale_weight(weight):
        return height - (weight - min_weight) / (max_weight - min_weight) * (height - padding * 2)

    # Draw x and y axis lines
    canvas.create_line(padding, padding, padding, height - padding, fill="black", width=2)
    canvas.create_line(padding, height - padding, width - padding, height - padding, fill="black", width=2)

    # Plot the weight points and lines
    for i in range(len(weights) - 1):
        x1 = padding + (i * (width - 2 * padding) // len(weights))
        y1 = scale_weight(weights[i])
        x2 = padding + ((i + 1) * (width - 2 * padding) // len(weights))
        y2 = scale_weight(weights[i + 1])

        canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill="blue")  # Point
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)  # Line

    # Add labels for the x-axis (dates)
    for i, date in enumerate(dates):
        x = padding + (i * (width - 2 * padding) // len(dates))
        canvas.create_text(x, height - padding + 10, text=date)

# Tkinter window setup
root = tk.Tk()
root.title("Weight Loss Progress")
root.geometry("450x400")

# Create Canvas widget for drawing graph
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=20)

# Button to draw progress chart
draw_button = tk.Button(root, text="Draw Progress Chart", command=draw_progress_chart)
draw_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
