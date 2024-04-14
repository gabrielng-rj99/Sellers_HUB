CREATE TABLE clients (
  client_CPF_ID INTEGER PRIMARY KEY,
  first_name VARCHAR NOT NULL,
  last_name VARCHAR,
  phone_number INTEGER,
  email VARCHAR,
);

CREATE TABLE company (
  company_CNPJ_ID INTEGER PRIMARY KEY,
  company_owner INTEGER NOT NULL,
  FOREIGN KEY (company_owner) REFERENCES clients(client_CPF_ID)
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
  client_CPF_ID INTEGER NOT NULL,
  FOREIGN KEY (client_CPF_ID) REFERENCES clients(client_CPF_ID)
);

CREATE TABLE transaction (
  transaction_id INTEGER PRIMARY KEY,
  first_pay_value DECIMAL(10,2) NOT NULL,
  extra_pay_value DECIMAL(10,2),
  client_CPF_ID INTEGER NOT NULL,
  FOREIGN KEY (client_CPF_ID) REFERENCES clients(client_CPF_ID)
);
