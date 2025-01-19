from PIL import Image, ImageDraw, ImageFont, ImageOps

def create_text_image(my_text, image_size=(320, 320), background_color='orange', text_color='white'):
    
    # 创建一个橙色背景的图片
    image = Image.new('RGB', image_size, background_color)

    draw = ImageDraw.Draw(image)
    
    # 选择字体和大小
    try:
        # 尝试加载系统字体
        font = ImageFont.truetype("fonts/simsun.ttc", 24)  # 调整字体大小以适应每行8个字
    except IOError:
        # 如果系统字体不可用，使用默认字体
        font = ImageFont.load_default()
    
    # 将文字分割成每行8个字
    lines = [my_text[i:i + 8] for i in range(0, len(my_text), 8)]
    print(lines)
    
    # 获取单行文字的高度
    line_height = font.getbbox('Mg')[3] - font.getbbox('Mg')[1] + 12 # here is the height buffer
    print("line_height: " + str(line_height))
    print("len(lines):" + str(len(lines)))
    
    # 计算起始y坐标
    y = (image_size[1] - len(lines) * line_height) / 2
    print("y(1st): " + str(y))
    
    # 在图片上绘制文字
    for line in lines:
        # 获取当前行文本的宽度
        text_width, _ = 20, 0
        x = (image_size[0] - text_width * 8) / 2  # 计算每行文字的起始x坐标
        print("x: " + str(x))
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height  # 更新y坐标以绘制下一行
        print("y(2nd): " + str(y))

    # 显示图片
    dpi = image.info.get('dpi', (72, 72))
    new_width = int(image_size[0] * (300 / dpi[0]))
    new_height = int(image_size[1] * (300 / dpi[1]))
    img_fitted = ImageOps.fit(image, (new_width, new_height), Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    return img_fitted