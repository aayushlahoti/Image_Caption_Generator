from config.config import Config
from preprocessing.image_processor import preprocess
from utils.file_handler import save_caption
from utils.validator import validate_upload


class CaptionService:
    """Orchestrates validation -> preprocessing -> model -> (optional) saving."""

    def __init__(self, model, cfg: Config):
        self.model = model
        self.cfg = cfg

    def generate_caption(self, filename: str, data: bytes, prompt: str | None = None) -> dict:
        validate_upload(filename, data, self.cfg.ALLOWED_EXTENSIONS, self.cfg.MAX_UPLOAD_MB)
        image = preprocess(data, self.cfg.MAX_IMAGE_SIDE)
        caption = self.model.generate(image, prompt=prompt)

        saved_to = None
        if self.cfg.SAVE_CAPTIONS:
            saved_to = str(save_caption(filename, caption, self.cfg.OUTPUT_DIR))

        return {"filename": filename, "caption": caption, "saved_to": saved_to}