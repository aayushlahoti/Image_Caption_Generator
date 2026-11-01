import io
from pathlib import Path

from PIL import Image, UnidentifiedImageError


class ValidationError(ValueError):
    """Raised when an uploaded file is not acceptable."""


def validate_extension(filename: str, allowed: tuple) -> None:
    ext = Path(filename).suffix.lower()
    if ext not in allowed:
        raise ValidationError(
            f"Unsupported file type '{ext or 'none'}'. Allowed: {', '.join(allowed)}"
        )


def validate_size(size_bytes: int, max_mb: int) -> None:
    if size_bytes == 0:
        raise ValidationError("The uploaded file is empty.")
    if size_bytes > max_mb * 1024 * 1024:
        raise ValidationError(f"File is too large. Maximum size is {max_mb} MB.")


def validate_image_bytes(data: bytes) -> None:
    try:
        with Image.open(io.BytesIO(data)) as img:
            img.verify()
    except (UnidentifiedImageError, OSError, SyntaxError):
        raise ValidationError("The file is not a valid image or is corrupted.")


def validate_upload(filename: str, data: bytes, allowed: tuple, max_mb: int) -> None:
    validate_extension(filename, allowed)
    validate_size(len(data), max_mb)
    validate_image_bytes(data)