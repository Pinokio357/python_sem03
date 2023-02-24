


dict_bonus ={1: ["a", "e", "i", "o", "u", "l", "n", "s", "t", "r", "а", "в", "е", "и", "н", "о", "р", "с", "т"],
         2: ["d", "g", "д", "к", "л", "м", "п", "у"],
         3: ["b", "c", "m", "p", "б", "г", "ё", "ь", "я"],
         4: ["f", "h", "v", "w", "y", "й", "ы"],
         5: ["k", "ж", "з", "х", "ц", "ч"],
         8: ["j", "x", "ш", "э", "ю"],
         10: ["q", "z", "ф", "щ", "ъ" ]}

word = input("enter word: ")
bonus_sum = 0
for i in word:
    for bonus in dict_bonus:
        for letter in dict_bonus[bonus]:
            if letter == i:
                bonus_sum += bonus

print(f"point count = {bonus_sum}")



