FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip python3.12-venv python3-xyz
COPY . /app
WORKDIR /app
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
