FROM python:3.11.3

ENV PYTHONBUFFERED=1

# Setup working directory
WORKDIR /app

# Copy and install requirements.txt
# COPY ./requirements.txt /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the scripts to folder
COPY . .

EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver"]