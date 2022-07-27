FROM python:3.9.10-alpine
COPY requirements.txt ./
COPY . .


RUN pip install --no-cache-dir --upgrade pip

RUN pip install webdriver-manager
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
