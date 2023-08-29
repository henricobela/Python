
FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# EXPOSE 8501

COPY . .

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/app.py"]

