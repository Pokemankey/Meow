import time
import requests
import cv2
import base64

def capture_and_send():
    # Open the webcam outside the loop
    cap = cv2.VideoCapture(1)

    try:
        while True:
            print("running")
            # Capture an image from the webcam
            ret, frame = cap.read()

            # Encode the image as base64
            _, img_encoded = cv2.imencode('.jpg', frame)
            img_base64 = base64.b64encode(img_encoded.tobytes())

            # Send the image to the server on the laptop
            url = 'http://192.168.1.121:5000/upload'
            headers = {'Content-Type': 'application/json'}
            data = {'image': img_base64.decode('utf-8')}
            response = requests.post(url, json=data, headers=headers)

            # Wait for 5 seconds before capturing the next image
            time.sleep(5)

    except KeyboardInterrupt:
        print("Capture stopped by user.")
        # Release the webcam when the script is interrupted
        cap.release()

# Run the capture_and_send function directly
capture_and_send()