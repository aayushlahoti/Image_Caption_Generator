import io

from PIL import Image, ImageOps


def load_image(data: bytes) -> Image.Image:
    """Decode bytes, fix EXIF rotation and convert to RGB."""
    img = Image.open(io.BytesIO(data))
    img = ImageOps.exif_transpose(img)
    return img.convert("RGB")


def resize_image(img: Image.Image, max_side: int) -> Image.Image:
    """Downscale so the longest side is <= max_side (never upscales)."""
    w, h = img.size
    longest = max(w, h)
    if longest <= max_side:
        return img
    scale = max_side / longest
    new_size = (max(1, round(w * scale)), max(1, round(h * scale)))
    return img.resize(new_size, Image.Resampling.LANCZOS)


def preprocess(data: bytes, max_side: int = 1024) -> Image.Image:
    return resize_image(load_image(data), max_side)