from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from .services.recommender import generate_recommendation

load_dotenv()
app = FastAPI(title="PocketSmart AI")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/planner/{kind}", response_class=HTMLResponse)
async def planner(request: Request, kind: str):
    if kind not in {"home","party","jewelry"}:
        return HTMLResponse("Planner not found", status_code=404)
    return templates.TemplateResponse(f"{kind}.html", {"request": request})

@app.post("/generate-home", response_class=HTMLResponse)
async def generate_home(request: Request, budget: float = Form(...), room: str = Form(...),
                        style: str = Form(...), items: str = Form(...)):
    data = generate_recommendation("home", {"budget":budget,"room":room,"style":style,"items":items})
    return templates.TemplateResponse("result.html", {"request":request, "data":data, "kind":"Home Interior"})

@app.post("/generate-party", response_class=HTMLResponse)
async def generate_party(request: Request, budget: float = Form(...), event: str = Form(...),
                         guests: int = Form(...), venue: str = Form(...)):
    data = generate_recommendation("party", {"budget":budget,"event":event,"guests":guests,"venue":venue})
    return templates.TemplateResponse("result.html", {"request":request, "data":data, "kind":"Party"})

@app.post("/generate-jewelry", response_class=HTMLResponse)
async def generate_jewelry(request: Request, budget: float = Form(...), occasion: str = Form(...),
                           style: str = Form(...), outfit: str = Form(""), image: UploadFile|None = File(None)):
    data = generate_recommendation("jewelry", {"budget":budget,"occasion":occasion,"style":style,"outfit":outfit,
                                                "image_uploaded": bool(image and image.filename)})
    return templates.TemplateResponse("result.html", {"request":request, "data":data, "kind":"Jewelry"})

@app.get("/api/health")
async def health():
    return {"status":"ok","service":"PocketSmart AI"}
