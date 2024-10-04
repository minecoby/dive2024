from fastapi import APIRouter, HTTPException, Depends, Response,Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session
from database import get_region_db
from models import District as District_Model, subway_info as Subway_Model, subway_Locker_info as Locker_Model, house_info as House_model

from region.region_schema import District
import csv


security = HTTPBearer()


router = APIRouter(
    prefix="/region",
)

@router.post("/add")
def add_district(district: District,region_db: Session = Depends(get_region_db)):
    district_create = District_Model(name = district.name
            )
    region_db.add(district_create)
    region_db.commit()
    region_db.refresh(district_create)
    return district_create

@router.get("/list")
def see_district_list(region_db: Session = Depends(get_region_db)):
    districts = region_db.query(District_Model).all()  
    return [{"id": district.id, "name": district.name} for district in districts]

@router.delete("/delete/{district_id}")
def delete_district(district_id: int, region_db: Session = Depends(get_region_db)):
    district = region_db.query(District_Model).filter(District_Model.id == district_id).first()
    
    if district is None:
        raise HTTPException(status_code=404, detail="해당 지역구 없음")
    
    region_db.delete(district)
    region_db.commit()
    
    return {"detail": "삭제완료"}

@router.get("/subway/list")
def show_list_subway(region_db: Session = Depends(get_region_db)):
    station_data = region_db.query(Subway_Model).all()
    return  [{"id": station.id, "name": station.station_name} for station in station_data]