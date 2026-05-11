import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# ---------- PAGE ----------
st.set_page_config(page_title="Birthday Surprise 🎉", page_icon="🎂")

st.title("🎉 Birthday Surprise")

# ---------- GET NAME ----------
query_params = st.query_params
name = query_params.get("name", "Tufail")

# ---------- CLICK BUTTON ----------
if "show_message" not in st.session_state:
    st.session_state.show_message = False

def reveal():
    st.session_state.show_message = True

st.button("🎁 Click to Reveal Message", on_click=reveal)

# ---------- MESSAGE ----------
message = """Happy Birthday to someone truly special to me, Tufail.

After years of knowing each other, you’ve become someone who holds a very special place in my heart.

I’m really grateful for everything you’ve taught me and for always being there.

You’ve never been just an ordinary person to me.

I pray this new year brings you peace, happiness, and success.

May Allah Bless you always."""

if st.session_state.show_message:
    st.markdown("### 💌 Your Message")
    st.info(message)

# ---------- IMAGE ----------
image = Image.open("T.jpeg")
draw = ImageDraw.Draw(image)

font_title = ImageFont.truetype("Roboto-Regular.ttf", 70)
font_text = ImageFont.truetype("Roboto-Regular.ttf", 45)

title = f"Happy Birthday {name}"
date = "16-05-2026"
country = "Spain"

margin_right = 40
margin_top = 40

title_bbox = draw.textbbox((0, 0), title, font=font_title)
date_bbox = draw.textbbox((0, 0), date, font=font_text)
country_bbox = draw.textbbox((0, 0), country, font=font_text)

title_x = image.width - (title_bbox[2] - title_bbox[0]) - margin_right
date_x = image.width - (date_bbox[2] - date_bbox[0]) - margin_right
country_x = image.width - (country_bbox[2] - country_bbox[0]) - margin_right

draw.text((title_x, margin_top), title, fill="black", font=font_title)
draw.text((date_x, margin_top + 90), date, fill="black", font=font_text)
draw.text((country_x, margin_top + 150), country, fill="black", font=font_text)

st.balloons()
st.image(image, caption="🎂 Dr. Ing. Hafiz Muhammad Tufail Shahzad Mahar🎉")

# ---------- DOWNLOAD ----------
img_bytes = io.BytesIO()
image.save(img_bytes, format="PNG")

st.download_button(
    "📥 Download Image",
    img_bytes.getvalue(),
    "birthday.png",
    "image/png"
)
