
from fastapi import FastAPI

app = FastAPI()

@app.get("/portfolio")
def get_portfolio():
    return {
        "name": "Ella Example",
        "bio": "Web developer and designer.",
        "projects": [
            {"title": "Project One", "description": "A cool project."},
            {"title": "Project Two", "description": "Another cool project."}
        ]
    }

@app.get("/projects")
def get_projects():
    return [
        {"title": "Project One", "description": "A cool project."},
        {"title": "Project Two", "description": "Another cool project."}
    ]

@app.get("/contact")
def get_contact():
    return {
        "email": "ella@example.com",
        "linkedin": "https://linkedin.com/in/ellaexample"
    }
