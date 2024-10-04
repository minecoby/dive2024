from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from database import user_Base, stamp_Base, region_Base
from datetime import datetime

# User 모델 정의
class User(user_Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), unique=True, nullable=False, index=True)  
    password = Column(String(255), nullable=False)
    user_name = Column(String(30), nullable=False)

# 지역구 테이블 정의
class District(region_Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False) 

# Stamp 테이블 정의
class Stamp(stamp_Base):
    __tablename__ = "stamps"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False)  
    title = Column(String(255), nullable=False)  
    description = Column(Text, nullable=True)  
    latitude = Column(Float, nullable=False)  
    longitude = Column(Float, nullable=False)  
    district_id = Column(Integer, nullable=False, index = True)  
    created_at = Column(DateTime, default=datetime.utcnow)

# 유저 스탬프 기록 테이블 정의
class UserStamp(stamp_Base):
    __tablename__ = "user_stamps"
    received_at = Column(DateTime, default=datetime.utcnow)
    stamp_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)

class subway_info(region_Base):
    __tablename__ = "station"
    id = Column(Integer, primary_key=True, index=True)
    line = Column(String(10))
    station_name = Column(String(20), index= True)
    Meeting_Point = Column(Integer)
    Locker = Column(Integer)
    Photo_Booth = Column(Integer)
    ACDI = Column(Integer)#무인민원발급기
    Infant_Nursing_Room = Column(Integer)
    Wheelchair_Lift = Column(Integer)
    TPVI = Column(Integer)#시각장애인유도로
    URP = Column(Integer)#도시경찰대

class subway_Locker_info(region_Base):
    __tablename__ = "Locker"
    id = Column(Integer, primary_key=True, index=True)
    station_name = Column(String(20), index= True)
    Detailed_Location = Column(String(100))
    Small = Column(Integer)
    Medium = Column(Integer)
    Large = Column(Integer)
    Extra_Large = Column(Integer)
    Usage_fee = Column(String(100))

class house_info(region_Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(15), index=True)
    name = Column(String(100), index=True)
    cnt = Column(Integer)
    address = Column(String(500))
    region = Column(String(20),index=True)