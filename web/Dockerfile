FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
ENV APP_HOME=/src
RUN mkdir $APP_HOME/static
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt --upgrade
ADD . ../src/
