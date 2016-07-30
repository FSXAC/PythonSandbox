list_even = []
list_names = []

def createEvenList(list_input):
    for i in range(0, 10, 2):
        list_input.append(i)
    return list_input

def createName(list_input):
    for i in range(5):
        list_input.append(str(input("Enter a name: ")))
    return list_input

list_even = createEvenList(list_even)
list_names = createName(list_names)

print(list_even)
print(list_names)

