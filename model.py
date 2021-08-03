import keras
from keras import layers

def create_model(num_classes: int = 10): 
    return keras.Sequential(
        [
	    layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
	    layers.MaxPooling2D(pool_size=(2, 2)),
	    layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
	    layers.MaxPooling2D(pool_size=(2, 2)),
	    layers.Flatten(),
	    layers.Dropout(0.5),
	    layers.Dense(num_classes, activation="softmax"),
        ]
    )

