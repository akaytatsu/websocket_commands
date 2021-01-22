FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app -p
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8080

CMD ["flask", "run", "--host", "0.0.0.0"]
