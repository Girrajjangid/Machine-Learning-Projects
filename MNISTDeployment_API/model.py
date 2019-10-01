from tensorflow import keras as kr

from sklearn.externals import joblib

fashion_mnist = kr.datasets.fashion_mnist
(x_train, y_train) , (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

model = kr.Sequential([kr.layers.Flatten(input_shape=(28,28)),
                      kr.layers.Dense(128,activation='relu'),
                      kr.layers.Dense(10,activation='softmax')
                      ])

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2)
model.save('model.h5')
print('model saved.')