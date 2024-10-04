from fastapi import APIRouter, HTTPException, Depends, Response,Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session
from database import get_region_db

from models import house_info as House_model
import csv
security = HTTPBearer()
from region.region_schema import District

router = APIRouter(
    prefix="/house",
)




@router.get("/list")
def show_house(district: District, region_db: Session = Depends(get_region_db)):
    datas = region_db.query(House_model).filter(House_model.region == district).all()
    return [{"type": data.type, "name": data.name, "cnt" : data.cnt, "address" : data.address} for data in datas]
    