import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.applications.resnet50 import preprocess_input

# Load pre-trained ResNet50 model without top layer
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the layers
for layer in base_model.layers:
    layer.trainable = False

# Define the image captioning model
image_input = Input(shape=(224, 224, 3))
features = base_model(image_input)
flatten = tf.keras.layers.Flatten()(features)
dense = Dense(256, activation='relu')(flatten)

# Define the sequence model
caption_input = Input(shape=(None,))
embedding = Embedding(input_dim=vocab_size, output_dim=100)(caption_input)
lstm = LSTM(256)(embedding)

# Combine image and sequence models
merged = tf.keras.layers.concatenate([dense, lstm])
output = Dense(vocab_size, activation='softmax')(merged)

model = Model(inputs=[image_input, caption_input], outputs=output)
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Display the model architecture
model.summary()

# Data preparation (load images, captions, tokenize text, etc.)

# Train the model
model.fit([image_data, caption_sequences], next_word_one_hot, epochs=10, batch_size=32, validation_split=0.2)

# Inference
def generate_caption(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    features = base_model.predict(img)
    features = np.reshape(features, (1, -1))

    start_token = tokenizer.word_index['startseq']
    end_token = tokenizer.word_index['endseq']
    current_token = start_token

    caption = []

    while current_token != end_token:
        caption.append(tokenizer.index_word[current_token])
        sequence = pad_sequences([caption], maxlen=max_length)
        prediction = model.predict([features, sequence], verbose=0)
        current_token = np.argmax(prediction)

    return ' '.join(caption[1:-1])  # Exclude startseq and endseq tokens

# Example usage
image_path = 'path/to/your/image.jpg'
predicted_caption = generate_caption(image_path)
print("Predicted Caption:", predicted_caption)