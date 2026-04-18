from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.deletion import CASCADE

from django.db.models import signals
from django.dispatch import receiver

class Profile(models.Model):
    GENDER_CHOICE = [
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHERS','OTHERS'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    addressLine1 = models.CharField(max_length=200, null=True, blank=True)
    addressLine2 = models.CharField(max_length=200, null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    timestamp =  models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return str(self.user.username)



class Test(models.Model):
    profile = models.ForeignKey(Profile,on_delete=CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='static/images')
    resulturl = models.CharField(max_length=300, null=True, blank=True)
    timestamp =  models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
                          
    def __str__(self):
        return str(self.timestamp)



import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import pathlib


@receiver(signals.post_save, sender=Test)
def my_handler(sender, instance, created, **kwargs):
    
    if created:
        data_dir = "../new_data"
        data_dir = pathlib.Path(data_dir)

        batch_size = 32
        img_height = 180
        img_width = 180
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        
        class_names = train_ds.class_names
        print(class_names)

        num_classes = 9

        model = Sequential([
            layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
        ])

        model.load_weights('../my_checkpoint.ckpt')


        test_image_path = instance.image.url[1:]
        #print(test_image_path)

        img = keras.preprocessing.image.load_img(
            test_image_path, target_size=(img_height, img_width)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        predictions = model.predict(img_array,batch_size = 2)
        score = tf.nn.softmax(predictions[0])


        plt.figure(figsize=(16,9))

        for index in range(0,len(score)):
            prediction = score[index]
            prediction_score = 100 * np.max(prediction)
            print('class {}, score: {:.2f}'.format(class_names[index], prediction_score))
            plt.bar('{}: {:.2f} '.format(class_names[index], prediction_score),prediction_score) 

        plt.title('Predictions', size = 20)
        plt.xticks(size=10,rotation=45)
        plt.yticks(size=10)

        result_image_path = test_image_path + "_result.png"
        
        Test.objects.filter(id=instance.id).update(resulturl=result_image_path)


        plt.savefig(result_image_path, bbox_inches='tight')
        #plt.show()


    



