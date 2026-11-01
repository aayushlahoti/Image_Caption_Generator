import json
import re
from datetime import datetime
from pathlib import Path


def _safe_stem(filename: str) -> str:
    stem = Path(filename).stem
    return re.sub(r"[^A-Za-z0-9_-]+", "_", stem).strip("_") or "image"


def save_caption(filename: str, caption: str, output_dir: Path) -> Path:
    """Save a caption as JSON in output_dir and return the file path."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    path = output_dir / f"{_safe_stem(filename)}_{timestamp}.json"
    payload = {
        "image": filename,
        "caption": caption,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path