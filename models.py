from sqlalchemy import Integer,String,DateTime,Float,Column


from database import base




class Location(base):
    __tablename__="location"
    id = Column(Integer,primary_key=True)
    location_name = Column(String(25),index=True)
    lat = Column(Float,index=True)
    long = Column(Float,index=True)
    created_at = Column(DateTime)



    