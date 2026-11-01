import torch
from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor


class CaptionModel:
    """Thin wrapper around BLIP for image captioning (lazy-loaded)."""

    def __init__(self, model_name: str, max_length: int = 50, num_beams: int = 5, device: str | None = None):
        self.model_name = model_name
        self.max_length = max_length
        self.num_beams = num_beams
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._processor = None
        self._model = None

    def load(self) -> None:
        if self._model is not None:
            return
        self._processor = BlipProcessor.from_pretrained(self.model_name)
        self._model = BlipForConditionalGeneration.from_pretrained(self.model_name)
        self._model.to(self.device)
        self._model.eval()

    def generate(self, image: Image.Image, prompt: str | None = None) -> str:
        """Generate a caption. `prompt` optionally conditions it (e.g. 'a photo of')."""
        self.load()
        if prompt:
            inputs = self._processor(images=image, text=prompt, return_tensors="pt")
        else:
            inputs = self._processor(images=image, return_tensors="pt")
        inputs = inputs.to(self.device)
        with torch.inference_mode():
            output_ids = self._model.generate(
                **inputs, max_length=self.max_length, num_beams=self.num_beams
            )
        return self._processor.decode(output_ids[0], skip_special_tokens=True).strip()