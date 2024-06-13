import requests

def get_exchange_rate():
    # Вставьте сюда ваш API-ключ
    api_key = '96e7021fe3ee43139e6552efe44d5f19'
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

    response = requests.get(url)
    data = response.json()
    return data['rates']['RUB']

def currency_converter():
    rate = get_exchange_rate()
    print(f"Текущий курс доллара к рублю: {rate}")

    amount = float(input("Введите сумму в долларах: "))
    converted_amount = amount * rate
    print(f"Сумма в рублях: {converted_amount}")

    # Новый функционал без изменения существующего кода
    choice = input("Вы хотите конвертировать обратно из рублей в доллары? (да/нет): ").strip().lower()
    if choice == 'да':
        amount_rub = float(input("Введите сумму в рублях: "))
        converted_amount_usd = amount_rub / rate
        print(f"Сумма в долларах: {converted_amount_usd}")

currency_converter()
