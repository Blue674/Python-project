import pickle
  
file = open("CouponCode.txt", "wb")
  
my_dict = {"KJ6789":52.0,
           "KJ1234":20.0}

pickle.dump(my_dict, file)
  
file.close()