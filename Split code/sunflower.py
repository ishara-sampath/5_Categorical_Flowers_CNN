import os
directory = os.fsencode(r"C:\Users\Ishara\Desktop\New folder\flowers\sunflower")
numPics = 0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(r"C:/Users/Ishara/Desktop/New folder/flowers/sunflower/" + filename)
     if filename.endswith(".jpg"): 
         numPics +=1
         if numPics % 4 == 0: #put in testing
            
            os.replace(r"C:/Users/Ishara/Desktop/New folder/flowers/sunflower/" + filename, r"C:/Users/Ishara/Desktop/New folder/dataset/testing/sunflower/" + filename)
         else:#put in training
            os.replace(r"C:/Users/Ishara/Desktop/New folder/flowers/sunflower/" + filename, r"C:/Users/Ishara/Desktop/New folder/dataset/training/sunflower/" + filename)

         continue
     else:
         continue