import os
import subprocess

# Define the input and output directories
input_folder = "renamed_images"
output_folder = "output"

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get the list of images (523 max)
image_list = sorted(
    [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
)[:523]

# Process each image
for image in image_list:
    # Extract the base name
    base_name = os.path.splitext(os.path.basename(image))[0]

    # Construct the output path
    output_path = os.path.join(output_folder, f"{base_name}_output")

    # Run the inference command
    command = [
        "CUDA_VISIBLE_DEVICES=0",
        "python",
        "inference_on_a_image.py",
        "-c", "groundingdino/config/GroundingDINO_SwinB_cfg.py",
        "-p", "weights/groundingdino_swinb_cogcoor.pth",
        "-i", image,
        "-o", output_path,
        "-t", "pest",
    ]
    # Run the command
    subprocess.run(" ".join(command), shell=True)

    print(f"Finished processing: {image}")

print("All 523 images have been processed.")
