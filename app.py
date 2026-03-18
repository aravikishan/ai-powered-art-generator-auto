
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
import os

# Database setup
DATABASE_URL = "sqlite:///./art_generator.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class ArtPiece(Base):
    __tablename__ = "art_pieces"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image_data = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app setup
app = FastAPI()

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/generate", response_class=HTMLResponse)
async def generate_art_page(request: Request):
    return templates.TemplateResponse("generate.html", {"request": request})

@app.get("/gallery", response_class=HTMLResponse)
async def gallery_page(request: Request, db: Session = Depends(get_db)):
    art_pieces = db.query(ArtPiece).all()
    return templates.TemplateResponse("gallery.html", {"request": request, "art_pieces": art_pieces})

@app.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# API Endpoints
class ArtPrompt(BaseModel):
    prompt: str

@app.post("/api/generate-art")
async def generate_art(prompt: ArtPrompt, db: Session = Depends(get_db)):
    # Mock art generation logic
    new_art = ArtPiece(title=f"Art for '{prompt.prompt}'", image_data="base64encodedstring")
    db.add(new_art)
    db.commit()
    db.refresh(new_art)
    return {"id": new_art.id, "title": new_art.title, "image_data": new_art.image_data}

@app.get("/api/gallery")
async def get_gallery(db: Session = Depends(get_db)):
    art_pieces = db.query(ArtPiece).all()
    return art_pieces

@app.post("/api/save-art")
async def save_art(art_id: int, db: Session = Depends(get_db)):
    # Mock save logic
    art_piece = db.query(ArtPiece).filter(ArtPiece.id == art_id).first()
    if not art_piece:
        raise HTTPException(status_code=404, detail="Art piece not found")
    return {"message": "Art piece saved successfully"}

@app.get("/api/user-profile")
async def get_user_profile():
    # Mock user profile data
    return {"username": "demo_user", "email": "demo@example.com"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
