from sqlalchemy import Column, String, Integer
from database import Base

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    song_name = Column(String, nullable=False, index=True)
    artist = Column(String, nullable=False, index=True)
    duration = Column(String, nullable=False)