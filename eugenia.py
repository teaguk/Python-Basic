# to run,copy and paste the code below
# streamlit run eugenia.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/

import streamlit as st

st.title("a tale of :blue[the girls] : da coding teacher:")

# Input field for user's name
name = st.text_input("Enter your name:")

# Display greeting message at the top as soon as the user enters their name
if name:
    st.markdown(f"<h2 style='text-align: center; color: green;'>Hello, {name}! Enjoy the book! 😊</h2>", unsafe_allow_html=True)


# Story text
story = """
Eugenia, Alice, Eiley, Yuna, and Tara were brilliant coders who had long heard whispers of the Evil Coding Teacher—a villain who was known for luring the most talented coders into his traps and keeping them locked in his digital dungeon. He had been a legend, one that no one had dared to challenge... until now.

It all started one sunny afternoon when Elena, the sixth member of their group, vanished without a trace. The girls had been working on a new project in their clubhouse when Elena had gotten a mysterious message on her laptop—a puzzle challenge unlike any they had seen before. She was excited at the challenge but warned the others she would be back soon. However, minutes turned into hours, and Elena didn’t return.

Panicked, the girls checked her laptop and saw the final message: “You’ve just been hacked. Come find me if you dare. - The Evil Coding Teacher.” It was signed with a digital signature that sent shivers down their spines. Elena had been kidnapped.

Determined to save their friend, the girls raced to the forest, where they knew the Evil Coding Teacher's tower was hidden. As they approached, they encountered the first of his deadly traps—a virtual firewall that burned like fire. Zoe, the genius hacker of the group, quickly bypassed the firewall, but they knew this was just the beginning.

The deeper they ventured into the tower, the more dangerous the traps became. Strange creatures made of corrupted code tried to attack them, but Eiley used her quick thinking and code manipulation to create illusions, distracting the creatures while Tara and Yuna disabled traps and coded new paths to move forward.

Finally, after what felt like hours of navigating through dark mazes and dodging digital enemies, they reached the heart of the tower. In a cold, eerie chamber, they saw Elena, locked inside a cage made of complex, shifting code. The Evil Coding Teacher was there, his face flickering on a hologram. “I’ve waited so long for someone to challenge me,” he sneered. “But you’re too late. Elena will never escape my puzzles!”

With determination in their eyes, the girls got to work. They had one chance to solve the final, impossible puzzle that held Elena captive. As the code morphed and changed with every attempt, the walls of the chamber seemed to close in, their every move watched by the Evil Coding Teacher’s mocking gaze.

But they didn’t give up. Working as one, they cracked the code, piece by piece, until the cage shattered. Elena was free, and the Evil Coding Teacher’s power finally crumbled. He screamed in rage as his digital form flickered and disappeared, the last remnants of his corrupted code vanishing into the ether.

Breathing heavily, the girls rushed to Elena, hugging her tightly. “I knew you’d come for me,” she said, her voice filled with relief.

They left the tower, knowing they had defeated the long-wanted villain, but as they walked away, the faint hum of static lingered in the air. The Evil Coding Teacher might have been gone for now, but the girls knew this was just one chapter in their coding adventures.

The End... or is it?
"""

# Display the story using st.write
st.write(story)

