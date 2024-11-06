from fastapi import FastAPI
from app.api.main_router import api_router


def get_application():
    app = FastAPI()

    app.include_router(api_router)

    return app


app = get_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
