import os
from pipeline import ArchiPipeline

stages = (
    'ParcelInputLayer',
    'ParcelOutputLayer',
    'FootprintInputLayer',
    'RepartitionInputLayer',
    'RepartitionOutputLayer',
)
layers = [os.path.join('./dataset/s0_parcel', layer) for layer in stages]
stages = [(j - 1, j) for j in range(1, len(layers))]
stages.pop(1)
directory = './dataset/s2_floorplan'

#print(layers, stages, directory)
pipeline = ArchiPipeline(layers, stages)
pipeline.setup_training(directory)