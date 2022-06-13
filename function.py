from google.cloud import translate_v2 as translate
import youtube_transcript_downloader
from lenguajes import language_short_name

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def detect_lang(url):
    # while not url.startswith('https://www.youtube'):
    #     print('No es una URL válida.')
        # url = input('Ingresá la URL de un video de YouTube: ')
        
    try:
        transcript = youtube_transcript_downloader.get_transcript(url)
        #toma el subtitulo automático de YouTube (en key trae el timecode y en val el texto)
        for key, val in transcript.items():
            if len(val)>28:
                sub = val
                
        #detecta lenguaje y le asigna un valor de probabilidad
        traductor = translate.Client()
        txtOriginal = sub   
        result= traductor.detect_language(txtOriginal)
        idioma =language_short_name.get(result["language"]).upper()
            
        if result['confidence'] > 0.90:

            txt_resultado = f'Hay un {round(result["confidence"],2) * 100}% de posibilidades de que el idioma sea: {idioma}.'
            return txt_resultado
        
        elif result['confidence'] > 0.70 and result['confidence']< 0.90:
            txt_resultado = f'Hay un {round(result["confidence"],2) * 100}% de posibilidades de que el idioma sea: {idioma} o el video no tiene subtítulo autómatico para reconocerlo.'
            return txt_resultado

        else:
            txt_resultado = 'No se puede reconocer el idioma del video o no tiene subtítulos automáticos'
            return txt_resultado

    except: 
        return f'La url ingresada no es válida.'  
                

    