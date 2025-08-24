from urllib.parse import urlparse
import streamlit as st

st.set_page_config(page_title="My Roblox Links Dashboard", page_icon="🎮", layout="wide")

# CSS for background and cards
st.markdown("""
<style>
.stApp {
    background-color: #d6eaff;
    background-image: url('https://www.pngmart.com/files/7/Roblox-Noob-PNG-Image.png');
    background-repeat: repeat;
    background-size: 100px 100px;
    background-position: top left;
}

.card {
    border-radius: 16px;
    box-shadow: 4px 4px 12px rgba(0,0,0,0.1);
    transition: transform 0.2s, box-shadow 0.2s;
    border: 3px solid #ff1493;
    margin: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    background-color: rgba(255,230,235,0.95);
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 6px 6px 16px rgba(0,0,0,0.15);
}

.card a { display: inline-block; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🎮 My Roblox Links Dashboard")

LINKS = [
    "https://www.roblox.com/games/126884695634066/Grow-a-Garden",
    "https://www.roblox.com/games/79546208627805/99-Nights-in-the-Forest",
    "https://www.roblox.com/games/109983668079237/Steal-a-Brainrot",
    "https://www.roblox.com/games/17625359962/RIVALS",
    "https://www.roblox.com/games/6445435958/unnamed",
    "https://www.roblox.com/games/15101393044/LADY-GAGA-Dress-To-Impress",
    "https://www.roblox.com/games/6737970321/Livetopia-RP#!/game-instances",
    "https://www.roblox.com/games/5985232436/Infectious-Smile-SUMMER"
]

def extract_name(url: str) -> str:
    try:
        path = urlparse(url).path.strip("/")
        parts = path.split("/")
        if len(parts) >= 3 and parts[0].lower() == "games":
            return parts[2].replace("-", " ")
        return parts[-1].replace("-", " ") if parts else url
    except:
        return url

# --- SEARCH BAR ---
search_term = st.text_input("🔍 Search Roblox games by name:")

# Filter links based on search term
filtered_links = []
for link in LINKS:
    name = extract_name(link)
    if search_term.lower() in name.lower():
        filtered_links.append(link)

# Display info if no results
if search_term and not filtered_links:
    st.warning("No games found with that name!")
else:
    display_links = filtered_links if search_term else LINKS

    cols_per_row = 3
    for i in range(0, len(display_links), cols_per_row):
        cols = st.columns(cols_per_row, gap="large")
        for col, link in zip(cols, display_links[i:i+cols_per_row]):
            name = extract_name(link)
            with col:
                st.markdown(f"""
                <div class="card">
                    <div style="font-size:16px;font-weight:bold;color:#333;margin-bottom:12px;text-align:center;">
                        {name}
                    </div>
                    <a href="{link}" target="_blank"
                       style="padding:10px 20px;border-radius:8px;
                              background-color:#4CAF50;color:white;
                              text-decoration:none;font-weight:bold;">
                        Open Game
                    </a>
                </div>
                """, unsafe_allow_html=True)











