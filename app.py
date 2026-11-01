import io

import streamlit as st
from PIL import Image

from config.config import config
from models.caption_model import CaptionModel
from services.caption_service import CaptionService
from utils.validator import ValidationError

st.set_page_config(page_title="Image Caption Generator", page_icon="🖼️", layout="centered")


@st.cache_resource(show_spinner="Loading model (first run downloads weights)...")
def get_service() -> CaptionService:
    model = CaptionModel(config.MODEL_NAME, config.MAX_LENGTH, config.NUM_BEAMS)
    model.load()
    return CaptionService(model, config)


st.title("🖼️ Image Caption Generator")
st.write("Upload an image and get an AI-generated caption.")

uploaded = st.file_uploader(
    "Choose an image",
    type=[ext.lstrip(".") for ext in config.ALLOWED_EXTENSIONS],
)

if uploaded is not None:
    data = uploaded.getvalue()
    try:
        st.image(Image.open(io.BytesIO(data)), caption=uploaded.name, use_container_width=True)
    except Exception:
        st.error("Could not display this file as an image.")

    if st.button("Generate caption", type="primary"):
        try:
            with st.spinner("Generating caption..."):
                result = get_service().generate_caption(uploaded.name, data)
            st.success("Caption generated")
            st.subheader(result["caption"])
            st.code(result["caption"], language=None)  # easy copy button
        except ValidationError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Something went wrong while generating the caption: {e}")