from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# ──────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/cadastro", response_class=HTMLResponse)
async def cadastro_hospede(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...),
):

    id = add_hospede(nome=nome, email=email, telefone=telefone, cpf=cpf)  # só uma vez
    return RedirectResponse(url="/", status_code=303)


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    if not consulta_hospedes():
        return {"Aviso":"Nenhum cliente cadastrado"}
    else:
        return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"hospedes": consulta_hospedes()}
    )