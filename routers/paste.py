import aiohttp
from fastapi import APIRouter, HTTPException, status
import schemas


router = APIRouter(
    prefix="/paste",
    tags=["Paste Text"]
)


async def spacebin(txt):
  async with aiohttp.ClientSession() as session:
    u="https://spaceb.in/api/v1/documents/"
    jso={"content": txt, "extension":"txt"}
    async with session.post(u, json=jso) as resp:
      r=await resp.json(content_type=None)
      id_=r["payload"]["id"]
      url="https://spaceb.in/"+id_
      return url


@router.post("/", status_code=200, summary="Paste any text or code")
async def get_ip_info_route(txt, service:str|None=None):
  if not service:
    url=await spacebin(txt)
    return {"url":url}
    
