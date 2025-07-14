import numpy as np
import cv2
import matplotlib.pyplot as plt


def capture_photo():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        cv2.imwrite('image.png', frame)
        break
    
    cap.release()
    cv2.destroyAllWindows()
    return True

def analyse():
    average = [0, 0]

    image = cv2.cvtColor(cv2.imread('image.png'),
                        cv2.COLOR_BGR2RGB)

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_data = cascade.detectMultiScale(image,
                                        scaleFactor=1.1,
                                        minNeighbors=5)
    print(face_data)
    if len(face_data) > 0:
        x, y, width, height = face_data[0]
        average[0] = x + width / 2
        average[1] = y + height / 2  
        average = [int(coord) for coord in average]
        return average
    else:
        quit()

 
def main():
    print(analyse())



if __name__ == "__main__":
    main()