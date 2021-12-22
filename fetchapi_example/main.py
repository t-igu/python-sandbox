from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def index(request: Request):
    return HTMLResponse(
"""
<html>
<head></head>
<body>
<H1>hello</H1>
<script>
    const api = async()=>{
        const url="http://127.0.0.1:8000/json/address";
        return await fetch(url).then(response => response.json())
    }
    const func = async()=>{
        const getData = await api();
        console.log(getData);
    }
    func();
</script>
</body>
</html>
"""
    )
