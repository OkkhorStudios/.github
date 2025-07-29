from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# --- Settings ---
width, height = 800, 250  # Banner size
frames = []
output_path = "okkhor_studios_banner.gif"

# Adjust this path depending on your OS:
# Linux / Mac:
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
# Windows example:
# font_path = "C:/Windows/Fonts/arialbd.ttf"

# --- Text content ---
title_en = "Okkhor Studios"
subtitle_en = "Empowering Students • Creatives • Developers"
title_bn = "অক্ষর স্টুডিওস"
subtitle_bn = "বাংলাদেশের শিক্ষার্থী, ক্রিয়েটিভ ও ডেভেলপারদের জন্য"

# --- Create animated frames ---
for i in range(20):  # 20 frames
    # Dark hacker-style background
    img = Image.new("RGB", (width, height), (15, 15, 20))
    draw = ImageDraw.Draw(img)

    # Color animation for the border (uses sine wave)
    phase = i / 20.0
    border_color = tuple(
        int(127 + 128 * np.sin(2 * np.pi * (phase + j / 3)))
        for j in range(3)
    )

    # Draw glowing border (5 layers for glow effect)
    for r in range(5):
        color = tuple(int(c * (1 - r * 0.1)) for c in border_color)
        draw.rectangle([r, r, width - r - 1, height - r - 1],
                       outline=color, width=3)

    # Load fonts
    font_big = ImageFont.truetype(font_path, 36)
    font_small = ImageFont.truetype(font_path, 20)

    # Center English texts
    draw.text((width // 2, 60), title_en,
              font=font_big, fill=(255, 255, 255), anchor="mm")
    draw.text((width // 2, 100), subtitle_en,
              font=font_small, fill=(180, 255, 180), anchor="mm")

    # Center Bangla texts
    draw.text((width // 2, 150), title_bn,
              font=font_big, fill=(255, 255, 255), anchor="mm")
    draw.text((width // 2, 190), subtitle_bn,
              font=font_small, fill=(255, 220, 180), anchor="mm")

    frames.append(img)

# Save as animated GIF
frames[0].save(output_path,
               save_all=True,
               append_images=frames[1:],
               loop=0,
               duration=120)

print("Banner saved as", os.path.abspath(output_path))
