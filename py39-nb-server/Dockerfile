FROM debian:buster-slim

RUN apt-get update && apt-get install -y pypy pip gfortran

WORKDIR /usr/src/app

RUN pip install --no-cache-dir numpy pandas matplotlib scikit-learn pillow plotly seaborn torch torchvision scipy scrapy tensorflow keras keras-nlp keras-cv beautifulsoup4 jupyter

ENV KERAS_BACKEND="tensorflow" --jax OR torch

EXPOSE 8888

CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--allow-root"]
