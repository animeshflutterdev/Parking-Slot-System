from fastapi import FastAPI
from app.core.routers import router as api_router
from app.core.config import appconfig
from app.core.logger import log
from uvicorn import Config, Server
from app.core.database import ( Base,engine )

Base.metadata.create_all(bind=engine)

app = FastAPI(title=appconfig.APP_NAME)
app.include_router(api_router)

@app.get("/")
async def root():
    log.info(message="info",data="Root endpoint called!", fileName="main.py")
    log.warning(message="warning",data="Root endpoint called!", fileName="main.py")
    return {"message": f'{appconfig.APP_NAME} running', "desc": appconfig.APP_DESCRIPTION}


if __name__ == "__main__":
    config = Config(app, host=appconfig.APP_HOST, port=appconfig.APP_PORT, reload=True)
    server = Server(config)
    server.run()