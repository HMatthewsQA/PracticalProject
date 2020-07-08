FROM python:3.8
RUN apt update
RUN apt install python-pip -y 
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
