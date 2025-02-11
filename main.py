import cv2
import mediapipe as mp
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Camera not found")
        return
    
    # MediaPipe
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)  

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Couldn't grab frame")
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        result = segment.process(frame_rgb)
        
        mask = result.segmentation_mask
        
        threshold = 0.5
        binary_mask = (mask > threshold).astype(np.uint8)

        blurred_background = cv2.GaussianBlur(frame, (55, 55), 0)

        output = frame * binary_mask[:, :, None] + blurred_background * (1 - binary_mask[:, :, None])
        
        cv2.imshow("Camera", output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()