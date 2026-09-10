fruits=["Apples","Mangoes","Banana","Pears","Oranges"]
try:

    index=int(input("Enter an index that you want to access"))
    print(fruits[index])
except IndexError:
    print("Given index number is not present in this list")
