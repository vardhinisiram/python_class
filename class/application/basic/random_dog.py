
import urllib.request
import os
import json

def ret_dog_image():
    
    with urllib.request.urlopen("https://random.dog/woof.json") as response:
        data = json.loads(response.read(300))
        # print(response.read(300))
        print(data)
        print(type(data))
        dog_image = data["url"]
        print("The image url is ", dog_image)
        image = urllib.request.urlopen(dog_image)
        file_name = dog_image.split("/")[-1]
        with open(file=file_name, mode='wb') as f:
            f.write(image.read())
        return file_name
            
        
        