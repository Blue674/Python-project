import pickle
  
file = open("ProductList.txt", "wb")
  
my_dict = {"CRMS": ['Strawberry Ice Cream',35.0,1.0],
           "CRMC": ['Chocolate Ice Cream',45.0,1.0],
           "CRMV": ['Vanilla Ice Cream',25.0,1.0],
           "PCHP": ['Potato Chips',57.0,1.0],
           "AT":['Gold Wheat Atta',62.0,0.5],
           "BRC":['Basamti Rice',74.0,1.0],
           "VGO":['Vegetable Oil',56.0,0.5],
           "TMT":['Tomato',40.0,1.0],
           "ONI":['Onion',85.0,1.0],
           "MLK":['Cow Milk',14.0,0.5]}
  
pickle.dump(my_dict, file)
  
file.close()

