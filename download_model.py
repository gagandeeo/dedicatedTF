import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils
import tensorflowjs as tfjs

 
def test_locally(filename):
    img = image.load_img(filename,target_size=(224,224))

    resizedimg = image.img_to_array(img)
    finalimg = np.expand_dims(resizedimg,axis=0)
    finalimg = tf.keras.applications.mobilenet_v2.preprocess_input(finalimg)
    finalimg.shape
    predictions = model.predict(finalimg)
    # To predict and decode the image details
    results = imagenet_utils.decode_predictions(predictions)
    print(results) 

def download_model():
    model = tf.keras.applications.mobilenet_v2.MobileNetV2()
    model.save('mobilenetV2')

# Download and save model
# download_model()

# Convert keras model to tensorflowjs format for serving with js (if you want to implement the model in client side)
# tfjs.converters.save_keras_model(model, "mobilenetv2")