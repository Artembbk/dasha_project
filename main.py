import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from torch import nn
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt # Visualization 
import matplotlib.dates as mdates # Formatting dates
import seaborn as sns # Visualization
from sklearn.preprocessing import MinMaxScaler
import torch # Library for implementing Deep Neural Network 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from dasha_project.utils import *

def main():
    company = "YNDX"
    data = read_data()
    data = get_company_data(data, company)
    train_data, test_data = split_train_test_data(data)
    X_train, y_train, X_test, y_test, scaler = get_Xy_train_test(train_data, test_data, company)
    train(X_train, y_train, X_test, y_test, company)
    PATH = f"{company}_model.path"
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    input_size = 1
    num_layers = 2
    hidden_size = 64
    output_size = 1
    model = LSTMModel(input_size, hidden_size, num_layers).to(device)
    model.load_state_dict(torch.load(PATH))
    model.eval()
    predcit(model, test_data, X_test, scaler)

if __name__ == '__main__':
    main()