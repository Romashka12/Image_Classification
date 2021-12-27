FROM pytorch/pytorch

WORKDIR /usr/src/app

COPY . ./

RUN conda config --add channels conda-forge

RUN conda env update --file flask_app_req.yml

WORKDIR /usr/src/app/image_classification_app

ENTRYPOINT flask run -p 5000 --host=0.0.0.0


