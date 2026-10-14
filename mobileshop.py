# AMITAVA's Mobile Shop

from google import genai
mobiles=[] # A LIST OF LISTS

while True:
    print("\n===== MOBILE SHOP DASHBOARD======\n")
    print("1. Add Mobile")
    print("2. View Mobile")
    print("3. Update Mobile")
    print("4. Delete Mobile")
    print("5. Search Mobile")
    print("6. Sort by Price")
    print("7. Google Gemini AI Chatbot Help")
    print("8. Exit")

    choice=int(input('Enter choice'))

    match choice:
        # CREATE
        case 1:
            name=input("enter mobile name")
            brand=input("enter brand")
            price=int(input("Enter price"))
            mobile=[name,brand,price]
            mobiles.append(mobile)
            print('Mobile added successfully\n')

        # READ
        case 2:

            print("\n Mobile List")
            for _ in mobiles:
                print(_)
        # UPDATE
        case 3:
            name = input("enter mobile name to update")
            for m in mobiles:
                if m[0]==name:
                    m[1]=input("Enter New Brand")
                    m[2]=int(input('Enter new Price'))
                    print('\nUpdation Completed...')

        # DELETE
        case 4:
            name = input("enter mobile name to delete")
            for m in mobiles:
                if m[0]==name:
                    mobiles.remove(m)
                    print('\nDeletion Completed...')

        # Search
        case 5:
            keyword=input("enter search keyword")
            print("\n Results:")
            for m in mobiles:
                if keyword.lower() in m[0].lower():
                    print(m)

        # Sort
        case 6:
            mobiles.sort(key=lambda x:x[2])
            print('Sorted by price')
            for m in mobiles:
                print(m)

        case 7:
            client=genai.Client()
            prompt=input('Ask about any mobile')

            response=client.models.generate_content(
                model='gemini-3.8-flash',
                contents=prompt
            )
            print('\n AI RESPONSE')
            print(response.text)





        # EXIT
        case 8:
            print('exiting ')
            break

        case _:
            print('Invalid Choice')










