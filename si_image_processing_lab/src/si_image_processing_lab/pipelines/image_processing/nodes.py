from PIL import Image, ImageFilter, ImageDraw
def process_image(
    input_path: str,
    output_path: str,
    rotation_angle: int,
    filter_name: str,
    watermark_text: str,
):
    image = Image.open(input_path)
    rotated = image.rotate(rotation_angle)
    filters = {
        "EMBOSS": ImageFilter.EMBOSS,
        "FIND_EDGES": ImageFilter.FIND_EDGES,
    }
    selected_filter = filters.get(filter_name, ImageFilter.EMBOSS)
    filtered = rotated.filter(selected_filter)
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), watermark_text, fill="white")
    filtered.save(output_path)
    return output_path