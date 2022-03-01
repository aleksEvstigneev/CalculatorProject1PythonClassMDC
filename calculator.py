#income tax calculator Aleksandr Evstigneev

grossIncome = float(input('Please, Enter your Gross Income: '))

dependents = int(input('Please, enter number of dependetnts: '))

incomeTax = float(((grossIncome - 10000) - dependents * 3000) * 0.2)
incomeTax = '{:.2f}'.format(incomeTax)
incomeTaxStr = str(incomeTax)

print('Enter the gross income:', '{:.2f}'.format(grossIncome))
print('Enter the number of dependents:', dependents)
print('The income tax is $' + incomeTaxStr)

input('\n\n Press enter key to exit.')
