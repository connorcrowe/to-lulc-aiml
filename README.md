# Land Use Land Cover Machine Learning Classification
The objective of this project is to produce a detailed, accurate (>0.85 in testing) vector map that uses machine learning classification on aerial data.

## 1) Simple Classifier
**Model:** Simple Random Forest
Kept to small scale. Included only 5 blocks squared of downtown Toronto and restricted to only 3 classes (road, building, vegetation).

### Attempt 1 - First Classifier
**Accuracy:** 0.42 (yikes!)
The first classifier did its job of being a first classifier. This proof of concept was helpful to practice processing image data and establish a baseline. 

### Attempt 2 - RF Improved
**Accuracy:** 0.44
This attempt included balancing the distribution of training classes, normalizing the pixel values in the image bands, and tuning the model hyperparameters. 
This saw a slight increase in accuracy as a result of balancing the distribution of classes in the training data set. Performing hyperparameter tuning and normalizing the pixel values of the input did not improve performance. 
The Random Forest approach lacks spatial context and is unlikely to scale well. It is likely that further investment in this approach will only bring diminished returns.

![](1_Simple_Classifier/result/1_042_Result.png)

## 2) Raster Input CNN
**Model:** Convolutional Neural Network