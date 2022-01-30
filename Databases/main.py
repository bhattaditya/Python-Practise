import sqlalchemy as db

engine = db.create_engine('sqlite:///mystore.db')
connection = engine.connect()
metadata = db.MetaData()

# user table already exists 
# user = db.Table('User', metadata, autoload=True, autoload_with=engine)

# if user table does not exists then 
user = db.Table('User', metadata, 
        db.Column('ID', db.Integer(), primary_key=True),
        db.Column('FirstName', db.String(20), nullable=False),
        db.Column('LastName', db.String(20)),
        db.Column('Email', db.String(20))
        )

metadata.create_all(engine)

query = user.insert().values(FirstName='Aditya', LastName='Bhatt', Email='bhattaditya2@gmail.com')

connection.execute(query)






