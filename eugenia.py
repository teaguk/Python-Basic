# to run,copy and paste the code below
# streamlit run eugenia.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/

import streamlit as st
from PIL import Image, ImageDraw


title="Climate Crash"
st.title(title)

description="""
This is a game where you can experience saving the world by killing climate change. 
If you like being in the spotlight, this is the game just for you!
"""
st.write(description)

# Load the image
image_path = "1.png"  # Make sure the image file exists in the same directory
image = Image.open(image_path)

# Convert to RGBA for transparency support
image = image.convert("RGBA")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define circle properties
width, height = image.size
circle_center = (width // 2, height // 2)  # Center of the image
radius = min(width, height) // 4           # 1/4 of the smallest dimension

# Draw the circle (change color as needed)
draw.ellipse(
    (circle_center[0] - radius, circle_center[1] - radius,
     circle_center[0] + radius, circle_center[1] + radius),
    outline="red", width=5  # Red circle with 5px thickness
)

# Display the image with the circle
st.image(image, caption="Image with Circle Overlay", use_container_width=True)
