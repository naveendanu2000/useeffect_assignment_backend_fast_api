from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.connections.connection import create_pool, close_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to PG DB")

    try:
        await create_pool(app)
        print("Connected to db!")

    except Exception as e:
        print(f"Unable to connect to db!: {e}")
        raise

    try:
        yield
    finally:
        print("Disconnecting from PG DB")
        try:
            await close_pool(app)
            print("Disconnected from DB!")
        except Exception as e:
            print(f"Unable to disconnect from DB! {e}")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "Welcome to useeffect_assignment_backend_home"
