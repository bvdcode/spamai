FROM python:3.13.3-slim

WORKDIR /app

RUN pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers==4.51.2
RUN pip install flask-cors==4.0.1
RUN pip install Flask==3.1.0

COPY . .
RUN python app.py --download-model

EXPOSE 8080
CMD ["python", "app.py"]