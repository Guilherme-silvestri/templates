FROM python:3.11.4-slim-bookworm as base
 
ENV PATH /usr/local/bin:$PATH
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONFAULTHANDLER 1 \
    PYTHONHASHSEED random \
    PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1
 
ARG TOKEN_USER
ARG TOKEN_PASS
 
RUN apt update -qq && apt install -qq --no-install-recommends -y \
    make gcc libffi-dev \
    && pip install poetry
 
WORKDIR /app
COPY pyproject.toml /app/
 
RUN poetry config http-basic.artifacts $TOKEN_USER $TOKEN_PASS
RUN poetry config virtualenvs.create false
RUN poetry install -q --only main
 
COPY . /app
 
# Estágio de compilação para cobertura de código
FROM base AS build_coverages
 
RUN mkdir logs
RUN poetry install -q
RUN make test
# Estágio final
FROM base AS final
 
COPY --from=build_coverages /app /app
COPY --from=build_coverages /app/coverage.xml /app/coverage.xml
 
# Limpeza
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache
 
ENTRYPOINT ["sh", "start.sh"]