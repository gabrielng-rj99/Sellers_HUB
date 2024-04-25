import os, sys
from decimal import Decimal

from directories import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.src.app.models import *

# Create the engine to connect to the database, and a sessionmaker bound to the engine
global Session, Engine
Engine = create_engine(f'sqlite:///{db_path}') 
Session = sessionmaker(bind=Engine)

def add_client(first_name: str, last_name: str, cpf: str, phone: str,
    email: str, address: str, birth_date: str, additional_info: str) -> None:
    
    client = Client(
        first_name  = first_name,
        last_name   = last_name,
        client_CPF  = cpf,
        phone_number= phone,
        email = email,
        physical_address = address,
        birthday = birth_date,
        additional_information = additional_info
    )
    
    with Session() as session:
        session.add(client)
        session.commit()
        print(f'Client {client.client_ID} added successfully!')
    
def add_new_company(owner_id: int, name: str, client_id: int) -> None:

    company = Company(owner_id      = owner_id,
                          name      = name,
                          client_id = client_id)
    
    with Session() as session:
        session.add(company)
        session.commit()
        print(f'Company {company.company_CNPJ_ID} added successfully!')

def add_new_contract(contract_type: str, administrator: str, operator: str,
    contract_plan: str, data_inicio: str, data_fim: str,
    valor_contrato: Decimal, client_ID: int) -> None:

    contract = Contract(contract_type  = contract_type,
                            administrator  = administrator,
                            operator       = operator,
                            contract_plan  = contract_plan,
                            data_inicio    = data_inicio,
                            data_fim       = data_fim,
                            valor_contrato = valor_contrato,
                            client_ID      = client_ID)
    
    with Session() as session:
        session.add(contract)
        session.commit()
        print(f'Contract {contract.contract_id} added successfully!')
        
def add_new_transaction(first_pay_value: Decimal, extra_pay_value: Decimal,
                        transaction_date: str, client_ID: int) -> None:
    
    transaction = Transaction(first_pay_value = first_pay_value,
                            extra_pay_value = extra_pay_value,
                            transaction_date = transaction_date,
                            client_ID = client_ID)
    
    with Session() as session:
        session.add(transaction)
        session.commit()
        print(f'Transaction {transaction.transaction_id} added successfully!')

def add_new_agenda_event(date_hour: str, description: str, client_ID: int) -> None:

    agenda_event = Agenda(date_hour = date_hour, #'2022-01-01 10:00:00'
                       description  = description,
                       client_ID    = client_ID)
    
    with Session() as session:
        session.add(agenda_event)
        session.commit()
        print(f'Event {agenda_event.event_id} added successfully!')

