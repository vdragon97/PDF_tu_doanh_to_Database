# import required libraries
import numpy as gfg
import matplotlib.image as img
 
# read an image
imageMat = img.imread('C:/Users/LONG.PV/Desktop/PDF_tu_doanh_to_Database/img_folder/test/Out2.jpg')
print("Image shape:", imageMat.shape)
 
# if image is colored (RGB)
if(imageMat.shape[2] == 3):
   
  # reshape it from 3D matrice to 2D matrice
  imageMat_reshape = imageMat.reshape(imageMat.shape[0],
                                      -1)
  print("Reshaping to 2D array:",
        imageMat_reshape.shape)
 
# if image is grayscale
else:
  # remain as it is
  imageMat_reshape = imageMat
     
# saving matrice to .csv file
gfg.savetxt('geek.csv',
            imageMat_reshape)
 
# retrieving matrice from the .csv file
loaded_2D_mat = gfg.loadtxt('geek.csv')
 
# reshaping it to 3D matrice
loaded_mat = loaded_2D_mat.reshape(loaded_2D_mat.shape[0],
                                   loaded_2D_mat.shape[1] // imageMat.shape[2],
                                   imageMat.shape[2])
 
print("Image shape of loaded Image:",
      loaded_mat.shape)
 
# check if both matrice have same shape or not
if((imageMat == loaded_mat).all()):
   
  print("\n\nYes",
        "The loaded matrice from CSV file is same as original image matrice")