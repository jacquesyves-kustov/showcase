import argparse
import asyncio

from api.app import run_server


async def startup(mode: str):
    if mode == 'backend':
        await run_server()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='Run a special container.', choices=['backend'])
    args = parser.parse_args()

    loop = asyncio.new_event_loop()
    loop.run_until_complete(startup(args.mode))
