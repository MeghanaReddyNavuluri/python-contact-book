def phone_numb(names,phone_numbers,address,num):
    for i in range(num):
        name = input("Name : ")
        phone_number = int(input("Phone Number : "))
        address_s = input("Address : ")
        names.append(name)
        phone_numbers.append(phone_number)
        address.append(address_s)
    print("\nName\t\t\tPhone Number\t\t\tAddress\n")
    for i in range(num):
        print(f"{names[i]}\t\t\t{phone_numbers[i]}\t\t\t{address[i]}")
    search_term = input("\nEnter search term: ")
    print("search result:")
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        address_s = address[index]
        print(f"Name : {search_term},Phone Number : {phone_number},Address : {address_s}")
    else:
        print("Name Not Found")
names = []
phone_numbers = []
address = []
num= int(input("Enter no.of contacts numbers do u want:"))
phone_numb(names,phone_numbers,address,num)
        
