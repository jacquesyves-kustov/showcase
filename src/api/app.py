import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title='PITCH YOUR GAME',
)


@app.get('/')
def check_health():
    return {'health': 'OK'}


async def run_server(host: str = '0.0.0.0', port: int = 8000):
    config = uvicorn.Config(app, host=host, port=port)
    server = uvicorn.Server(config)
    await server.serve()
