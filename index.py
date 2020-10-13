import cv2
import addon_function as my

angle = 0
pin = ""
text = "Please raise your hand..."

cap = cv2.VideoCapture(0)

while cap.isOpened():

    # TO CAPTURE FRAME AND FLIP IT
    # h IS HEIGHT OF FRAME
    # w IS WITHT OF FRAME
    frame,h,w = my.capture_frame(cap)

    # TO DRAW TWO REGION OF INTEREST (ROI) ON FRAME
    frame,roi1,roi2=my.draw_roi(frame)

    # TO CREATE SMALL CIRCLE WHICH IS AT TOP-RIGHT CORNER
    # WHEN CIRCLE IS COMPLETED THEN ONLY IT CAPTURE THE PRESENT FRAME AND MAKE PREDICTION
    img_timer = my.timer(frame, angle)
    angle = (angle + 8) % 360

    # TO PREPARE BOTH ROI'S TO RUN PREDICTION ON THEM
    thres1,thres2 = my.thresold(roi1,roi2)

    # ONLY RUN PREDICTION ON FEW FRAMES
    if angle >= 352:
        # predictt IMPLEMENT CNN TO COUNT NUMBER OF FINGURE
        detected_number = my.predictt(thres1,thres2)

        # IF DETECTED_NUMBER IS SINGLE DIGIT THEN ADD IT TO PIN
        if detected_number <= 9:
            pin += str(detected_number)
        # ELSE SHOW AN ERROR MESSAGE
        elif detected_number == 10:
            img = cv2.imread('data/wrong_number.png',1)
            cv2.imshow('wrong_number', img)
            cv2.waitKey(1200)
            cv2.destroyWindow('wrong_number')
        else:
            img = cv2.imread('data/error_message.png',1)
            cv2.imshow('error_message', img)
            cv2.waitKey(1200)
            cv2.destroyWindow('error_message')

        # CHECK PIN HAVE 6 DIGIT OR NOT IF TRUE THEN PRINT RESULT
        if len(pin) == 6:

            # TO SHOW RESULT
            my.show_result(cap, pin)

            #FOR NEW INPUT
            pin = ""

    #PRINT PIN AND INSTRUCTION
    cv2.putText(frame, text, (int(w * 0.1), int(h * 0.85)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255))
    cv2.putText(frame, pin, (int(w * 0.1), int(h * 0.91)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255))

    #SHOW FRAMES AND ALL ROI'S
    cv2.imshow("video", frame)
    cv2.imshow("thres1", thres1)
    cv2.imshow("thres2", thres2)
    cv2.imshow("roi1", roi1)
    cv2.imshow("roi2", roi2)

    # TO EXIT PROGRAM
    if cv2.waitKey(1) == 27:
        img=cv2.imread('data/exit_message.png',1)
        cv2.imshow('exit_message',img)
        cv2.waitKey(2000)
        break

cap.release()
cv2.destroyAllWindows()
