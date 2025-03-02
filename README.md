# 🛩️ Land Use Land Cover Classification of Aerial Imagery with Machine Learning
**Explore the full model:** [U-Net CNN in Jupyter Notebook](https://github.com/connorcrowe/to-lulc-aiml/blob/main/3_Final/3_Full_Model.ipynb)
***Objective:** Predict land use classification in aerial imagery with high accuracy, especially in specific spatial relationships, such as identifying a connected roadway network and accurately mapping vegetation vs pavement to allow for potential future use in transportation analysis, impervious surface mapping, etc.*
IMAGE

## Project Overview
This project explores the use of machine learning to automate Land Use Land Cover (LULC) classification from high-resolution aerial imagery. Automated LULC mapping is a critical tool for urban planning, climate analysis, and environmental monitoring, providing consistent and scalable methods for understanding how land is being used in urban environments.

By iterating through multiple model architectures and analyzing the results, this project demonstrates how machine learning techniques can improve the accuracy of LULC classification through experimentation.

## Tools & Tech & Skills
- QGIS, Digitization, Aerial Imagery via WMS
- CNNs, U-Net, Python, Data Augmentation, Tensorflow, 

## Experimental Journey
### **Baseline Model: Random Forest Classifier**
**Goal:** Establish very simply baseline with traditional method, and ensure data formatting is correct

The first attempt used a Random Forest Classifier trained on disparate, pure features without spatial context (a flawed approach).
| | | 
|-|-| 
| **Model** | Random Forest | 
| **Validation Accuracy** | ~0.4 |
| **Observations** | Detailed lines and corners predicted well. Vegetation predicted fairly well. Struggled with spatial relationships. Thought many building rooves were roads. |

| Input Aerial | Predicted | 
|-|-|
| ![](/results/input_1.jpg) | ![](results/1_random_forest.jpg)|
| **Resolution:** 2560 x 2347 px | **Light Green:** Vegetation, **Orange:** Building, **Dark Green:** Road |

### **Basic CNN**
**Goal:** Improve accuracy with convolutional network. Use labelled rasters for training input. Apply image augmentation in training.

This model trained on 128x128 patches of a 512x512 aerial image that hand been manually digitized.
| | |
|-|-|
| **Model** | CNN | 
| **Validation Accuracy** | ~0.5 |
| **Observations** | Better at telling roads from buildings. Failed to understand spatial relationship of roads. Failed to identify vegetation. Struggles to predict areas under building shadows. | 

| Input Aerial | Predicted | 
|-|-|
| ![](/results/input_1.jpg) | ![](/results/2_simple_cnn.jpg) |
| **Resolution:** 2560 x 2347 px | **Light Green:** Vegetation, **Orange:** Building, **Dark Green:** Road, **Grey:** Pavement |

### **U-Net Architecture**
**Goal:** Improve spatial relationships of roads relative to each other. Improve classification of vegetation. Predict on more input imagery. Train on, and predict higher resolution imagery (improve memory management). 

Improvements:
- Robust data augmentation
- More, higher resolution training data
- More convolutional layers
- Add 'skip connections' 
- Add learning rate scheduling

| | |
|-|-|
| **Model** | U-Net CNN |
| **Validation Accuracy** | ~0.7 | 
| **Dice Coefficient (Val)** | ~0.6 |
| **Observations** | Best performance overall. Identifiable roadway pattern, even in some shadowed areas. Vegetation predicted accurately. Most pavement footpaths predicted accurately. Sidewalk network (as pavement class) in reasonable shape in some places. Building footprints generally shaped correctly, although some shadows do interfere, and buildings are not instance segmented. 

## Results
| Input Aerial |Predicted | 
|-|-|
| ![](/results/input_2.jpg) | ![](/results/3_unet.jpg) |
| **Resolution:** 9216 x 9126 px | **Light Green:** Vegetation, **Orange:** Building, **Dark Green:** Road, **Grey:** Pavement |

**Key Observations**

## Data Sources
- Aerial Imagery (for training and prediction): [Toronto Aerial Imagery GIS Map Server](https://gis.toronto.ca/arcgis/rest/services/basemap/cot_ortho/MapServer), imagery taken 2019
- Labelled raster for training: self-digitized from aerial imagery