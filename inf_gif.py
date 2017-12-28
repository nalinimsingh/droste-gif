import argparse
from scipy import misc
import imageio

# Process arguments
parser = argparse.ArgumentParser(description='Generate a gif that loops into itself when played on repeat.')
parser.add_argument('image_path', help='path to input image')
parser.add_argument('output_path', help='path to output gif')
parser.add_argument('-n', '--num-frames', type=int,
                    dest='n', help='number of intermediate frames in gif',
                    default=8)
args = parser.parse_args()

image = misc.imread(args.image_path)
images = [image]

imsize = image.shape
n = args.n
split = (n+2)*2

y1 = 124
y2 = 292
x1 = 872
x2 = 1072

ymax = imsize[0]
xmax = imsize[1]


for i in range(n):

    y1_new = int(y1*(i+1)/split)
    y2_new = int(ymax-(ymax-y2)*(i+1)/split)
    x1_new = int(x1*(i+1)/split)
    x2_new = int(xmax-(xmax-x2)*(i+1)/split)

    image = misc.imresize(image[y1_new:y2_new,x1_new:x2_new,:],imsize)

    images.append(image)

imageio.mimsave(args.output_path, images)
