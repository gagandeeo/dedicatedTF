import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils
import tensorflowjs as tfjs
# from IPython.display import Image
 
# importing image
# filename = 'cat.jpg'
 
#displaying images
# Image(filename,width=224,height=224)
# img = image.load_img(filename,target_size=(224,224))


#initializing the model to predict the image details using predefined models.
model = tf.keras.applications.mobilenet_v2.MobileNetV2()
# resizedimg = image.img_to_array(img)
# finalimg = np.expand_dims(resizedimg,axis=0)
# finalimg = tf.keras.applications.mobilenet_v2.preprocess_input(finalimg)
# finalimg.shape
# predictions = model.predict(finalimg)
 
# To predict and decode the image details
# results = imagenet_utils.decode_predictions(predictions)
# print(results)
model.save('mobilenetV2')
# tfjs.converters.save_keras_model(model, "mobilenetv2")