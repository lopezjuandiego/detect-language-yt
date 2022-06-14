from function import detect_lang
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
# class YouTube(BaseModel):
#     url_youtube: str = None
    
@app.post("/api/")
def save_url(url: str):
    print(f"Chequeando el video {url} ...")
    resultado = detect_lang(url)

    if resultado:
        return JSONResponse({'mensaje' : resultado}, status_code = status.HTTP_200_OK) 

    else: 
        return JSONResponse({'mensaje' : f'{url} no es una URL válida.'}, status_code = status.HTTP_400_BAD_REQUEST) 


# detect_lang(url)

