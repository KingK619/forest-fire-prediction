import torch
import jovian
import torchvision
import torch.nn as nn

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import torch.nn.functional as F
from torchvision.datasets.utils import download_url
from torch.utils.data import DataLoader, TensorDataset, random_split
%matplotlib inline

project_name='forest-fires-regression-prediction' # will be used by jovian.commit