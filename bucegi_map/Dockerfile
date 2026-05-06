FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Make the system python3-gdal bindings visible to pip's Python
RUN echo "/usr/lib/python3/dist-packages" > \
    /usr/local/lib/python3.12/site-packages/system-gdal.pth

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
