import rotatescreen
import time
import streamlit as st

st.title("Welcome to funplay :)")

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

if st.button("click me!, and have fun"):
    for i in range(1,5):
        pos = abs((start_pos - i*90) % 360)
        screen.rotate_to(pos)
        time.sleep(0.5)
