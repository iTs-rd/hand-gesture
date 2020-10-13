
import tensorflow as tf
from keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Convolution2D,MaxPooling2D,BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#CONFIGER GPU TO BE USED BY PROGRAM

try:
    pd=tf.config.experimental.list_physical_devices('GPU')
    print("No. of GPU ",len(pd))
    tf.config.experimental.set_memory_growth(pd[0],True)
except:
    pass

# MODEL NUMBER
i=5

# COPYED FROM https://analyticsindiamag.com/how-to-implement-cnn-model-to-count-fingers-and-distinguish-between-left-and-right-hand/
# AND MAKE SOME CHANGES
model=Sequential()
model.add(BatchNormalization(input_shape = (64,64,3)))
model.add(Convolution2D(32, (3,3), activation ='relu', input_shape = (64,64, 3)))
model.add(MaxPooling2D(pool_size=2))
model.add(Convolution2D(filters=6,kernel_size=4,padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Convolution2D(filters=128,kernel_size=3,padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Convolution2D(filters=128,kernel_size=2,padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Flatten())
model.add(Dense(units=128,activation = 'relu'))
model.add(Dense(units = 64, activation = 'relu'))
model.add(Dense(units = 32, activation = 'relu'))
model.add(Dense(units = 7, activation = 'softmax'))

#COMPILE MODEL
model.compile(optimizer=Adam(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

#SAVE MODEL ARCHITECTURE
model_json = model.to_json()
with open("model/model_architecture"+str(i)+".json", "w") as json_file:
    json_file.write(model_json)

train_path='images/train'
valid_path='images/valid'

classes=['0','1','2','3','4','5','6']
#IMAGE PROCESSING
#COPYED FROM DEEPLIZARD
train_batches=ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)\
    .flow_from_directory(directory=train_path,target_size=(64,64),classes=classes,batch_size=10)
valid_batches=ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)\
    .flow_from_directory(directory=valid_path,target_size=(64,64),classes=classes,batch_size=10)

#TRAIN MODEL IT WILL SAVE WEIGHTS AFTER EVERY 20 ITERATIONS

model.fit(x=train_batches,validation_data=valid_batches,epochs=20,verbose=2,steps_per_epoch=238,validation_steps=49)
model.save_weights('model/weight_21_'+str(i)+'.h5')
print("model/weight_20.h5 SAVED")

model.fit(x=train_batches,validation_data=valid_batches,epochs=20,verbose=2,steps_per_epoch=238,validation_steps=49)
model.save_weights('model/weight_40_'+str(i)+'.h5')
print("model/weight_40.h5 SAVED")

model.fit(x=train_batches,validation_data=valid_batches,epochs=20,verbose=2,steps_per_epoch=238,validation_steps=49)
model.save_weights('model/weight_600_'+str(i)+'.h5')
print("model/weight_60.h5 SAVED")


model.save_weights('model/weight_final'+str(i)+'.h5')
