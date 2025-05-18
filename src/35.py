import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import fetch_openml
from PIL import Image

def load_image_data():
    mnist = fetch_openml('mnist', version=1)
    images = mnist['data']
    labels = mnist['target']

    x_train, y_train = images[:60000], labels[:60000]
    x_test, y_test = images[60000:], labels[60000:]

    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    return x_test, y_test

def display_image(image):
    img = Image.open(image).resize((28, 28))
    np_arr = tf.keras.utils.img_to_array(img)
    plt.imshow(np_arr, cmap=plt.cm.binary)
    plt.title('predicted label: {}'.format(y_pred))
    plt.xticks([])
    plt.yticks([])

# Example usage
x_test, y_test = load_image_data()
display_image(x_test[0])
