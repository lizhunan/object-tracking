import cv2
import argparse
from main import tracking

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tracker', help="Object trackers based on OpenCV.", default='kcf', type=str)
args = parser.parse_args()

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv2.putText(frame, 'Tracker: {}'.format(args.tracker), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, 'FPS: {:.2f}'.format(cap.get(cv2.CAP_PROP_FPS)), (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    tracking(args.tracker, frame)
    cv2.imshow('capture', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 