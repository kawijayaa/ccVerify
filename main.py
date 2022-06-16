import re

def valid_card_type(card_number):
    card_number_string = str(card_number)
    match card_number_string:
        case card_number_string if re.match("^4[0-9]{12}(?:[0-9]{3})?$", card_number_string):
            return "Visa"
        case card_number_string if re.match("^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$", card_number_string):
            return "Mastercard"
        case card_number_string if re.match("^3[47][0-9]{13}$", card_number_string):
            return "American Express"
        case card_number_string if re.match("^3(?:0[0-5]|[68][0-9])[0-9]{11}$", card_number_string):
            return "Diner's Club"
        case card_number_string if re.match("^6(?:011|5[0-9]{2})[0-9]{12}$", card_number_string):
            return "Discover"
        case card_number_string if re.match("^(?:2131|1800|35\d{3})\d{11}$", card_number_string):
            return "JCB"
        case _:
            return False

while True:    
    cc_number = input("Enter Credit Card Number: ")
    cc_number = "".join(cc_number.split())
    try:
        cc_number_test = int(cc_number)
    except:
        print("Not a number")

    even_placed_num = cc_number[-2::-2]
    even_digit_sum = 0
    for x in even_placed_num:
        num = int(x)
        str_multiplied = str(num*2)
        if num*2 >= 10:
            even_digit_sum += int(str_multiplied[0]) + int(str_multiplied[1])
        else:
            even_digit_sum += num*2
        
    odd_placed_num = cc_number[-1::-2]
    odd_digit_sum = 0
    for x in odd_placed_num:
        num = int(x)
        odd_digit_sum += num
        
    cc_number_split = " ".join([cc_number[i:i+4] for i in range(0, len(cc_number), 4)])
    
    verify_num = odd_digit_sum + even_digit_sum
    if verify_num % 10 == 0:
        if valid_card_type(cc_number):
            print(f"{cc_number_split} is a valid {valid_card_type(cc_number)} card number.")
        else:
            print(f"{cc_number_split} is not a valid card number.")
    else:
        if valid_card_type(cc_number_split):
            print(f"{cc_number_split} is not a valid {valid_card_type(cc_number)} card number.")
        else:
            print(f"{cc_number_split} is not a valid card number.")

