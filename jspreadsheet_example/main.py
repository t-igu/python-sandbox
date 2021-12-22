import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, ORJSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "jspreadsheet-ce-example"})

@app.get("/jsuite", response_class=HTMLResponse)
async def jsuite_example(request: Request):
    return templates.TemplateResponse("jsuite.html", {"request": request, "title": "jsuite-example"})

@app.get("/jexcel1", response_class=HTMLResponse)
async def excel1_example(request: Request):
    return templates.TemplateResponse("jexcel1.html", {"request": request, "title": "excel-example1"})

@app.get("/jexcel2", response_class=HTMLResponse)
async def excel2_example(request: Request):
    return templates.TemplateResponse("jexcel2.html", {"request": request, "title": "excel-example2"})

@app.get("/jexcel3", response_class=HTMLResponse)
async def excel3_example(request: Request):
    return templates.TemplateResponse("jexcel3.html", {"request": request, "title": "excel-example3"})

@app.get("/json/pref")
async def get_preflist(request: Request):
    pref = [
        {"id":"1", "name":"北海道"},
        {"id":"2", "name":"青森県"},
        {"id":"3", "name":"岩手県"},
        {"id":"4", "name":"宮城県"},
        {"id":"5", "name":"秋田県"},
        {"id":"6", "name":"山形県"},
        {"id":"7", "name":"福島県"},
        {"id":"8", "name":"茨城県"},
        {"id":"9", "name":"栃木県"},
        {"id":"10", "name":"群馬県"},
        {"id":"11", "name":"埼玉県"},
        {"id":"12", "name":"千葉県"},
        {"id":"13", "name":"東京都"},
        {"id":"14", "name":"神奈川県"},
        {"id":"15", "name":"新潟県"},
        {"id":"16", "name":"富山県"},
        {"id":"17", "name":"石川県"},
        {"id":"18", "name":"福井県"},
        {"id":"19", "name":"山梨県"},
        {"id":"20", "name":"長野県"},
        {"id":"21", "name":"岐阜県"},
        {"id":"22", "name":"静岡県"},
        {"id":"23", "name":"愛知県"},
        {"id":"24", "name":"三重県"},
        {"id":"25", "name":"滋賀県"},
        {"id":"26", "name":"京都府"},
        {"id":"27", "name":"大阪府"},
        {"id":"28", "name":"兵庫県"},
        {"id":"29", "name":"奈良県"},
        {"id":"30", "name":"和歌山県"},
        {"id":"31", "name":"鳥取県"},
        {"id":"32", "name":"島根県"},
        {"id":"33", "name":"岡山県"},
        {"id":"34", "name":"広島県"},
        {"id":"35", "name":"山口県"},
        {"id":"36", "name":"徳島県"},
        {"id":"37", "name":"香川県"},
        {"id":"38", "name":"愛媛県"},
        {"id":"39", "name":"高知県"},
        {"id":"40", "name":"福岡県"},
        {"id":"41", "name":"佐賀県"},
        {"id":"42", "name":"長崎県"},
        {"id":"43", "name":"熊本県"},
        {"id":"44", "name":"大分県"},
        {"id":"45", "name":"宮崎県"},
        {"id":"46", "name":"鹿児島県"},
        {"id":"47", "name":"沖縄県"},
    ]
    return ORJSONResponse(pref)

@app.get("/json/address")
async def json_addresslist(request: Request):
    return FileResponse('static/hokkaido.json')

@app.get("/json/address_many")
async def json_addresslist(request: Request):
    return FileResponse('static/zenkoku_all.json')
