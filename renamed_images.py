# Define the input folder
input_folder="renamed_images"
output_folder="output"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Find all images in the input folder and process only the first 523
image_list=$(find "$input_folder" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | head -n 523)

# Process each image
for image in $image_list; do
  if [ -f "$image" ]; then
    # Extract the base name of the image
    base_name=$(basename "$image" .${image##*.})
    
    # Run the inference for each image
    CUDA_VISIBLE_DEVICES=0 python inference_on_a_image.py \
      -c groundingdino/config/GroundingDINO_SwinB_cfg.py \
      -p weights/groundingdino_swinb_cogcoor.pth \
      -i "$image" \
      -o "$output_folder/${base_name}_output" \
      -t "pest"

    echo "Finished processing: $image"
  fi
done

echo "All 523 images have been processed. Outputs are saved in $output_folder."

