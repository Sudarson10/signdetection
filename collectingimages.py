import os

import cv2


DATA_DIR = r"C:\Users\sudar\OneDrive\Desktop\miniprojects\signdetection\images"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes =3
dataset_size =200

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        frame1 = cv2.flip(frame, 1)
        cv2.imshow('frame', frame1)
        if cv2.waitKey(1) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        frame1=cv2.flip(frame,2)
        cv2.imshow('frame', frame1)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame1)

        counter += 1

cap.release()
cv2.destroyAllWindows()