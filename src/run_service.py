import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    from config import settings

    uvicorn.run("service:app", host=settings.HOST, port=settings.PORT, reload=settings.is_dev())
