import cv2
import time
import json 
from ultralytics import YOLO
#----------------
# Load Settings
#----------------
with open('settings.json') as f:
    settings = json.load(f)
PHONE_THRESHOLD = settings['phone_threshold']
HYDRATION_THRESHOLD = settings['hydration_threshold']
AWAY_THRESHOLD = settings['away_threshold']

print("AuraGuard Started.")
print("Privacy Notice: All processing happens locally. No video is stored or uploaded.")

#----------------
# Load YOLO Model
#----------------

model = YOLO('yolov8n.pt')
#----------------
# Webcam
#----------------
cap = cv2.VideoCapture(0)

#----------------
# COCO Class IDs
#----------------

PERSON = 0
BOTTLE =39
CUP = 41
PHONE = 67
# ----------------
# Timers
# ----------------
phone_start_time = None
last_drink_time = time.time()
person_last_seen = time.time()

#----------------
# FPS Tracking
#----------------
prev_time = 0
frame_count = 0
results = None
while True:
    ret,frame = cap.read()
    if not ret:
        break
    # Resize frame for better performance
    frame = cv2.resize(frame,(480,360))
    frame_count += 1
    if frame_count % 2 == 0:
        results = model(frame, classes = [0,39,41,67],conf=0.25, verbose = False)[0]
    
    
    phone_detected = False
    person_detected = False
    drink_detected = False
    person_box = None
    #------------------
    # Process Detections
    #------------------
    if results:
        for box in results.boxes:
            cls_id = int(box.cls[0])
            
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            # draw detection line
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            if cls_id == PERSON:
                person_detected = True
                person_box = (x1,y1,x2,y2)
            if cls_id == PHONE:
                phone_detected = True
            if cls_id in [BOTTLE,CUP]:
                drink_detected = True
                
        
        
    
    current_time = time.time()
    #------------------
    # Update Timers
    #------------------
    if person_detected:
        person_last_seen = current_time
    if drink_detected:
        last_drink_time = current_time
    
    #------------------
    # Default status
    #------------------
    status_text = "Status: Focusing"
    color = (0,255,0)
    
    flash = int(time.time()*2) %2
    #------------------
    #User away Detection
    #------------------
    if current_time - person_last_seen > AWAY_THRESHOLD:
        status_text = "System Paused: User away"
        color = (0,255,255)
    #------------------
    # Phone Distraction Detection
    #------------------
    elif phone_detected:
        if phone_start_time is None:
            phone_start_time = current_time
        if current_time - phone_start_time > PHONE_THRESHOLD:
            status_text = "WARNING: Put your Phone away"
            
            if flash:
                color = (0,0,255)
            else:
                color = (0,0,150)
    elif not phone_detected and phone_start_time:
        if current_time - phone_start_time > 1:
            phone_start_time = None
   
    #------------------
    # Hydration Reminder
    #------------------
    if current_time - last_drink_time > HYDRATION_THRESHOLD:
        status_text = "HEALTH ALERT: DRINK WATER"
        color = (255,0,0)
    #------------------
    # Draw focus Bounding Box
    #------------------
    if person_box and status_text == "Status: Focusing":
        x1,y1,x2,y2 = person_box
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
    #------------------
    # HUD Text
    #------------------
    cv2.putText(frame,status_text,(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,color,3)
    time_since_drink = int(current_time - last_drink_time)
    cv2.putText(frame,f"Time since last drink: {time_since_drink}s",(20,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
    #------------------
    # FPS Counter
    #------------------
    new_time = time.time()
    fps  = 1/(new_time - prev_time) if prev_time != 0 else 0
    prev_time = new_time
    cv2.putText(frame,f"FPS: {int(fps)}",(520,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
    #------------------
    # Show Window
    #------------------
    cv2.imshow("AuraGuard AI",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#----------------------
# Cleanup
#----------------------
cap.release()
cv2.destroyAllWindows()