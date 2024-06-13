import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the saved model
loaded_model = load_model('wrist_fracture.keras')

# Function to predict image class
def predict_fracture(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize pixel values
    preds = loaded_model.predict(x)
    if preds[0][0] > 0.5:
        return "Non-Fractured"
    else:
        return "Fractured"

# Function to handle file selection
def select_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename()
    if selected_image_path:
        try:
            # Display the selected image
            img = Image.open(selected_image_path)
            # Check if the image mode is supported
            if img.mode not in ['RGB', 'RGBA']:
                raise ValueError("Unsupported image mode")
            img = img.resize((224, 224), Image.BILINEAR)
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img
            # Adjust window size based on image size
            root.geometry(f"{img.width()+100}x{img.height() + 250}")  # Increased width and height
        except ValueError as e:
            result_label.config(text="Error: Unsupported image mode")
        except Exception as e:
            result_label.config(text="Error: " + str(e))

# Function to start prediction
def start_prediction():
    global selected_image_path
    if not selected_image_path:
        result_label.config(text="Please select an image first")
    else:
        predicted_class = predict_fracture(selected_image_path)
        result_label.config(text="Predicted Class: " + predicted_class)

# Create main window
root = tk.Tk()
root.title("Wrist Fracture Classification")

# Set window background color to gray
root.configure(bg="#413835")  # Light gray background

# Create heading label
heading_label = tk.Label(root, text="Wrist Fracture Detection", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")  
heading_label.pack(pady=10)

# Create buttons and labels with custom colors and styling
select_button = tk.Button(root, text="Select Image", command=select_image, bg="#007bff", fg="white", font=("Helvetica", 12, "bold"))  
select_button.pack(pady=10)

predict_button = tk.Button(root, text="Predict", command=start_prediction, bg="#007bff", fg="white", font=("Helvetica", 12, "bold"))  
predict_button.pack(pady=5)

result_label = tk.Label(root, text="Predicted Class: ", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))  
result_label.pack(pady=5)

image_label = tk.Label(root, bg="#413835")  # White background for image display
image_label.pack(pady=5)

# Variable to store selected image path
selected_image_path = None

# Run the Tkinter event loop
root.mainloop()
