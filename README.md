# 🛩️ Land Use Land Cover Classification of Aerial Imagery with Machine Learning
**Explore the full model:** [U-Net CNN in Jupyter Notebook](https://github.com/connorcrowe/to-lulc-aiml/blob/main/3_Final/3_Full_Model.ipynb)

![](/results/banner.jpg)

**Objective:** *Predict land use classifications in aerial imagery, focusing on specific spatial relationships, such as identifying roadway networks and mapping vegetation versus pavement. This enables potential applications in transportation analysis, impervious surface mapping, etc.*

## Project Overview
This project explores using machine learning to automate Land Use Land Cover (LULC) classification from high-resolution aerial imagery. Automated LULC mapping is a critical tool for urban planning, climate analysis, and environmental monitoring, providing consistent and scalable methods for understanding how land is being used in urban environments.

Urban planners and environmental researchers need accurate, automated maps to track how cities evolve. Traditional mapping methods are slow and labor-intensive. This project explores how machine learning can automate land use classification from aerial imagery, improving scalability and consistency.

An iterative approach was taken, gradually improving the quality of the training data, data augmentation, model, and prediction. 

The training data was labelled manually, with more data being annotated and added to the training set by the third model. This approach allowed for familiarity with the annotation process, but has drawbacks (human error, less data since it is time-consuming).

## Tools & Tech & Skills
- QGIS, Digitization, Aerial Imagery via WMS, Geospatial Data Manipulation
- Convolutional Neural Networks (CNNs), U-Net Architectures, Python, Data Augmentation, TensorFlow 
- *Some imagery (input aerial as .tif, several intermediate results) excluded for size concerns*

## Experimental Journey
### **Baseline Model: Random Forest Classifier**
**Goal:** Establish very simply baseline with traditional method, and ensure data formatting is correct

The first attempt used a Random Forest Classifier. To train it, polygons for each class were manually labelled, and then the aerial image was masked on to it. This approach requires little space, but does not help the model understand any spatial relationships. 
| | | 
|-|-| 
| **Model** | Random Forest | 
| **Validation Accuracy** | ~0.4 |
| **Observations** | Detailed lines and corners predicted well. Vegetation predicted fairly well. Struggled with spatial relationships. Thought many building rooves were roads. |

| Input Aerial | Predicted | 
|-|-|
| ![](/results/input_1.jpg) | ![](results/1_random_forest.jpg)|
| **Resolution:** 2560 x 2347 px | **Light Green:** Vegetation, **Orange:** Building, **Dark Green:** Road |

### **Simple CNN**
**Goal:** Improve accuracy with convolutional network. Use labelled rasters for training input. Apply image augmentation in training.

This model trained on 128x128 patches of a 512x512 aerial image that had been manually digitized. These labelled rasters should improve the ability of the model to see spatial relationships. 

The aerial image was predicted in overlapping patches, with the overlapping areas blended by average value. This leads to fewer sharp corners compared to the Random Forest model.
| | |
|-|-|
| **Model** | Simple CNN | 
| **Validation Accuracy** | ~0.5 |
| **Observations** | Failed to understand spatial relationship of roads. Failed to identify vegetation. Struggles to predict areas under building shadows. Blended approach reduced sharpness of predicted results. | 

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
| **Observations** | Identifiable roadway pattern, even in some shadowed areas. Vegetation predicted accurately. Pavement footpaths predicted accurately. Sidewalk network (as pavement class) in reasonable shape in some places. Building footprints generally shaped correctly, although some shadows do interfere, and buildings are not instance segmented. |

*Result image below*

## Results
### Large Area Predicted by U-Net Model
With tweaks like improving the resolution of the input imagery, and providing more training data in trouble spots like parks and shadowed areas, the model improved. 
- Roads were mapped in an identifiable and nearly connected network, even in some shadowed areas
- Vegetation was classified accurately
- Sidewalk network partially identified
- Pathway network in parks reasonably identified
- Shadows and building edges proved persistent challenges

On a large aerial, the segmentation result produces an identifiable roadway network even in shadows. Parks and vegetation are predicted accurately. This means that further refinement of the model could unlock its use in transportation mapping, impervious surface mapping/change detection, and other important applications.
| Input Aerial |Predicted | 
|-|-|
| ![](/results/input_2.jpg) | ![](/results/3_unet.jpg) |
| **Resolution:** 9216 x 9126 px | **Light Green:** Vegetation, **Orange:** Building, **Dark Green:** Road, **Grey:** Pavement |

The project demonstrates how iterative experimentation and model refinement can improve LULC classification. It highlights the importance in improving both model architecture and input data quality in geospatial machine learning. 

### Future Work & Limitations

With more time and resources, this could be experimented with further:
- Improve model architecture
    - ✔️ Add dropout layers to prevent overfitting
    - ✔️ Increase filter layers to better extract features
    - ✔️ Increase kernel size in deep layers

- Improve data & training
    - ✔️ Add water class
    - Try different training image pixel densities

- Predict large area
    - Look into automated tiling
    - Collate predictions (explore web API for result viewing)


While this approach classifies pixels, future iterations could incorporate instance segmentation for automated building footprint extraction, a key problem in urban planning and disaster response. It could also be improved and used on several aerials from different years to analyze the change in other impervious surfaces, a key part of flood response planning. 

## Data Sources
- Aerial Imagery (for training and prediction): [Toronto Aerial Imagery GIS Map Server](https://gis.toronto.ca/arcgis/rest/services/basemap/cot_ortho/MapServer), imagery taken 2019
- Labelled raster for training: self-digitized from aerial imagery