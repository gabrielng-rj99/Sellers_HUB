CREATE TABLE clients (
  client_ID INTEGER PRIMARY KEY,
  client_CPF INTEGER,
  first_name VARCHAR NOT NULL,
  last_name VARCHAR,
  phone_number INTEGER,
  email VARCHAR,
  birthday DATETIME,
  physical_address VARCHAR,
  additional_information VARCHAR
);

CREATE TABLE company (
  company_CNPJ_ID INTEGER PRIMARY KEY,
  company_owner INTEGER NOT NULL,
  company_name VARCHAR NOT NULL,
  FOREIGN KEY (company_owner) REFERENCES clients(client_ID)
);

CREATE TABLE contracts (
  contract_id INTEGER PRIMARY KEY,
  contract_type VARCHAR NOT NULL,
  administrator VARCHAR,
  operator VARCHAR,
  contract_plan VARCHAR NOT NULL,
  data_inicio DATETIME,
  data_fim DATETIME,
  valor_contrato DECIMAL(10,2),
  client_ID INTEGER NOT NULL,
  FOREIGN KEY (client_ID) REFERENCES clients(client_ID)
);

CREATE TABLE transaction (
  transaction_id INTEGER PRIMARY KEY,
  first_pay_value DECIMAL(10,2) NOT NULL,
  extra_pay_value DECIMAL(10,2),
  transaction_date DATETIME NOT NULL,
  client_ID INTEGER NOT NULL,
  FOREIGN KEY (client_ID) REFERENCES clients(client_ID)
);

CREATE TABLE agenda (
  event_id INTEGER PRIMARY KEY,
  client_ID INTEGER NOT NULL,
  date_hour DATETIME NOT NULL,
  description TEXT,
  FOREIGN KEY (client_ID) REFERENCES clients(client_ID)
);