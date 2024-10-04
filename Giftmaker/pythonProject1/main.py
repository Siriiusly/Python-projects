import imageio.v3 as iio

file_names=['0.jpg',"1.jpg","2.jpg","4.jpg","5.jpg"]
images=[]

for file_name in file_names:
    images.append(iio.imread(file_name))

iio.imwrite('finger.gif',images,duration=500,loop=0)