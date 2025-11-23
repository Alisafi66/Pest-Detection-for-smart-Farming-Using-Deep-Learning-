# Set the input and output directories
input_folder="input_images"  # Replace with the path to your folder containing the images
output_folder="output_images"  # Replace with the path to your output folder

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Randomly select 500 images from the input folder
selected_images=$(find "$input_folder" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | shuf -n 500)

# Process each selected image
for image in $selected_images; do
  if [ -f "$image" ]; then
    # Extract the base name of the image (without extension)
    base_name=$(basename "$image" .${image##*.})
    
    # Run the inference for each image
    CUDA_VISIBLE_DEVICES=0 python inference_on_a_image.py \
      -c groundingdino/config/GroundingDINO_SwinB_cfg.py \
      -p weights/groundingdino_swinb_cogcoor.pth \
      -i "$image" \
      -o "$output_folder/${base_name}_output.jpg" \
      -t "pest"
    
    echo "Processed: $image"
  fi
done

echo "Processing complete. Outputs saved to $output_folder."
