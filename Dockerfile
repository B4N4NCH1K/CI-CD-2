FROM python:3.9.2
RUN pip install flask
WORKDIR /code
COPY web.py /code/web.py
COPY static/ /code/static 
EXPOSE 5000
CMD ["python3", "web.py"]
