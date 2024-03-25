import cv2

OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT.create(),
	"kcf": cv2.TrackerKCF.create(),
	"boosting": cv2.legacy.TrackerBoosting.create(),
	"mil": cv2.TrackerMIL.create(),
	"tld": cv2.legacy.TrackerTLD.create(),
	"medianflow": cv2.legacy.TrackerMedianFlow.create(),
	"mosse": cv2.legacy.TrackerMOSSE.create()
}

bounding_box = None

def tracking(tracker, frame):
    global bounding_box
    tracker = OBJECT_TRACKERS[tracker]
    if cv2.waitKey(1) & 0xFF == ord('s'):
        bounding_box = cv2.selectROI('capture', frame, fromCenter=False, showCrosshair=True)
        tracker.init(frame, bounding_box)
    if bounding_box is not None:
        (success, box) = tracker.update(frame)
        cv2.putText(frame, 'Success: {}'.format('Yes' if success else 'No'), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        