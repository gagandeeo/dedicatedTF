FROM continuumio/miniconda3 AS builder

COPY  environment.yml .
RUN conda env create --file environment.yml

RUN conda install -c conda-forge conda-pack

RUN /bin/bash -c "conda-pack -n dev.tensorflow.env -o /tmp/env.tar && mkdir venv && cd venv && tar xf /tmp/env.tar && rm /tmp/env.tar"

RUN venv/bin/conda-unpack


FROM debian:buster AS runtime

ARG CACHEBUST=1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 APP_USER=app APP_HOME=/home/app

RUN useradd --no-log-init -r -m -U "$APP_USER"

COPY --from=builder --chown="$APP_USER":"$APP_USER" venv "$APP_HOME"/dev.tensorflow.env
COPY --chown="$APP_USER":"$APP_USER" ./ "$APP_HOME"/app

USER "$APP_USER"
WORKDIR "$APP_HOME"/app


ENV PATH="$APP_HOME/dev.tensorflow.env/bin:$PATH"

CMD uvicorn main:app --reload --workers $(nproc) --host 0.0.0.0 --port 8080