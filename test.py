print('Артыкова Наргиза вт 15:25')

age = int(input('age = '))
if age < 10:          #10-нан кіші немесе тең болса
    price = 800
elif 10 <= age < 18:   #10-нан үлкен және 18-ден кіші болса
    price = 1100
else:                  #басқа жаста болса
    price = 1500

print('price = ', price)
