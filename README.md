# Image classification using CoreML and Turi Create

Build a CoreML classification model with following commands.

## Training

- Create a folder for storing training data. The name of the folder will be used as name of the model saved at the end.
- Create multiple folders inside the main folder containing data to be classified. For example, if you are classifying food then here is typical folder hierarchy. \
/food \
/food/bananas \
/food/oranges \
/food/apples \
The sub-folders will be used a lables for classification.

- `python classification.py train <path to training data>`
- Models will be saved in the current folder as *\<top-folder-name\>*.model and *\<top-folder-name\>*.mlmodel. In above example, it will be saved as food.model and food.mlmodel

## Prediction
- `python classification.py predict <path to test data file>`. For example,
`python classification.py predict ./datasets/food/rice/7_92.jpg`
