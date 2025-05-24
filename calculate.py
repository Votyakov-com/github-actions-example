def calculate_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height
