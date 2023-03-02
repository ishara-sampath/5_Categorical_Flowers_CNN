import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained CNN model
model = load_model('flower_recognition_model.h5')

# Define the labels for the flower categories
labels = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale and resize it to 128x128
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.resize(gray, (32, 32))

    # Reshape the image to match the input shape of the CNN model
    img = gray.reshape(-1, 32, 32, 3)

    # Normalize the image pixel values to be between 0 and 1
    img = img / 255.0

    # Use the CNN model to predict the label of the flower in the image
    pred = model.predict(img)[0]
    flower = labels[np.argmax(pred)]

    # Display the label on the screen
    cv2.putText(frame, flower, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Flower Classification', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
