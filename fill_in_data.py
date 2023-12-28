import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from main import Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:postgres@localhost:5432/netology_hw"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

