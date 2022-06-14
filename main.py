from function import detect_lang
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
class YouTube(BaseModel):
    url_youtube: str
    
@app.post("/api/")
def save_url(url: YouTube):
    print(f"Chequeando el video {url.url_youtube} ...")
    resultado = detect_lang(url.url_youtube)

    if resultado:
        return JSONResponse(resultado, status_code = status.HTTP_200_OK) 

    else: 
        return JSONResponse({'mensaje': 'url inválida'}, status_code = status.HTTP_400_BAD_REQUEST) 



