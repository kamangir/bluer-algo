import cv2 as cv


def select_roi(frame):
    roi_box = [0, 0, 0, 0]
    dragging = [False]

    def mouse_callback(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            roi_box[0], roi_box[1] = x, y
            dragging[0] = True
        elif event == cv.EVENT_MOUSEMOVE and dragging[0]:
            roi_box[2], roi_box[3] = x - roi_box[0], y - roi_box[1]
        elif event == cv.EVENT_LBUTTONUP:
            roi_box[2], roi_box[3] = x - roi_box[0], y - roi_box[1]
            dragging[0] = False

    cv.namedWindow("Select ROI")
    cv.setMouseCallback("Select ROI", mouse_callback)

    while True:
        temp_frame = frame.copy()
        if roi_box[2] and roi_box[3]:
            x, y, w, h = roi_box
            cv.rectangle(temp_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow("Select ROI", temp_frame)
        key = cv.waitKey(1) & 0xFF
        if key in [13, 32]:  # ENTER or SPACE to confirm
            break
        if key == 27:  # ESC to cancel
            cv.destroyWindow("Select ROI")
            return None

    cv.destroyWindow("Select ROI")
    return tuple(roi_box)
