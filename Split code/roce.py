import os
directory = os.fsencode(r"C:\Users\Ishara\Desktop\New folder\flowers\rose")
numPics = 0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(r"C:/Users/Ishara/Desktop/New folder/flowers/rose/" + filename)
     if filename.endswith(".jpg"): 
         numPics +=1
         if numPics % 4 == 0: #put in testing
            
            os.replace(r"C:/Users/Ishara/Desktop/New folder/flowers/rose/" + filename, r"C:/Users/Ishara/Desktop/New folder/dataset/testing/rose/" + filename)
         else:#put in training
            os.replace(r"C:/Users/Ishara/Desktop/New folder/flowers/rose/" + filename, r"C:/Users/Ishara/Desktop/New folder/dataset/training/rose/" + filename)

         continue
     else:
         continue