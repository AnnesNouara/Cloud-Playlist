from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
import schemas
from schemas import TrackCreate, TrackResponse

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Cloud Tracker API",
    description="Spotify- Like playlist app",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TRACK CREATE POST
@app.post("/tracks", response_model=schemas.TrackResponse)
def create_track(track: TrackCreate, db: Session = Depends(get_db)):
    new_track = models.Track(**track.model_dump())

    db.add(new_track)
    db.commit()
    db.refresh(new_track)

    return new_track


@app.get("/tracks", response_model = list[TrackResponse])
def get_track(db: Session = Depends(get_db)):
    results =  db.query(models.Track).all()

    return results

