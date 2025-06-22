# to run,copy and paste the code below
# streamlit run eugenia.py --server.port 8080 --server.address 0.0.0.0
import streamlit as st
import base64

st.title("Climate Crash")

description = """
I made this game based on SDG 13. It's about a young animal  
trying to save its village from climate change! Help the animal  
and make it happy!!
"""
st.write(description)

# Encode images to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image1_base64 = get_base64_image("1.png")
image2_base64 = get_base64_image("2.png")
image3_base64 = get_base64_image("3.png")
image4_base64 = get_base64_image("4.png")
chicken_base64 = get_base64_image("chicken.png")

# HTML + JS
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      display: inline-block;
      outline: none;
    }}
    .clickable-area {{
      position: absolute;
      width: 60px;
      height: 65px;
      cursor: pointer;
      border: 2px solid red;
    }}
    .multi-box {{
      display: none;
    }}
    .fade-text {{
      opacity: 0;
      transition: opacity 2s ease-in-out;
      font-size: 20px;
      font-weight: bold;
      color: white;
      text-shadow: 2px 2px 4px black;
      position: absolute;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      text-align: center;
      width: 100%;
    }}
    .visible {{
      opacity: 1;
    }}
    .blackout {{
      position: absolute;
      top: 0;
      left: 0;
      width: 600px;
      height: 100%;
      background-color: black;
      z-index: 10;
      display: none;
    }}
    .chicken {{
      position: absolute;
      bottom: 20px;
      left: 220px;
      width: 100px;
      display: none;
      z-index: 5;
    }}
    .speech {{
      position: absolute;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 20px;
      color: yellow;
      font-weight: bold;
      background-color: rgba(0, 0, 0, 0.6);
      padding: 10px 20px;
      border-radius: 10px;
      display: none;
      z-index: 11;
    }}
  </style>
</head>
<body>
  <div class="container" tabindex="0" onkeydown="moveChicken(event)">
    <img id="main-image" src="data:image/png;base64,{image1_base64}" width="600" alt="Game Image">

    <!-- Clickable box for 1.png -->
    <div id="box1" class="clickable-area" style="top: 80px; left: 270px;" onclick="changeImage()"></div>

    <!-- 6 boxes for 2.png -->
    <div id="box2" class="clickable-area multi-box" style="top: 120px; left: 65px;" onclick="boxClicked(1)"></div>
    <div id="box3" class="clickable-area multi-box" style="top: 120px; left: 210px;" onclick="boxClicked(2)"></div>
    <div id="box4" class="clickable-area multi-box" style="top: 125px; left: 370px;" onclick="boxClicked(3)"></div>
    <div id="box5" class="clickable-area multi-box" style="top: 230px; left: 150px;" onclick="boxClicked(4)"></div>
    <div id="box6" class="clickable-area multi-box" style="top: 120px; left: 515px;" onclick="boxClicked(5)"></div>
    <div id="box7" class="clickable-area multi-box" style="top: 220px; left: 455px;" onclick="boxClicked(6)"></div>

    <!-- Fade-in narration for 3.png -->
    <div id="fade-text" class="fade-text">It was a peaceful day until the Evil Dude came by...</div>

    <!-- Blackout transition -->
    <div id="blackout" class="blackout"></div>

    <!-- Chicken character -->
    <img id="chicken" class="chicken" src="data:image/png;base64,{chicken_base64}" />

    <!-- Chicken's speech -->
    <div id="chicken-speech" class="speech">I have to do something!</div>
  </div>

  <script>
    let currentImage = "1";
    let chickenLeft = 220;
    let movementAllowed = false;

    function changeImage() {{
      if (currentImage === "1") {{
        document.getElementById("main-image").src = "data:image/png;base64,{image2_base64}";
        document.getElementById("box1").style.display = "none";

        const boxes = document.getElementsByClassName("multi-box");
        for (let i = 0; i < boxes.length; i++) {{
          boxes[i].style.display = "block";
        }}
        currentImage = "2";
      }}
    }}

    function boxClicked(boxNumber) {{
      if (currentImage === "2" && boxNumber === 1) {{
        document.getElementById("main-image").src = "data:image/png;base64,{image3_base64}";
        const boxes = document.getElementsByClassName("multi-box");
        for (let i = 0; i < boxes.length; i++) {{
          boxes[i].style.display = "none";
        }}

        const fadeText = document.getElementById("fade-text");
        fadeText.classList.add("visible");

        currentImage = "3";

        setTimeout(() => {{
          fadeText.style.display = "none";
          const blackout = document.getElementById("blackout");
          blackout.style.display = "block";

          setTimeout(() => {{
            blackout.style.display = "none";
            document.getElementById("main-image").src = "data:image/png;base64,{image4_base64}";
            document.getElementById("chicken").style.display = "block";
            document.getElementById("chicken-speech").style.display = "block";
            document.querySelector(".container").focus();
            currentImage = "4";

            // After 2 seconds, hide text and allow movement
            setTimeout(() => {{
              document.getElementById("chicken-speech").style.display = "none";
              movementAllowed = true;
            }}, 2000);
          }}, 3000);
        }}, 2500);
      }} else {{
        alert("Coming soon...");
      }}
    }}

    function moveChicken(event) {{
      if (!movementAllowed) return;
      const chicken = document.getElementById("chicken");
      if (!chicken) return;

      if (event.key === "ArrowLeft") {{
        chickenLeft = Math.max(0, chickenLeft - 20);
        chicken.style.left = chickenLeft + "px";
      }} else if (event.key === "ArrowRight") {{
        chickenLeft = Math.min(500, chickenLeft + 20);
        chicken.style.left = chickenLeft + "px";
      }}
    }}
  </script>
</body>
</html>
"""

# Render in Streamlit
st.components.v1.html(html_code, height=800)