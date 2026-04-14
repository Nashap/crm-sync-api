from fastapi import FastAPI
from database import Base, engine

from routes import meta_routes, google_routes, linkedin_routes, whatsapp_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(meta_routes.router)
app.include_router(google_routes.router)
app.include_router(linkedin_routes.router)
app.include_router(whatsapp_routes.router)


@app.get("/")
def root():
    return {"message": "CRM Sync API Running"}