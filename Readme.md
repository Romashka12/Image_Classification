# App to classify images

Creates a simple flask app to classify images using Flask and MobileNet. Docker file is also provided.

Use commands below to create image.

docker build -t image_class_app .
docker run  --publish 5000:5000 --name=flask  image_class_app
