FROM python:3.7-alpine

RUN apk add --no-cache pdftk texlive

WORKDIR /tmp

COPY ./ ./

RUN python setup.py install

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install dungeonsheets pypdftk latexpages


WORKDIR /examples

ENTRYPOINT [ "makesheets" ]
