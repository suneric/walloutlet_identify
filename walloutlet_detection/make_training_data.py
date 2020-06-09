import numpy as np
import os
import sys

def create_data(data, file_type):
    print(data)
    if not os.path.exists(data):
        print(data, 'is not existed')

    print(file_type)
    if file_type == 'pos':
        for img in os.listdir(data):
            line = file_type+'/'+img+' 1 0 0 50 50\n'
            with open('info.data', 'a') as f:
                f.write(line)

    elif file_type == 'neg':
        for img in os.listdir(data):
            line = file_type+'/'+img+'\n'
            with open('bg.txt','a') as f:
                f.write(line)

if __name__ == '__main__':
    data = sys.argv[1]
    file_type = sys.argv[2]
    create_data(data, file_type)
