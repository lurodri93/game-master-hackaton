from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import httpx
import os
from datetime import datetime
import asyncio

# Cargar variables de entorno desde .env
load_dotenv()

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Ajustamos las rutas desde la raíz del proyecto
app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class WebhookConfig(BaseModel):
    webhookUrl: str = os.getenv("WEBHOOK_URL")

class WebhookRequest(BaseModel):
    message: str
    action: str
    sessionID: str

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Crear personaje",
                "action": "create",
                "sessionID": "123e4567-e89b-12d3-a456-426614174000"
            }
        }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/config")
async def config():
    return WebhookConfig()

@app.post("/webhook")
async def webhook(request: WebhookRequest):
    webhook_url = os.getenv("WEBHOOK_URL")
    
    print(f"Usando la URL del webhook: {webhook_url}")  # Registro adicional para depuración
    
    try:
        async with httpx.AsyncClient(timeout=3000.0) as client:
            response = await client.post(
                webhook_url,
                json={
                    "message": request.message,
                    "action": request.action,
                    "sessionID": request.sessionID,
                    "timestamp": datetime.now().isoformat()
                }
            )
            print(f"Respuesta del servidor: {response.status_code}")
            
            if response.status_code == 404:
                return {"error": f"Webhook no encontrado en la URL: {webhook_url}"}
                
            response.raise_for_status()
            
            try:
                response_data = response.json()
                print(f"Datos de la respuesta: {response_data}")
                return {"message": response_data.get("output", "Sin mensaje")}
            except:
                response_text = response.text
                print(f"Respuesta en texto: {response_text}")
                return {"message": response_text}
                
    except httpx.ConnectError as e:
        error_msg = f"No se pudo conectar al webhook: {str(e)}"
        print(error_msg)
        return {"error": error_msg}
        
    except httpx.TimeoutException as e:
        error_msg = f"Tiempo de espera agotado: {str(e)}"
        print(error_msg)
        return {"error": error_msg}
        
    except httpx.HTTPError as e:
        error_msg = f"Error al comunicarse con el webhook: {str(e)}"
        print(error_msg)
        return {"error": error_msg}
        
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}"
        print(error_msg)
        return {"error": error_msg}