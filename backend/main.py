from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
import schemas
from schemas import TrackCreate, TrackResponse
from fastapi.middleware.cors import CORSMiddleware


# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Cloud Tracker API",
    description="Spotify- Like playlist app",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

# get all tracks
@app.get("/tracks", response_model = list[TrackResponse])
def get_track(db: Session = Depends(get_db)):
    results =  db.query(models.Track).all()

    return results


# get track by id
@app.get("/tracks/{track_id}",response_model=schemas.TrackResponse)
def get_track_id(track_id: int, db: Session = Depends(get_db)):
    track = db.query(models.Track).filter(models.Track.id == track_id).first()

    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    return track

# deletes a track
@app.delete("/tracks/{track_id}/delete")
def delete_track(track_id: int, db:Session = Depends(get_db)):
    track = db.query(models.Track).filter(models.Track.id == track_id).first()

    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    
    db.delete(track)
    db.commit()

    return {"message": "Track has been deleted."}
  
@app.patch("/tracks/{track_id}/edit", response_model=schemas.TrackResponse)
def update_track(
    track_id: int,
    track_update: schemas.TrackUpdate,
    db: Session = Depends(get_db),
):
    # 1. Get existing track
    track = db.query(models.Track).filter(models.Track.id == track_id).first()

    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    # 2. Get only the fields that were actually sent (exclude_unset=True)
    update_data = track_update.model_dump(exclude_unset=True)

    # 3. Apply each provided field to the SQLAlchemy model
    for key, value in update_data.items():
        setattr(track, key, value)

    # 4. Commit changes and refresh from DB
    db.commit()
    db.refresh(track)

    # 5. Return updated track
    return track

