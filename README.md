# FastAPI Portfolio API

This is a FastAPI backend for a personal portfolio website. The API serves portfolio data and is designed to be hosted on Render. The frontend is built in HTML.

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Access the API at [http://localhost:8000/portfolio](http://localhost:8000/portfolio)


## Deployment on Render

1. Push your code to a public GitHub repository.
2. Log in to [Render](https://render.com/) and create a new Web Service.
3. Connect your repository and select the root directory.
4. Render will detect the `render.yaml` file and use it for configuration.
5. The service will build and start automatically. Your API will be available at the URL provided by Render.

### Key files for deployment
- `requirements.txt`: Python dependencies
- `render.yaml`: Render deployment configuration

## Endpoints
- `/portfolio`: Returns portfolio data in JSON format.
- `/projects`: Returns a list of projects.
- `/contact`: Returns contact information.
