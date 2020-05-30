import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
import numpy

# LOADING MNIST DATASET IN OUR MODEL
(train_X , train_y) , (test_X , test_y) = mnist.load_data("mnist.data")

# RESHAPING DATA AND CHANGING IT'S SIZE
test_X = test_X.reshape(-1 , 28*28)
train_X = train_X.reshape(-1 , 28*28)
test_X = test_X.astype("float32")
train_X = train_X.astype("float32")

# ONE HOT ENCODING
test_y = to_categorical(test_y)
train_y = to_categorical(train_y)

# load Model
model = Sequential()
model.add(Dense(units=20 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=300 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=80 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
model.compile(optimizer="Adam" , loss='categorical_crossentropy' , metrics=['accuracy'])
fit_model = model.fit(train_X , train_y , epochs = 3 , verbose= False)

# Saving and printing accuracy of our model
text = fit_model.history
accuracy = text['accuracy'][1] * 100
accuracy= int(accuracy)
f=open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()
print("Accuracy of Model is : " , accuracy,"%" )