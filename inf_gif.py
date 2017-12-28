import argparse

import matplotlib
matplotlib.use('Agg')
from pylab import *
from skimage import data
from skimage.viewer.canvastools import RectangleTool
from skimage.viewer import ImageViewer

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

# Read Image
image = misc.imread(args.image_path)
images = [image]
imsize = image.shape

# User input for recursive ROI
def get_rect_coord(extents):
    global viewer,coord_list,selecting
    coord_list.append(extents)
    selecting=False
    viewer.close()

def get_ROI(im):
    global viewer,coord_list,selecting

    selecting=True
    finished=False
    while selecting:
        viewer = ImageViewer(im)
	coord_list = []
        rect_tool = RectangleTool(viewer, on_enter=get_rect_coord)
	viewer.show()
    return coord_list

coords=get_ROI(image)[0]

# Organize image parameters
n = args.n
split = (n+2)*2

y1 = coords[2]
y2 = coords[3]
x1 = coords[0]
x2 = coords[1]

ymax = imsize[0]
xmax = imsize[1]

# Generate images
for i in range(n):
    y1_new = int(y1*(i+1)/split)
    y2_new = int(ymax-(ymax-y2)*(i+1)/split)
    x1_new = int(x1*(i+1)/split)
    x2_new = int(xmax-(xmax-x2)*(i+1)/split)
    image = misc.imresize(image[y1_new:y2_new,x1_new:x2_new,:],imsize)

    images.append(image)

imageio.mimsave(args.output_path, images)
