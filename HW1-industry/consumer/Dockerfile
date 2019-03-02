FROM python:3.5-alpine
ADD . /code
WORKDIR /code
RUN apk add --update py2-pip
RUN apk --no-cache --update-cache add python-dev py-numpy gcc gfortran musl-dev freetype-dev
RUN pip install -r requirements.txt
CMD ["python", "./consumer/consumer.py"]
