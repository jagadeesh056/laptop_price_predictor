#baseimage
FROM python:3.10
#workdir
WORKDIR /app
#copy
COPY . .
#run
RUN pip install -r requirements.txt
#port
EXPOSE 8501
#command
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]