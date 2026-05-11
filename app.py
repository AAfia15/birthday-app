import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("🎉 Birthday Image Generator")

# Automatically load your image
image = Image.open("T.jpeg")

width, height = image.size
draw = ImageDraw.Draw(image)

title = "Happy Birthday TufAil"
date = "16-05-2026"
country = "Spain"

font_title = ImageFont.truetype("Roboto-Regular.ttf", 70)
font_text = ImageFont.truetype("Roboto-Regular.ttf", 45)


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

draw.text((title_x, title_y), title, fill="black", font=font_title)
draw.text((date_x, date_y), date, fill="black", font=font_text)
draw.text((country_x, country_y), country, fill="black", font=font_text)

st.image(image, caption="Happy Birthday Dr. Ing. Hafiz Muhammad Tufail Shahzad Mahar 🎂")
