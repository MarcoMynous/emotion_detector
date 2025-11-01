from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import io

# Load your model and processor
processor = AutoImageProcessor.from_pretrained("trpakov/vit-face-expression")
model = AutoModelForImageClassification.from_pretrained("trpakov/vit-face-expression")

def predict_emotion(image_input):
    # If it's a Streamlit UploadedFile
    if hasattr(image_input, "getvalue"):
        image_bytes = image_input.getvalue()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    else:
        # Otherwise assume it's a file path
        image = Image.open(image_input).convert("RGB")

    # Force the image into a list (batch of 1) and activate padding
    inputs = processor(images=[image], return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()

    label = model.config.id2label[predicted_class_idx]
    return label
