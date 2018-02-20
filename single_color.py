#!/usr/bin/env python3

import imageio, PIL.Image, os, sys

filename = 'animated.gif'
root = '/tmp/gif_writer'

frames = 'black.gif', 'red.gif', 'green.gif', 'blue.gif', 'white.gif'

PIL.Image.new('RGB', (64, 64), (0, 0, 0)).save('black.gif')
PIL.Image.new('RGB', (64, 64), (255, 0, 0)).save('red.gif')
PIL.Image.new('RGB', (64, 64), (0, 255, 0)).save('green.gif')
PIL.Image.new('RGB', (64, 64), (0, 0, 255)).save('blue.gif')
PIL.Image.new('RGB', (64, 64), (255, 255, 255)).save('white.gif')

strategy = (sys.argv + ['simple'])[1]

if strategy == 'simple':
    images = [imageio.imread(f) for f in frames]
    imageio.mimsave(filename, images, duration=1)
    # https://stackoverflow.com/a/35943809/43839
    # The resulting animation is incorrectly grayscale

elif strategy == 'write':
    with imageio.get_writer(filename, mode='I', duration=0.5) as writer:
        for f in frames:
            writer.append_data(imageio.imread(f))
    # The resulting animation is incorrectly grayscale

elif strategy == 'pil':
    images = [PIL.Image.open(f) for f in frames]
    image = images.pop(0)
    image.save(filename, save_all=True, append_images=images)
    # The resulting animation is correct

else:
    raise ValueError
