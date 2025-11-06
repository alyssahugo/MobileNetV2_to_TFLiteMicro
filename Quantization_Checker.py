import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="tflite_models/mobilenetv2_int8.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Input details:")
for inp in input_details:
    print(inp)

print("\nOutput details:")
for out in output_details:
    print(out)

# Check if the model is INT8
input_type = input_details[0]['dtype']
output_type = output_details[0]['dtype']

print(f"\nInput dtype: {input_type}")
print(f"Output dtype: {output_type}")

if input_type == 'uint8' and output_type == 'uint8':
    print("The model is fully INT8 quantized.")
else:
    print("The model is not fully INT8 quantized.")


# xxd -i mobilenetv2_int8.tflite > mobilenetv2_model_data.h

# /home/alyssa/tflite-micro/tensorflow/lite/micro/examples/network_tester
