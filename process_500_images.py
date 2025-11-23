#!/bin/bash

# Define the input and output folders
input_folder="stem_borer"
output_folder="stem_borer_out"

# Create the output folder if it doesn't exist
mkdir -p "$renamed_images"

# Randomly select 500 images from the input folder
selected_images=$(find "$input_folder" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | shuf -n 500)

# Process each selected image
for image in $selected_images; do
  if [ -f "$image" ]; then
    # Run the inference for each image
    CUDA_VISIBLE_DEVICES=0 python inference_on_a_image.py \
      -c groundingdino/config/GroundingDINO_SwinB_cfg.py \
      -p weights/groundingdino_swinb_cogcoor.pth \
      -i "$image" \
      -o "$output_folder/$(basename "$image" .${image##*.})_output" \
      -t "pest"
  fi
done

echo "Inference completed for 500 random images from $input_folder. Outputs saved to $output_folder."
#!/bin/bash

# Define the input and output folders
input_folder="stem_borer"
output_folder="stem_borer_out"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Randomly select 500 images from the input folder
selected_images=$(find "$input_folder" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | shuf -n 500)

# Process each selected image
for image in $selected_images; do
  if [ -f "$image" ]; then
    # Run the inference for each image
    CUDA_VISIBLE_DEVICES=0 python inference_on_a_image.py \
      -c groundingdino/config/GroundingDINO_SwinB_cfg.py \
      -p weights/groundingdino_swinb_cogcoor.pth \
      -i "$image" \
      -o "$output_folder/$(basename "$image" .${image##*.})_output" \
      -t "pest"
  fi
done

echo "Inference completed for 500 random images from $input_folder. Outputs saved to $output_folder."
