import os
import cv2
import addon_function as my

#TO CREAT FOLDER IF DELETED

if not os.path.exists("images"):
    os.makedirs("images")
    os.makedirs("images/valid")
    os.makedirs("images/valid/0")
    os.makedirs("images/valid/1")
    os.makedirs("images/valid/2")
    os.makedirs("images/valid/3")
    os.makedirs("images/valid/4")
    os.makedirs("images/valid/5")
    os.makedirs("images/valid/6")
    os.makedirs("images/train")
    os.makedirs("images/train/0")
    os.makedirs("images/train/1")
    os.makedirs("images/train/2")
    os.makedirs("images/train/3")
    os.makedirs("images/train/4")
    os.makedirs("images/train/5")
    os.makedirs("images/train/6")

#PATHS

train_path="images/train"
valid_path='images/valid'


cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    x1 = 330
    y1 = 10
    x2 = 630
    y2 = 310

    #DRAW ROI ON FRAME (300*300)
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    #THRESOLD FUNCTION TAKE 2 IMAGE AS INPUT AND APPLY THRESOLD
    #I NEED INLY ONE IMAGE THIS TIME
    roi,_=my.thresold(roi,roi)
    cv2.imshow('roi',roi)

    #COUNT NUMBER OF IMAGES IN EACH DIRECTORY
    count = {'zero':len(os.listdir(train_path+'/0')),
             'one':len(os.listdir(train_path+'/1')),
             'two':len(os.listdir(train_path+'/2')),
             'three':len(os.listdir(train_path+'/3')),
             'four':len(os.listdir(train_path+'/4')),
             'six':len(os.listdir(train_path+'/6')),
             'five':len(os.listdir(train_path+'/5'))}

    #PRINT DETEAIL OF NO OF IMAGE IN EACH DIRECTORY
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ZERO : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ONE : " + str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "TWO : " + str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THREE : " + str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FOUR : " + str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FIVE : " + str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "SIX : " + str(count['six']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.imshow('frame',frame)

    #EXICUTE IF ANT KEY IS PRESSED
    #IT WILL ALSO FLIP THE IMAGE TO CREATE ANOTHER IMAGE
    event=cv2.waitKey(1)
    if event & 0xFF == 27:
        break
    elif event & 0xFF == ord('0'):
        cv2.imwrite(train_path+'/0/'+str(count['zero'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/0/'+str(count['zero']+1)+'.jpg', roi)
    elif event & 0xFF == ord('1'):
        cv2.imwrite(train_path+'/1/'+str(count['one'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/1/'+str(count['one']+1)+'.jpg', roi)
    elif event & 0xFF == ord('2'):
        cv2.imwrite(train_path+'/2/'+str(count['two'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/2/'+str(count['two']+1)+'.jpg', roi)
    elif event & 0xFF == ord('3'):
        cv2.imwrite(train_path+'/3/'+str(count['three'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/3/'+str(count['three']+1)+'.jpg', roi)
    elif event & 0xFF == ord('4'):
        cv2.imwrite(train_path+'/4/'+str(count['four'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/4/'+str(count['four']+1)+'.jpg', roi)
    elif event & 0xFF == ord('5'):
        cv2.imwrite(train_path+'/5/'+str(count['five'])+'.jpg', roi)
        roi=cv2.flip(roi,1)
        cv2.imwrite(train_path+'/5/'+str(count['five']+1)+'.jpg', roi)
    elif event & 0xFF == ord('6'):
        cv2.imwrite(train_path+'/6/'+str(count['six'])+'.jpg', roi)



cap.release()
cv2.destroyAllWindows()
