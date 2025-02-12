import cv2
import mediapipe as mp
import numpy as np
import pyvirtualcam
import argparse

def main():
    parser = argparse.ArgumentParser(description="Virtual camera with background replacement.")
    parser.add_argument("-b", "--background", type=str, help="Path to background image", default=None)
    args = parser.parse_args()
    
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Camera not found")
        return
    
    # Load background image if provided
    background = None
    if args.background:
        background = cv2.imread(args.background)
        if background is None:
            print("Error: Could not load background image.")
            return
        background = cv2.resize(background, (640, 480))
    
    # MediaPipe
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)  

    try:
        with pyvirtualcam.Camera(width=640, height=480, fps=60) as cam:
            print(f"Virtual camera started: {cam.device}")

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Couldn't grab frame")
                    break

                frame = cv2.resize(frame, (640, 480))  
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = segment.process(frame_rgb)
                
                mask = result.segmentation_mask
                binary_mask = (mask > 0.5).astype(np.uint8)

                if background is None:
                    blurred_background = cv2.GaussianBlur(frame, (55, 55), 0)
                    bg = blurred_background
                else:
                    bg = background
                
                output = frame * binary_mask[:, :, None] + bg * (1 - binary_mask[:, :, None])
                
                cam.send(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
                cam.sleep_until_next_frame()

                cv2.imshow("Camera", output)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except RuntimeError as e:
        if "OBS Virtual Camera device not found" in str(e):
            print("\nERROR: OBS Virtual Camera not found!")
            print("Please install OBS Studio and enable the Virtual Camera feature.")
            print("Download OBS Studio here: https://obsproject.com/")
        else:
            print(f"Error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
