FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY /my-fastapi-app/requirements.txt .

# Install the dependencies
RUN pip install  -r /my-fastapi-app/requirements.txt

# Copy the application code
COPY /my-fastapi-app/src /app/src

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]