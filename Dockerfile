FROM python:latest

RUN apt-get update && apt-get install -y pdftk texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-luatex texlive-pstricks

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN pip install --no-cache-dir -e /app

WORKDIR /build

ENTRYPOINT [ "python", "-m", "dungeonsheets.make_sheets" ]
CMD [ "--fancy", "--editable", "--recursive" ]
