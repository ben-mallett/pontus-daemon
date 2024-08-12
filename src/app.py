from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2

app = FastAPI()

cap = cv2.VideoCapture(0)

def gen_frames():
    if not cap.isOpened():
        raise RuntimeError("Could not start video capture.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.get("/stream")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

