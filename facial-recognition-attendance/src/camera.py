class Camera:
    def __init__(self):
        self.video_capture = None

    def start_camera(self):
        import cv2
        self.video_capture = cv2.VideoCapture(0)

    def stop_camera(self):
        if self.video_capture is not None:
            self.video_capture.release()
            self.video_capture = None

    def capture_image(self):
        if self.video_capture is not None:
            ret, frame = self.video_capture.read()
            if ret:
                return frame
        return None