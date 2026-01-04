import requests
import asyncio
import time

s = time.time()

async def catch_poki(num):
    url = 'https://pokeapi.co/api/v2/pokemon/'+ str(num)
    resp = requests.get(url)
    pokimon = resp.json()
    print(pokimon['name'])

async def main():
    for i in range(1,5):
        await catch_poki(i)

asyncio.run(main())
    

e = time.time()
print("Execution Time:",(e-s))
