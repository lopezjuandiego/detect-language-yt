from function import detect_lang
from fastapi import FastAPI

app = FastAPI()

    
@app.post("/api/")
async def save_url(url: str):
    print(f"Chequeando el video {url} ...")
    resultado = detect_lang(url)

    if resultado:
        return {'mensaje' : resultado}

    else: 
        return {'mensaje' : f'{url} no es una URL válida.' }


# detect_lang(url)

