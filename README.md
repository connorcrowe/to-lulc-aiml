# to-lulc-aiml
The objective of this project is to produce a detailed, accurate (>0.85 in testing) vector map that uses machine learning classification on aerial data.

## 1) Simple Classifier
**Model:** Simple Random Forest
Kept to small scale. Included only a few blocks of downtown Toronto and restricted to only 3 classes (road, building, vegetation).

### Attempt 1 - First Classifier
**Accuracy:** 0.42 (yikes!)
**Improvements to make**:
- Balance classes
- Increase amount of training data
- Tune random forest parameters

![](1_Simple_Classifier/result/1_042_Result.png)

### Attempt 2 - RF Improved