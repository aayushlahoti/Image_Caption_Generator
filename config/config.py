import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:  # python-dotenv is optional; env vars still work
    pass

BASE_DIR = Path(__file__).resolve().parent.parent


def _bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Config:
    MODEL_NAME: str = os.getenv("MODEL_NAME", "Salesforce/blip-image-captioning-base")
    MAX_LENGTH: int = int(os.getenv("MAX_LENGTH", "50"))
    NUM_BEAMS: int = int(os.getenv("NUM_BEAMS", "5"))
    MAX_UPLOAD_MB: int = int(os.getenv("MAX_UPLOAD_MB", "10"))
    MAX_IMAGE_SIDE: int = int(os.getenv("MAX_IMAGE_SIDE", "1024"))
    SAVE_CAPTIONS: bool = _bool(os.getenv("SAVE_CAPTIONS", "true"))
    ALLOWED_EXTENSIONS: tuple = (".jpg", ".jpeg", ".png", ".webp", ".bmp")
    OUTPUT_DIR: Path = BASE_DIR / "outputs" / "captions"


config = Config()