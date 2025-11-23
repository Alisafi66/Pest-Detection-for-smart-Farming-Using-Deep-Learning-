import os
import subprocess

# Define the directories
input_dir = 'stem_borer'  # Directory containing the images
output_dir = 'stem_borer_out'  # Directory to save the output

# Ensure the input directory exists
if not os.path.exists(input_dir):
    print(f"Input directory {input_dir} does not exist.")
    exit(1)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

# If no images are found, print a message and exit
if not image_files:
    print(f"No image files found in {input_dir}.")
    exit(1)

# Iterate through all the images
for image_file in image_files:
    # Construct the full input and output paths
    input_image_path = os.path.join(input_dir, image_file)
    output_image_path = os.path.join(output_dir, f"{os.path.splitext(image_file)[0]}_output")
    
    # Build the command with the current image
    command = [
        'CUDA_VISIBLE_DEVICES=0', 'python', 'inference_on_a_image.py',
        '-c', 'groundingdino/config/GroundingDINO_SwinB_cfg.py',
        '-p', 'weights/groundingdino_swinb_cogcoor.pth',
        '-i', input_image_path,
        '-o', output_image_path,
        '-t', 'pest'
    ]
    
    # Run the command
    subprocess.run(command)
