from PIL import Image, ImageDraw, ImageFont, ImageOps

def create_text_image(my_text, image_size=(320, 320), background_color='orange', text_color='white'):
    
    image = Image.new('RGB', image_size, background_color)

    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("fonts/simsun.ttc", 24)  # 调整字体大小以适应每行8个字
    except IOError:
        font = ImageFont.load_default()
    
    # 将文字分割成每行8个字
    lines = [my_text[i:i + 8] for i in range(0, len(my_text), 8)]
    print(lines)
    print("len(lines):" + str(len(lines)))
    
    # 获取单行文字的高度
    EXTRA_HEIGHT_BUFFER = 12
    line_height = (font.getbbox('Mg')[3] - font.getbbox('Mg')[1]) + EXTRA_HEIGHT_BUFFER
    word_width = (font.getbbox('Mg')[2] - font.getbbox('Mg')[0]) 

    y = (image_size[1] - len(lines) * line_height) / 2
    
    # Draw text on the image
    for line in lines:
        x = (image_size[0] - word_width * 8) / 2
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height

    # Change Image DPI
    dpi = image.info.get('dpi', (72, 72))
    new_width = int(image_size[0] * (300 / dpi[0]))
    new_height = int(image_size[1] * (300 / dpi[1]))
    img_fitted = ImageOps.fit(image, (new_width, new_height), Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    return img_fitted