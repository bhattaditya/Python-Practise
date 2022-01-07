d1 = {
    "k1": 1000,
    "k2": [10, 20, 30],
    "k3": 2000,
    "k4": 5000,
}
 # This will be string
user_input = input("Enter key: ")

if user_input in d1.keys():
    print("Key already present ...try with another key")
else:
    print("Good to go")  
