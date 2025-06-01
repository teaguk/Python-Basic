# to run,copy and paste the code below
# streamlit run eugenia.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/

import streamlit as st
import base64


title="Climate Crash"
st.title(title)

description="""
I made this game based on sdgs 13. its about a young animal
trying to save its village from climate change! help the animal
and make it happy!!
"""
st.write(description)
image_1 = "1.png"
image_2 = "2.png"

# Session state to track current image
if "current_image" not in st.session_state:
    st.session_state.current_image = image_1

# Button to switch the image
if st.button("Click here to continue"):
    # Swap the image
    if st.session_state.current_image == image_1:
        st.session_state.current_image = image_2
    else:
        st.session_state.current_image = image_1
# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the image file.
image_path_1 = "./1.png"  # Change this to your image file path.

# Encode the image to a base64 string.
encoded_image_1 = get_base64_image(image_path_1)

# HTML code that displays the image with an overlay clickable area.
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Container to hold the image and position the clickable area relative to it */
    .container {{
      position: relative;
      display: inline-block;
    }}
    /* Clickable area overlay positioned over the image */
    .clickable-area {{
      position: absolute;
      top: 80px;         /* Distance from the top of the container */
      left: 270px;       /* Distance from the left of the container */
      width: 60px;      /* Width of the clickable area */
      height: 65px;     /* Height of the clickable area */
      cursor: pointer;   /* Change the mouse pointer to indicate clickable area */
      border: 2px solid red; /* Red border to visually identify the clickable area */
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Display the image using the base64 encoded string -->
    <img src="data:image/jpeg;base64,{encoded_image_1}" width="600" alt="Clickable Image">
    <!-- Div element that acts as the clickable overlay area -->
    <div class="clickable-area" onclick="handleClick()"></div>
  </div>
  <script>
    // Function that is executed when the clickable area is clicked.
    function handleClick() {{
      // Display a JavaScript alert when the area is clicked.
      window.alert("The clickable area has been clicked!");
    }}
  </script>
</body>
</html>
"""

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
