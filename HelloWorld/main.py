#\\\\\\\\\\\priprava pole pro operace s cisly\\\\\\\\\\\\\\\\\\

#ziska cisla od uzivatele
def getNumbers():
    #string_of_numbers = input("Zadej čísla pro seřazení (oddělená čárkou): ")
    string_of_numbers = "5,17,-3, 9,1,15, 13,1 "
    return string_of_numbers

#rozdeli retezec podle separatoru a ulozi do listu retezcu
#oseka mezery, prevede polozky na int
def prepareNumbersToSort(string_of_numbers):
    numbers = string_of_numbers.split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].strip())
    return numbers

#\\\\\\\\\\\\\\\\\\\\\\\priprava na vypis\\\\\\\\\\\\\\\
#prevede na retezec cisel oddelenych carkou
def NumbersToPrint(numbers):
    for i in range(len(numbers)):
      numbers[i] = str(numbers[i])
    numbers_to_print = ", ".join(numbers)
    return numbers_to_print

#\\\\\\\\\\\\\\\\\\\\\\kody pro razeni\\\\\\\\\\\\\\

#najde index nejmensiho prvku v cely zbyvajici nesetrideny casti seznamu
#jako nejmensi se oznaci nejdriv ten prvni nesetrideny [first_unsorted]
# a porovnava se s vedlejsim prvkem [first_unsorted +1]
def findTheSmallestNumber(numbers, first_unsorted):
    for i in range(first_unsorted + 1, len(numbers)):
        if  numbers[i] < numbers[first_unsorted]:
            minimum = i
            first_unsorted = i     # nastavi novy nejmensi prvek
        else:
            minimum = first_unsorted
    return minimum

#prohodí dvě čísla:
#nejmensi cislo presune na prvni misto v nesetridene casti seznamu
#nahrazene číslo da na puvodni pozici nejmensiho
def swapTwoNumbers(numbers, first_unsorted, minimum):
    if minimum != first_unsorted:       #pokud ten nejmensi neni prvni nesetrideny = uz na spravne pozici
        tmp = numbers[first_unsorted]
        numbers[first_unsorted] = numbers[minimum]
        numbers[minimum] = tmp
    return first_unsorted + 1

#setridi cely seznam prohozenim prvku
def sortNumbersBySwapping(numbers, first_unsorted):
    while first_unsorted < len(numbers)-1:
        minimum = findTheSmallestNumber(numbers,first_unsorted)
        first_unsorted = swapTwoNumbers(numbers, first_unsorted, minimum)


#\\\\\\\\\\\\\---hlavni funkce---\\\\\\\\\\

#ziska a upravi seznam cisel pro numericke operace
#setridi seznam cisel od nejmensiho
#upravi setridený seznam cisel k tisku a vytiskne
def selectionSort():
    numbers = prepareNumbersToSort(getNumbers())
    sortNumbersBySwapping(numbers, first_unsorted=0)
    print("Výsledek řazení:\n" + NumbersToPrint(numbers))


#----------------zacatek programu--------------------------------

selectionSort()



