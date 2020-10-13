import cv2
import numpy as np
import pandas as pd

text="Please raise your hand..."

# TO CAPTURE FRAME AND FLIP IT ALSO RETURN FRAME SIZE
def capture_frame(cap):
    # CAPTURE FRAME
    _, frame = cap.read()
    # FLIP FRAME
    frame = cv2.flip(frame, 1)

    h,w, _ = frame.shape
    # INCRESE FRAME SIZE
    frame=cv2.resize(frame,(832,624))
    return frame,h,w

# TO DRAW BOTH ROI'S AND EXTRACT IT ALSO
def draw_roi(frame):
    # COORDINATE OF 1st ROI [(x1,y1),(x2,y2)]
    x1 = 15
    y1 = 15
    x2 = 315
    y2 = 315

    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)

    # EXTRECT 1st RIO
    roi1 = frame[y1:y2, x1:x2]

    # RESIZE IT TO (64,64)
    roi1 = cv2.resize(roi1, (64, 64))

    # COORDINATE OF 2st ROI [(x1,y1),(x2,y2)]
    x1=517
    x2=817

    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (0, 255, 0), 1)
    roi2 = frame[y1:y2, x1:x2]
    roi2 = cv2.resize(roi2, (64, 64))
    return frame,roi1,roi2


#TO CREATE SMALL CIRCLE ON TOP-RIGHT CORNER
def timer(img,i):
    radius = 10
    axes = (radius, radius)
    angle = 0;

    h,w,_=img.shape

    center = (w-20, 20)
    color = (255,0,0)
    cv2.ellipse(img, center, axes, angle, 0, i, color, 2)
    return img


# PREPARE BINARY IMAGE
def thresold(roi1,roi2):
    # READ HSV VALUES FROM FILE
    hsv_values = np.loadtxt('data/hsv_values.txt', dtype=int)

    # REMOVING BACKGROUNG FROM BOTH ROI'S
    roi1=cv2.cvtColor(roi1,cv2.COLOR_BGR2HSV)
    roi1=cv2.inRange(roi1,hsv_values[0],hsv_values[1])
    roi1=cv2.bitwise_not(roi1)
    
    roi2=cv2.cvtColor(roi2,cv2.COLOR_BGR2HSV)
    roi2=cv2.inRange(roi2,hsv_values[0],hsv_values[1])
    roi2=cv2.bitwise_not(roi2)
    return roi1,roi2


def predictt(img1,img2):
    from keras.models import model_from_json
    import tensorflow as tf
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    #PRINT CALL TO CHECK FUNCTION IS CALL
    print("CALL")
    #READ MODEL ARCHITECTURE AND WEIGHT
    json_file = open("model/model_architecture.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    loaded_model.load_weights("model/weight_final.h5")

    #SAVE INPUT IMAGE TO DISK FOR IMAGE PROCESSING
    cv2.imwrite('images/temp/0/img1.jpg', img1)
    cv2.imwrite('images/temp/0/img2.jpg', img2)
    #IMAGE PROCESSING
    classes = ['0', '1', '2', '3', '4', '5','6']
    test = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
        .flow_from_directory(directory='images/temp/', target_size=(64, 64), classes=classes, batch_size=2,shuffle=False)
    pred=loaded_model.predict(test)
    x=pred>0.7
    a=np.array([-1,-1])
    for i in range(2):
        for j in range(6):
            if(x[i][j]==True):
                a[i]=j
                break

    if(a[0]==-1 and a[1]==-1):
        return 11
    elif(a[0]==-1):
        return a[1]
    elif(a[1]==-1):
        return a[0]
    else:
        return a[0]+a[1]


#TO READ DATABASE
def data(pin):
    p=int(pin)
    df = pd.read_csv('data/pin_code_list.csv')
    h = df[df.pincode == p].reset_index()
    p = h[h.index == 0]
    try:
        d_name = p['Districtname'][0]
        s_name = p['statename'][0]
        return 1,d_name,s_name
    except:
        return 0,"no","no"


#TO SHOW RESULT
def show_result(cap,pin):
    r,d_name,s_name=data(pin)
    # r,d_name,s_name=data("274001")
    #TO CLOSE ALL OTHER WINDOWS
    cv2.destroyAllWindows()

    while cap.isOpened():
        _,frame=cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (832, 624))

        w, h, _ = frame.shape

        cv2.putText(frame, text, (int(w * 0.1), int(h * 0.1)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
        cv2.putText(frame, pin, (int(w * 0.1), int(h * 0.16)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255))
        if r==1:
            cv2.putText(frame, "Right Pincode", (int(w * 0.1), int(h * 0.22)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
            cv2.putText(frame, "District name : "+d_name, (int(w * 0.1), int(h * 0.28)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
            cv2.putText(frame, "State name : "+s_name, (int(w * 0.1), int(h * 0.34)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
        else:
            cv2.putText(frame, "Wrong Pincode.", (int(w * 0.1), int(h * 0.22)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0,255))
            cv2.putText(frame, "try again...", (int(w * 0.1), int(h * 0.28)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0,255))

        cv2.imshow("video",frame)
        if cv2.waitKey(1)==27:
            break
