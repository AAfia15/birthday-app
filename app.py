import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import time

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Birthday Surprise 🎉", page_icon="🎂", layout="centered")

# ---------- GET NAME FROM URL ----------
query_params = st.query_params
name = query_params.get("name", "Tufail")

# ---------- ANIMATED MESSAGE ----------
message = """Happy Birthday to someone truly special to me, Tufail.

After years of knowing each other, you’ve become someone who holds a very special place in my heart, no matter how much we used to talk or don’t talk now.

I’m really grateful for everything you’ve taught me, for always being there whenever I needed you, and for the way you’ve supported me through so much without ever making it feel ordinary.

You’ve never been just an “ordinary” person to me. You’ve been someone I trusted with my whole heart.

I pray this new year of your life brings you peace, happiness, success, and everything your heart has been quietly wishing for.

May Allah Bless you always."""

placeholder = st.empty()
typed_text = ""

for char in message:
    typed_text += char
    placeholder.markdown(f"## {typed_text}")
    time.sleep(0.02)

st.write("")

# ---------- LOAD IMAGE ----------
image = Image.open("T.jpeg")
width, height = image.size
draw = ImageDraw.Draw(image)

# ---------- FONT ----------
font_title = ImageFont.truetype("Roboto-Regular.ttf", 70)
font_text = ImageFont.truetype("Roboto-Regular.ttf", 45)

# ---------- TEXT ON IMAGE ----------
title = f"Happy Birthday {name}"
date = "16-05-2026"
country = "Spain"

# ---------- POSITION ----------
margin_right = 40
margin_top = 40

title_bbox = draw.textbbox((0, 0), title, font=font_title)
date_bbox = draw.textbbox((0, 0), date, font=font_text)
country_bbox = draw.textbbox((0, 0), country, font=font_text)

title_x = width - (title_bbox[2] - title_bbox[0]) - margin_right
date_x = width - (date_bbox[2] - date_bbox[0]) - margin_right
country_x = width - (country_bbox[2] - country_bbox[0]) - margin_right

title_y = margin_top
date_y = title_y + 90
country_y = date_y + 60

# ---------- DRAW TEXT ----------
draw.text((title_x, title_y), title, fill="black", font=font_title)
draw.text((date_x, date_y), date, fill="black", font=font_text)
draw.text((country_x, country_y), country, fill="black", font=font_text)

# ---------- ANIMATION ----------
st.balloons()

# ---------- SHOW IMAGE ----------
st.image(image, caption="🎂 Dr. Ing. Hafiz Muhammad Tufail Shahzad Mahar")

# ---------- DOWNLOAD BUTTON ----------
img_bytes = io.BytesIO()
image.save(img_bytes, format="PNG")

st.download_button(
    label="📥 Download Birthday Image",
    data=img_bytes.getvalue(),
    file_name="birthday.png",
    mime="image/png"
)
