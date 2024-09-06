FROM tiangolo/uvicorn-gunicorn-fastapi
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["uvicorn", "app.py", "--host 0.0.0.0", "--port 8080"]