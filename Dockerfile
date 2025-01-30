FROM python:3.12

ADD . /docs
WORKDIR /docs

RUN apt-get install -y make git
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["make", "html"]