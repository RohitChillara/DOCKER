FROM python:3.14-slim                              # start from a minimal Linux with Python 3.14
WORKDIR /app                                       # work inside /app in the container
COPY requirements.txt .                            # bring in JUST the dependency list first
RUN pip install --no-cache-dir -r requirements.txt # install deps (this layer caches)
COPY . .                                           # now bring in the rest of the code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  # how to start it