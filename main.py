import requests


def run():
    print('')

    data = {"message_date": "10.12.2023",
            "sender_phone": "+7 382 279 87 41",
            "sender_email": "bla@gmail.com",
            "message_text": "Test good form"}

    print('1. Запрос с подходящей формой.'
          ' В ответе ожидается имя подходящего шаблона.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "user_number": "+7 382 279 87 41",
            "user_email": "bla@gmail.com",
            "user_text": "Hello"}
    print('2. Запрос с не подходящей формой.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"da_of_burn": "10.12.1998",
            "user_number": "+7 382 279 87 41",
            "user_email": "bla@gmail.com",
            "user_text": "Hello"}
    print('3.1 Запрос с не подходящим ключом одного из полей.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "ur_number": "+7 382 279 87 41",
            "user_email": "bla@gmail.com",
            "user_text": "Hello"}
    print('3.2 Запрос с не подходящим ключом одного из полей.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "user_number": "+7 382 279 87 41",
            "user_ail": "bla@gmail.com",
            "user_text": "Hello"}
    print('3.3 Запрос с не подходящим ключом одного из полей. '
          'В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "user_number": "+7 382 279 87 41",
            "user_email": "bla@gmail.com",
            "user_xt": "Hello"}
    print('3.4 Запрос с не подходящим ключом одного из полей. '
          'В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.19918",
            "user_number": "+7 382 279 87 41",
            "user_email": "bla@gmail.com",
            "user_text": "Hello"}
    print('4.1 Запрос с не подходящим типом одного из полей.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "user_number": "+7 382 279 878 41",
            "user_email": "bla@gmail.com",
            "user_text": "Hello"}
    print('4.2 Запрос с не подходящим типом одного из полей.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')

    data = {"date_of_burn": "10.12.1998",
            "user_number": "+7 382 279 87 41",
            "user_email": "bla_gmail.com",
            "user_text": "Hello"}
    print('4.3 Запрос с не подходящим типом одного из полей.'
          ' В ответе ожидается форма, где значения полей - это их тип.')
    print(f'Входные данные: {data}')
    response = requests.post("http://127.0.0.1:8000/get_form/", data)
    print(f'Выходные данные: {response.text}')
    print('---------------------------')
    print('')


if __name__ == '__main__':
    run()
