class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        
        total_sum = 0
        reversed_card = self.card_num[::-1]
        for i in range(len(reversed_card)):
            digit = reversed_card[i]
            if i % 2 == 1:
                double_of_digit = 2 * int(digit)
                total_sum += double_of_digit if double_of_digit < 10 else (double_of_digit - 9)
            else:
                total_sum += int(digit)
                
        return (total_sum % 10) == 0
# x ="1 2345 6789 1234 5678 9013"
# y = reversed(x)
# print(y)

l1 = Luhn("59")
print(l1.valid())
# print(l1.valid())