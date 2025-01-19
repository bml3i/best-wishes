from PIL import Image, ImageDraw, ImageFont, ImageOps
from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from blessing_model import Blessing

import re

def create_text_image(my_text, image_size=(320, 320), background_color='orange', text_color='white', delimiters=r'[，。,.\n]'):
    # New Image
    image = Image.new('RGB', image_size, background_color)
    draw = ImageDraw.Draw(image)

    FONT_SIZE = 24
    
    try:
        font = ImageFont.truetype("fonts/simsun.ttc", FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()
    
    # Split words into multi-lines    
    text_array = re.sub(delimiters, ' ', my_text)
    lines = text_array.split()
    max_line_words_len = max(map(len, lines))

    EXTRA_HEIGHT_BUFFER = 12
    line_height = (font.getbbox('Mg')[3] - font.getbbox('Mg')[1]) + EXTRA_HEIGHT_BUFFER
    word_width = (font.getbbox('Mg')[2] - font.getbbox('Mg')[0])

    y = (image_size[1] - len(lines) * line_height) / 2
    
    # Draw text on the image
    for line in lines:
        x = (image_size[0] - word_width * max_line_words_len) / 2
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height

    # Change Image dpi to 300
    dpi = image.info.get('dpi', (72, 72))
    new_width = int(image_size[0] * (300 / dpi[0]))
    new_height = int(image_size[1] * (300 / dpi[1]))
    img_fitted = ImageOps.fit(image, (new_width, new_height), Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    return img_fitted


def count_any_chars(s):
    count = 0
    for char in s:
        if '\u4e00' <= char <= '\u9fff' or char.isalpha():
            count += 1
    return count


def generate_my_blessing(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=Blessing)
    chain = prompt | model | output_parser
    print("get_format_instructions: " + output_parser.get_format_instructions())
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result