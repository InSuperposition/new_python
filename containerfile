# FROM gcr.io/distroless/python3-debian12:latest
FROM python:3.11-slim AS build-env
COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir --upgrade pip &&\
 pip3 install --no-cache-dir '.[dev,test]'


# FROM gcr.io/distroless/python3
# COPY --from=build-env /app /app
# WORKDIR /app
# CMD ["main_module/__main__.py", "/app"]
# CMD ["-V"]
