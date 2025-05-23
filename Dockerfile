FROM python:3.9-slim
WORKDIR /usr/src/app
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /usr/src/app
EXPOSE 5000
ENV NAME World
CMD ["python", "app.py"]