import random
import tkinter as tk

attempts = 0

# Function to generate image puzzles with black shapes and question
def generate_image():
    global attempts
    attempts += 1
    
    # Create a tkinter Canvas
    root = tk.Tk()
    root.title("Image Puzzle")
    
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()
    
    # Draw random black shapes on the canvas
    for _ in range(random.randint(5, 10)):
        x1 = random.randint(0, 350)
        y1 = random.randint(0, 350)
        x2 = x1 + random.randint(50, 100)
        y2 = y1 + random.randint(50, 100)
        
        canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    
    # Randomly select a shape to be clicked
    shapes = canvas.find_all()
    correct_shape = random.choice(shapes)
    
    # Get coordinates of the correct shape
    x1, y1, x2, y2 = canvas.coords(correct_shape)
    
    # Display a question prompting the user to click on the correct shape
    question_text = "Click on the black shape."
    question_id = canvas.create_text(200, 30, text=question_text, font=("Arial", 14))
    
    # Function to check if the user clicked on the correct shape
    def check_click(event):
        global attempts
        x, y = event.x, event.y
        
        # Check if the clicked area matches the correct shape
        clicked_shape = canvas.find_closest(x, y)
        
        if clicked_shape[0] == correct_shape:
            print("Correct! You are a human.")
            root.quit()
        else:
            print("Sorry, wrong click.")
            if attempts < 3:

                root.quit()
                generate_image()
            else:
                print("You are a robot.")
                root.quit()
    
    # Bind the click event to the check_click function
    canvas.bind("<Button-1>", check_click)
    
    root.mainloop()

# Main function
if __name__ == "__main__":
    generate_image()
