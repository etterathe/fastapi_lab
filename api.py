from io import BytesIO
from fastapi import FastAPI, UploadFile, File, Depends
from starlette.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from math import sqrt
from datetime import date
from PIL import Image, ImageOps

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get("/prime/{number}")
async def checkPrime(number: int):
    prime_flag = 0
    if(number > 1):
        for i in range(2, int(sqrt(number)) +1):
            if(number % i == 0):
                prime_flag = 1
                break
            if (prime_flag == 0):
                return {"message": "True"}
            else:
                return {"message": "False"}
    else:
        return {"message": "False"}

@app.post("/picture/invert")
async def invert_image(file: UploadFile = File(...)):
    img = Image.open(file.file)
    inverted_img = ImageOps.invert(img)
    stream_img = BytesIO()
    inverted_img.save(stream_img, "JPEG")
    stream_img.seek(0)
    return StreamingResponse(content= stream_img, media_type="image/jpeg")

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}

@app.get('/date')
async def index(token: str = Depends(oauth2_scheme)):
    return {'date': date.today()}




