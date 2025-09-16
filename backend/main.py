from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.madre_routes import router as madre_router
from app.routes.neonato_routes import router as neonato_router
from app.routes.llanto_routes import router as llanto_router

app = FastAPI(title="NEO-ID Backend")

# ✅ CORS para conectar con frontend Vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción pon dominio fijo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(madre_router)
app.include_router(neonato_router)
app.include_router(llanto_router)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Backend funcionando"}
