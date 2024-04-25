from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Date, Numeric, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy() 

class Client(db.Model):
    client_ID = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50), nullable=False)
    last_name = db.Column(String(50))
    client_CPF = db.Column(Integer)
    phone_number = db.Column(String(20))
    email = db.Column(String(50))
    physical_address = db.Column(String(100))
    birthday = db.Column(Date)
    additional_information = db.Column(Text)

class Company(db.Model):
    company_CNPJ_ID = db.Column(Integer, primary_key=True)
    company_owner = db.Column(Integer, nullable=False)
    company_name = db.Column(String(50), nullable=False)
    client_ID = db.Column(Integer, ForeignKey('client.client_ID'))

class Contract(db.Model):
    contract_id = db.Column(Integer, primary_key=True)
    contract_type = db.Column(String(50), nullable=False)
    administrator = db.Column(String(50))
    operator = db.Column(String(50))
    contract_plan = db.Column(String(50), nullable=False)
    data_inicio = db.Column(DateTime)
    data_fim = db.Column(DateTime)
    valor_contrato = db.Column(Numeric(10, 2))
    client_ID = db.Column(Integer, ForeignKey('client.client_ID'))

class Transaction(db.Model):
    transaction_id = db.Column(Integer, primary_key=True)
    first_pay_value = db.Column(Numeric(10, 2), nullable=False)
    extra_pay_value = db.Column(Numeric(10, 2))
    transaction_date = db.Column(DateTime, nullable=False)
    client_ID = db.Column(Integer, ForeignKey('client.client_ID'))

class Agenda(db.Model):
    event_id = db.Column(Integer, primary_key=True)
    client_ID = db.Column(Integer, ForeignKey('client.client_ID'))
    date_hour = db.Column(DateTime, nullable=False)
    description = db.Column(Text)