from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((100, 100))
    pixels = list(image.getdata())
    pixel_counts = Counter(pixels)
    most_common = pixel_counts.most_common(num_colors)
    hex_colors = ["#{:02x}{:02x}{:02x}".format(*color) for color, _ in most_common]
    return hex_colors

if __name__ == '__main__':
    colors = get_dominant_colors('path/to/image.jpg')
    print(colors)