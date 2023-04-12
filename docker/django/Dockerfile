###
### Ubuntu 2004 with default Python 3.9
###

# -- Base --

FROM ubuntu:20.04 AS base

RUN apt-get update -y \
  && apt-get install --yes --no-upgrade --no-install-recommends \
    libmysqlclient-dev \
    mysql-client \
    python3.9 \
    python3-pip \
  && apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/apt/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# -- Build --

FROM base AS build

RUN apt-get update -y \
  && apt-get install --yes --no-upgrade --no-install-recommends \
    gcc \
    python3.9-dev \
    curl \
    git \
    ca-certificates \
  && apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/apt/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

RUN curl -o /usr/local/share/ca-certificates/cacert.crt "https://curl.se/ca/cacert.pem"
COPY django/subway_ads/scholarship-rice-edu.crt /usr/local/share/ca-certificates/scholarship-rice-edu.crt

RUN update-ca-certificates


WORKDIR /srv/dspace-django

RUN python3.9 -m pip install --user --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

COPY django/requirements.txt .
RUN python3.9 -m pip install --user --no-cache-dir -r ./requirements.txt

# This isn't working, despite their documentation
# RUN python3.9 -m pip install --user --no-cache-dir git+https://github.com/django-haystack/django-haystack.git#egg=django-haystack

# -- Release --

FROM build AS release

WORKDIR /srv/dspace-django

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH=/root/.local/bin:$PATH

COPY --from=build /root/.local /root/.local
COPY . .

COPY django/hacks/solr_backend.py /root/.local/lib/python3.9/site-packages/haystack/backends/

ARG GUNICORN_PORT="8000"
ARG GUNICORN_OPTS="--reload --workers 3 --threads 2 --worker-class gthread"

ENV GUNICORN_PORT=${GUNICORN_PORT}
ENV GUNICORN_OPTS=${GUNICORN_OPTS}

EXPOSE $GUNICORN_PORT

CMD gunicorn --bind 0.0.0.0:$GUNICORN_PORT $GUNICORN_OPTS subway_ads.wsgi