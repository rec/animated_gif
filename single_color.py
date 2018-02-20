#!/usr/bin/env python3

import imageio, PIL.Image, os, sys

def add(color, filename):
    PIL.Image.new('RGB', (64, 64), color).save(filename)
    frames.append(filename)


frames = []

# Create five frames
add((0, 0, 0), 'black.gif')
add((255, 0, 0), 'red.gif')
add((0, 255, 0), 'green.gif')
add((0, 0, 255), 'blue.gif')
add((255, 255, 255), 'white.gif')

# Use PIL to write the animated GIF.
# This GIF is *right*: the expected five-frame RGB GIF.
images = [PIL.Image.open(f) for f in frames]
image = images.pop(0)
image.save('pil.gif', save_all=True, append_images=images)

# Use imageio to write the animated GIF.
# See https://stackoverflow.com/a/35943809/43839
# This GIF is *wrong*: the red, green and blue frames are shades of gray.
images = [imageio.imread(f) for f in frames]
imageio.mimsave('simple.gif', images)

# Alternate method: use imageio.get_writer.
# This GIF is also grayscale and *wrong*.
with imageio.get_writer('writer.gif', mode='I') as writer:
    for f in frames:
        writer.append_data(imageio.imread(f))
