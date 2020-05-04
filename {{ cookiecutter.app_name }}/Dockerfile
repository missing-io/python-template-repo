FROM python:3.6-alpine

LABEL maintainer="missing-io"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["./{{cookiecutter.app_name }}.py"]
