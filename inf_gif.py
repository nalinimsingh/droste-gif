from scipy import misc
import imageio

image = misc.imread('sciarappa.png')
images = [image]

imsize = image.shape
n = 20

y1 = 124
y2 = 292
x1 = 872
x2 = 1072

ymax = imsize[0]
xmax = imsize[1]


for i in range(n/2-2):

    y1_new = int(y1*(i+1)/n)
    y2_new = int(ymax-(ymax-y2)*(i+1)/n)
    x1_new = int(x1*(i+1)/n)
    x2_new = int(xmax-(xmax-x2)*(i+1)/n)

    image = misc.imresize(image[y1_new:y2_new,x1_new:x2_new,:],imsize)

    images.append(image)

imageio.mimsave('inf_apt.gif', images)
