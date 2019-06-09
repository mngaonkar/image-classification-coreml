import turicreate as tc
import sys
import os

"""
Predict the classification
"""
def model_predict(model, image_path):
    image = tc.Image(image_path)
    image_sframe = tc.SFrame({'path': [image_path], 'image': [image], 'type':['']})
    print "Image SFrame : \n", image_sframe

    prediction = model.predict(image_sframe)
    print "Prediction : \n", prediction


"""
Create model
"""
def create_classifier(sframe_name, classifier_model_name, target_attribute):
    training_percent = 0.8

    # create classifier
    data_buffer = tc.SFrame(sframe_name)
    training_data, testing_data = data_buffer.random_split(training_percent)
    model = tc.image_classifier.create(training_data, target=target_attribute, model=classifier_model_name)

    return model

"""
Save model in native and CoreML format
"""
def save_model(model, name):
    model.save(name + ".model")
    model.export_coreml(name + ".mlmodel")


"""
Lable images and create sframe, folder name is used as data label
"""
def load_dataset(folder_path):
    sframe_name = "datasets.sframe"  

    # annotate images
    images = tc.image_analysis.load_images(folder_path, with_path = True)
    # images["type"] = images["path"].apply(lambda path: "rice" if "rice" in path else "soup")
    images["type"] = images["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))
    images.save(sframe_name)

    return sframe_name

def explore_dataset(dataset):
    dataset.explore()

def main():
    arguments = sys.argv[1:]
    if len(arguments) < 1:
        print "Invalid arguments"
        print "Usage : python classifier.py [train | predict]"
        exit(1)

    model_name = "RiceOrSoup"

    if sys.argv[1] == "train":
        if len(arguments) < 2:
            print "Usage : python classifier.py train <dataset path>"
            exit(1)

        dataset_path = arguments[1]

        print "Loading dataset..."
        sframe = load_dataset(dataset_path)
        print "Dataset loaded."

        print "Creating model..."
        model = create_classifier(sframe, "squeezenet_v1.1", "type")
        print "Model created."

        print "Saving model..."
        save_model(model, model_name)
        print "Model %s saved."%(model_name)
    elif sys.argv[1] == "predict":
        if len(arguments) < 2:
            print "Usage : python classifier.py predict <image path>"
            exit(1)
        
        image_path = arguments[1]

        loaded_model = tc.load_model(model_name + ".model")
        prediction = model_predict(loaded_model, image_path)
    else:
        print "Invalid arguments"
        print "Usage : python classifier.py [train | predict]"

if __name__ == "__main__":
    main()
