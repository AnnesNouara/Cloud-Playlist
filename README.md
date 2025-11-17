🎧 Cloud Playlist Tracker

A lightweight Spotify-like playlist & track management API built with FastAPI.

Cloud Playlist Tracker is a backend-first project designed to manage tracks and playlists in a clean, scalable way. It follows real-world backend architecture principles and demonstrates your understanding of API design, data modelling, and modern Python development workflows.

This project is part of my personal portfolio to showcase practical backend engineering skills using Python, FastAPI, SQLAlchemy, and SQLite — later expanding to a full Svelte front-end and authentication.

🚀 Features
✅ Track Management (CRUD)

Add tracks (name, artist, duration)

Retrieve all tracks

Retrieve a track by ID

Update a track (coming soon)

Delete a track (coming soon)

🗂 Playlist System (coming next)

Create playlists

Add/remove tracks from playlists

Many-to-many relationship using a join table

🔒 Authentication (future upgrade)

User accounts

JWT login/signup

Per-user playlists

🎨 Frontend (in progress)

Svelte + TypeScript interface

Track listing

Playlist UI

Track forms

🛠️ Tech Stack

Backend

FastAPI — high-performance Python web framework

SQLAlchemy — ORM for modelling and database interaction

SQLite — lightweight DB for development

Pydantic — data validation and schema definitions

Uvicorn — ASGI server

Frontend (later)

SvelteKit

TypeScript

Fetch API for communicating with FastAPI

Other

Git & GitHub

Virtual environments (venv)

📂 Project Structure
cloud-playlist-app/
│
├── backend/
│   ├── main.py          # FastAPI main application
│   ├── database.py      # SQLite connection + SQLAlchemy Base
│   ├── models.py        # Track model (and later Playlist models)
│   ├── schemas.py       # Pydantic schemas for validation
│   └── venv/            # Virtual environment
│
└── frontend/            # (Future) SvelteKit project

📡 API Endpoints
➕ Create Track

POST /tracks

Request body:

{
  "song_name": "Let it Happen",
  "artist": "Tame Impala",
  "duration": "4M 11S"
}

📄 Get All Tracks

GET /tracks

Response example:

[
  {
    "id": 1,
    "song_name": "Let it Happen",
    "artist": "Tame Impala",
    "duration": "4M 11S"
  }
]

▶️ Running the Project
1. Create the virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
pip install fastapi sqlalchemy pydantic uvicorn

3. Start the server
uvicorn main:app --reload

4. View API Docs

Go to:

👉 http://127.0.0.1:8000/docs

🧱 Database

Tracks are stored in a local SQLite file:

tracks.db


Created automatically on app startup using:

Base.metadata.create_all(bind=engine)

🎯 Roadmap

 Track CRUD (Create + Get complete)

 Track Update & Delete

 Playlist model

 Playlist–Track relationship

 User system

 JWT Authentication

 Svelte Frontend UI

 Docker deployment

 Cloud deployment (Railway / Render / AWS)

💡 Purpose

This project demonstrates practical backend development skills including:

API design

SQL database modelling

Python backend architecture

Version control & GitHub workflow

Building scalable, real-world project structure

Incremental feature development

It also serves as the foundation for a full-stack portfolio project.
