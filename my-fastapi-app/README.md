# My FastAPI Application

This is a simple FastAPI application that demonstrates how to set up a FastAPI server and deploy it using Docker.

## Project Structure

```
my-fastapi-app
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   └── types
│       └── index.py     # Data models and types used in the application
├── Dockerfile            # Dockerfile for building the application image
├── requirements.txt      # Python dependencies for the project
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-fastapi-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application locally, execute the following command:
```
uvicorn src.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Docker Deployment

To build and run the application using Docker, follow these steps:

1. Build the Docker image:
   ```
   docker build -t my-fastapi-app .
   ```

2. Run the Docker container:
   ```
   docker run -d -p 8000:8000 my-fastapi-app
   ```

The application will be accessible at `http://localhost:8000`.

## Usage

You can access the API documentation at `http://localhost:8000/docs` after running the application.

## License

This project is licensed under the MIT License.