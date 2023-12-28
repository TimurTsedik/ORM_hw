import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from main import Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:postgres@localhost:5432/netology_hw"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

def get_sales_from_publishers(pub_id):
    query = session.query(Book).join(Stock).join(Shop).join(Sale).join(Publisher).filter(Publisher.id == pub_id).all()
    data ={}
    for i in (query):
        book_title = i.title
        data.setdefault(book_title, [])
        for j in i.stocks:
            shop_name = j.shops.name
            for cntr, k in enumerate(j.sales):
                price = k.price
                data[book_title].append({'shop_name': shop_name, 'price': price, 'date_sale': k.date_sale})
    for book in data.keys():
        title = book
        for i in data[title]:
            shop_name = i['shop_name']
            price = i['price']
            date_sale = i['date_sale']
            print(title.ljust(40) + '|' + shop_name.ljust(30) + '|' + str(price).ljust(10) + '|' + (date_sale).strftime('%m/%d/%Y').ljust(30))

print(get_sales_from_publishers(1))