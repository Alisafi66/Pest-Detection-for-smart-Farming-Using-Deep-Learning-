# 🌾 Zero-Shot Pest Detection for Smart Farming
### Integrating Grounding DINO for Unseen Pest Identification

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1-EE4C2C)](https://pytorch.org/)
[![Task](https://img.shields.io/badge/Task-Zero--Shot_Detection-green)](https://github.com/IDEA-Research/GroundingDINO)
[![Sponsor](https://img.shields.io/badge/Sponsor-MDEC-purple)]()

## 📖 Project Overview
This repository houses the **Zero-Shot Object Detection** module of my Final Year Project: *"Pest Detection for Smart Farming using Deep Learning."*

The primary objective was to develop an AI model capable of detecting agricultural pests that it had never seen before during training. To achieve this, we utilized **Grounding DINO**, an open-set object detector that uses text prompts (e.g., "insect", "pest") to identify objects.

**Key Achievements:**
* **Zero-Shot Capability:** Successfully detected unseen pest species without bounding box training.
* **Large-Scale Data Curation:** Collected and curated a dataset of **>100,000 images** due to the scarcity of public agricultural datasets.
* **Stochastic Evaluation:** Designed a randomized testing pipeline to validate performance efficiently.

## 📂 The Challenge: Data Scarcity
One of the biggest hurdles in Smart Farming robotics is the lack of diverse, labeled datasets for specific regional pests.
* **Problem:** Existing datasets were insufficient for real-world deployment in Malaysian farms.
* **Solution:** I curated a massive dataset comprising over **100,000 images**, split between:
    1.  **Pest Images:** Various species of insects harmful to crops.
    2.  **Non-Pest Images:** Background foliage, harmless insects, and humans.

## ⚙️ Methodology & Testing Pipeline
To efficiently evaluate the model's performance on such a massive dataset, I engineered a stochastic (randomized) testing protocol.

### 1. The Model: Grounding DINO
We utilized Grounding DINO with a Swin-Transformer backbone. The model takes an image and a text prompt (e.g., *"a pest on a leaf"*) and outputs bounding boxes for objects matching that description.

### 2. Randomized Sampling Algorithm
Running inference on 100,000+ images is computationally expensive for rapid prototyping. I developed a custom script to:
1.  Scan the full 100k dataset.
2.  **Randomly Select** a subset of **500 images** per evaluation cycle.
3.  Run inference on this subset to generate performance metrics.

This approach ensured our accuracy metrics were statistically significant without requiring days of compute time for every test run.

## 📊 Results
| Metric | Performance | Notes |
| :--- | :--- | :--- |
| **Accuracy** | **74%** | On randomly sampled unseen test sets |
| **Approach** | Zero-Shot | No fine-tuning required for new pest types |
| **Detection** | Human vs. Pest | Capable of distinguishing humans (safety) from pests |

## 🛠️ Repository Structure
```text
.
├── scripts/
│   ├── batch_inference.sh   # Main script to run the randomized 500-image test
│   └── process_images.sh    # Utilities for image preprocessing
├── src/
│   └── inference.py         # Core logic wrapping Grounding DINO
├── notebooks/
│   └── demo.ipynb           # Jupyter notebook for visual demonstrations
├── Dockerfile               # Containerized environment for reproducibility
└── requirements.txt         # Python dependencies
