from sqlalchemy import Column, Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Products(db.Model):
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_no = Column(String(32), nullable=False, unique=True)
    title = Column(String(256), nullable=False)
    img = Column(String(4096), nullable=False, default='')
    qiniu_url = Column(String(256), nullable=False, default='')
    item_type = Column(Integer, nullable=False, default=0)
    org_price = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    old_price = Column(Integer, nullable=False, default=0)
    sale = Column(Integer, nullable=False, default=0)
    status = Column(Boolean, nullable=False, default=1)
