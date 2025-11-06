import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import glob
import os

model = MobileNetV2(weights='imagenet', input_shape=(224,224,3))

converter = tf.lite.TFLiteConverter.from_keras_model(model)

converter.optimizations = [tf.lite.Optimize.DEFAULT]

def representative_dataset():
    image_files = glob.glob("images/*.jpg")  # adjust path & extension if needed
    if not image_files:
        raise ValueError("No images")
    for img_path in image_files:
        img = Image.open(img_path).resize((224,224))
        img = np.array(img, dtype=np.float32)
        img = preprocess_input(img)  # scale inputs like MobileNetV2 expects
        img = np.expand_dims(img, axis=0)
        yield [img]

converter.representative_dataset = representative_dataset

converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model = converter.convert()
os.makedirs("tflite_models", exist_ok=True)
tflite_path = os.path.join("tflite_models", "mobilenetv2_int8.tflite")
with open(tflite_path, "wb") as f:
    f.write(tflite_model)

print(f"Fully INT8 MobileNetV2 saved as {tflite_path}")
