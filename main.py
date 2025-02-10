import cv2

def main():
    cap = cv2.VideoCapture(0)  
    
    if not cap.isOpened():
        print("Camera not found")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Couldn't grab frame")
            break
        
        cv2.imshow("Camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()