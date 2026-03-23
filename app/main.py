from fastapi import FastAPI
from app.database import Base, engine
from app.models import task
from app.routes import task_routes
from app.models import user
from app.routes import task_routes, user_routes


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_routes.router)
app.include_router(user_routes.router)

