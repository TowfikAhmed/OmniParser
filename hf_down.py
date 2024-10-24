import os
import shutil
from huggingface_hub import hf_hub_download

# Set the model repository
model_repo = "microsoft/OmniParser"

# Define the model files you want to download
model_files = [
    "icon_caption_blip2/pytorch_model-00001-of-00002.bin",
    "icon_caption_blip2/pytorch_model-00002-of-00002.bin",
    "icon_caption_blip2/config.json",
    "icon_caption_blip2/generation_config.json",
    "icon_caption_blip2/pytorch_model.bin.index.json",
    "icon_detect/best.pt"  # Add this line for best.pt
]

# Create a directory to store the downloaded models
download_dir = "weights/omniparser/icon_caption_blip2"
os.makedirs(download_dir, exist_ok=True)

# Download each file
for file in model_files:
    file_path = hf_hub_download(repo_id=model_repo, filename=file)
    # Move the file to your desired download directory using shutil.move
    shutil.move(file_path, os.path.join(download_dir, os.path.basename(file_path)))

print(f"Downloaded model files to {download_dir}")
