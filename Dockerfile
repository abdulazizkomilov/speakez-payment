FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv

RUN apt-get update && apt-get install -y \
    apt-utils curl netcat vim gettext python3-venv libpq-dev gcc postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY .deploy/entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "/entrypoint.sh"]
