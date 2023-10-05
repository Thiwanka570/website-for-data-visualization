from django.shortcuts import render, HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import os

def uploadDataset():
    pass

file_path = os.path.join(".", "myapp", "dataset", "sample.csv")
try:
    dataset = pd.read_csv(file_path)
    column_names=dataset.columns
    column_namelist=dataset.columns.to_list()   
except FileNotFoundError:
    print( "CSV file not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")


def read_columns(data):
    columnNames=data.columns
    return columnNames
    
def genarate_Graps(columns,dataset):
    x_column=columns[1]
    y_column=columns[2]
    
    x_data=dataset[x_column]
    y_data=dataset[y_column]
    
    plt.plot(x_data, y_data)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Plot of {x_column} vs. {y_column}')
    plt.grid(True)
    
    plt.savefig('sample1.jpg')
    
genarate_Graps(column_namelist,dataset)

def home(request):
    columnNames = read_columns(dataset)
    return render(request,'home.html',{'columns':columnNames})
