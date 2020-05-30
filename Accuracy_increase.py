import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
import numpy

# Model Train function
def model_train(neurons , model , epochs , test) :
            print("\n" , " *** model summary *** " , "\n","Iteration :", test , "\n" , "Neurons : ",neurons , "\n" , " Epochs: ", epochs)
            model.add(Dense(units=neurons , input_dim = 28*28 , activation = 'relu'))
            model.add(Dense(units=300 , input_dim = 28*28 , activation = 'relu'))
            model.add(Dense(units=80 , input_dim = 28*28 , activation = 'relu'))
            model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
            model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
            model.compile(optimizer="Adam" , loss='categorical_crossentropy' , metrics=['accuracy'])
            return model
        
# Function for saving and printing accuracy in txt file
def save_model(fit_model, epochs) :
        text = fit_model.history
        accuracy = text['accuracy'][1] * 100
        accuracy= int(accuracy)
        f=open("accuracy.txt","w+")
        f.write(str(accuracy))
        f.close()
        print("Accuracy of Model is : " , accuracy,"%" )
        return accuracy
           
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

# initializing variables and making a loop for model till desired accuracy is not fullfilled
neurons = 10
accuracy = 0
epochs = 1
test =1
flag = 0

while int(accuracy) <= 93 :
        if flag == 1 :
                model = keras.backend.clear_session()
                neurons = neurons+10
                epochs = epochs+1
                test = test + 1
        model = Sequential()
        model = model_train(neurons , model , epochs , test)
        print("Determining Accuracy...")
        fit_model = model.fit(train_X , train_y , epochs = 3 , verbose= False)
        accuracy=save_model(fit_model , epochs)
        flag = 1