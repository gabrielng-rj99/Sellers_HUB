import sqlite3, unicodedata, re, phonenumbers
from validate_email import validate_email, validate_email_or_fail
from phonenumbers import PhoneNumberType
from datetime import datetime

VALID_LETTERS      = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALID_NUMBERS      = "0123456789"
VALID_PUNCTUATIONS = "'\",.:;?°/!@#$%&*|-_=+[]}\{()ªº"
ALL_VALID_CHARS    = VALID_LETTERS + VALID_NUMBERS + VALID_PUNCTUATIONS
INVALID_ACCENTS    = "¨´`^~"


def normalize(str_input) -> str:
    nfkd_form = unicodedata.normalize('NFKD', str_input)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Functions for data validation
def is_valid_text(text_input:str) -> bool:
    normalized_input = normalize(text_input)
    for char in normalized_input:
        if char not in ALL_VALID_CHARS:
            return False
    return True

def is_valid_mobile(num_input:tuple[str]) -> bool:   # (55,21,999999999)
    for i in range(len(num_input)):
        try:
            int(num_input[i])
        except:
            print(num_input[i], i)
            return False, False
    
    num_input = "".join(num_input)
    num_input = "+"+num_input
    phone_number = phonenumbers.parse(num_input)
    is_valid = phonenumbers.is_possible_number(phone_number)
    is_mobile = True if phonenumbers.number_type(phone_number) == PhoneNumberType.MOBILE else False
    
    return is_valid, is_mobile

def is_valid_datetime(date_string):
    try:
        datetime.strptime(date_string, '%m-%d-%Y %H:%M')
        return True
    except:
        return False

def is_valid_email(email_input:str) -> bool:    # Format
    is_valid = validate_email(
        email_address= email_input,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        smtp_helo_host='my.host.name',
        smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False)
    return is_valid
    
def is_valid_adress(adress_input:str) -> bool:
    return is_valid_text(adress_input)

def is_valid_cpf(cpf: str) -> bool:
    """
    Validates a CPF number, checking both formatting and verification digits.

    Args:
        cpf (str): The CPF number to be validated.

    Returns:
        bool:
            - False when the CPF does not have the 999.999.999-99 format;
            - False when the CPF does not have 11 numeric digits;
            - False when the verification digits are invalid;
            - True in any other case.

    Examples:
        >>> is_valid_cpf('529.982.247-25')
        True
        >>> is_valid_cpf('52998224725')
        False
        >>> is_valid_cpf('111.111.111-11')
        False
    """

    # Checks the CPF formatting
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtains only the numbers from the CPF, ignoring punctuation
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Checks if the CPF has 11 numbers or if they are all equal:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validates the first verification digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validates the second verification digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def is_valid_cnpj(cnpj: str) -> bool:
    # Checks the CNPJ formatting
    if not re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj):
        return False

    # Obtains only the numbers from the CNPJ, ignoring punctuation
    numbers = [int(digit) for digit in cnpj if digit.isdigit()]

    # Checks if the CNPJ has 14 numbers or if they are all equal:
    if len(numbers) != 14 or len(set(numbers)) == 1:
        return False

    # Calculates the first verification digit:
    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(a*b for a, b in zip(numbers[0:12], weights))
    expected_digit = 11 - (sum_of_products % 11)
    if expected_digit > 9:
        expected_digit = 0
    if numbers[12] != expected_digit:
        return False

    # Calculates the second verification digit:
    weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(a*b for a, b in zip(numbers[0:13], weights))
    expected_digit = 11 - (sum_of_products % 11)
    if expected_digit > 9:
        expected_digit = 0
    if numbers[13] != expected_digit:
        return False

    return True



# Functions for treat data
def treat_number(num_input:tuple[str]) -> str:       # (55,21,999999999)
    num = "".join(num_input)
    return int(num)


def test():
    nome1 = "Márcia dos Santos Espíndola"
    nome2 = "Márci@ d0s S4ntos Espí1ndol4"
    nome3 = "Márci@ d0s¨¨ S4ntos Espí1ndol4"

    print(normalize(nome1))
    print(is_valid_text(nome1))
    print(normalize(nome2))
    print(is_valid_text(nome2))
    print(normalize(nome3))
    print(is_valid_text(nome3))
    print(is_valid_mobile(("55","21","999999999")))
    print(treat_number(("55","21","999999999")))
    print(is_valid_cpf("529.982.247-25"))
    print("cnpj")
    print(is_valid_cnpj("29.309.127/0122-66"))
    print(is_valid_cnpj("29.309.127/0001-79"))
    print(is_valid_cnpj("59.104.760/0011-63"))
    print("email")
    print(is_valid_email("a2@a.com.br"))
    print(is_valid_email("aa@a.com"))
    print(is_valid_email("a2@a"))
    print(is_valid_email("aaaa@gmail.com"))
    print(is_valid_email("aa.aa@gmail.com"))
    print(is_valid_email("aa.a.aa.a.a.aa@gmail.com"))
    print(is_valid_email("aa.a.aa.a.a.aa.@gmail.com"))
    print(is_valid_email(".aa.a.aa.a.a.aa@gmail.com"))
    print(is_valid_email("gabriel.12.07.ng@gmail.com"))
    print(is_valid_email("nerdguinho0709@gmail.com"))

test()