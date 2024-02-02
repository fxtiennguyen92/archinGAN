import cv2
import numpy as np

def combineAB(path_A, path_B, path_AB):
        """Combine images at `path_A` and `path_B` into new image at `path_AB`
            from: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/datasets/combine_A_and_B.py#L8
        """
        im_A = cv2.imread(path_A, 1)
        im_B = cv2.imread(path_B, 1)
        im_AB = np.concatenate([im_A, im_B], 1)
        cv2.imwrite(path_AB, im_AB)

input_url = "_mir_-1-inputs.png"
output_url = "_mir_-1-outputs.png"
base_dir = "room_layouts"
ifrom = 139
ito = 169

# input_url = "-input.png"
# output_url = "-targets.png"
# base_dir = "footprints"
# ifrom = 501
# ito = 600


for i in range(ifrom, ito):
    pa = base_dir + "/inputs/" +  str(i) + input_url
    pb = base_dir + "/outputs/" +  str(i) + output_url
    pab = base_dir + "/combine/" + str(i) + '.png'
    combineAB(pa, pb, pab)