price_under_18 = 0
price_from_18_to_25 = 990
price_from_25 = 1390
sum_of_order = 0
discount = 10

while True:
    try:
        number_of_tickets = int(input("Введите количество билетов: "))
        if 1 <= number_of_tickets <= 10:
            break
        elif number_of_tickets < 1:
            print("Количество не может быть отрицательным или равняться 0")
            continue
        elif number_of_tickets > 10:
            print("За раз можно купить не более 10 билетов")
            continue
    except ValueError as e:
        print("Введите цифру от 1 до 10")

for ticket in range(1, number_of_tickets + 1):
    while True:
        try:
            age = int(input(f"Введите возраст участника для билета {ticket}: "))
            if age <= 0:
                print("Возраст не может быть отрицательным или равняться 0")
                continue
            elif 1 <= age <= 17:
                sum_of_order += price_under_18
                break
            elif 18 <= age <= 25:
                sum_of_order += price_from_18_to_25
                break
            elif age > 25:
                sum_of_order += price_from_25
                break
        except ValueError as e:
            print("Введите возраст цифрами")

if number_of_tickets > 3:
    sum_of_order = sum_of_order - sum_of_order*discount//100
    print(f"Количество билетов: {number_of_tickets}. Скидка: {discount}%. Сумма к оплате: {sum_of_order}")
else:
    print(f"Количество билетов: {number_of_tickets}. Сумма к оплате: {sum_of_order}")
