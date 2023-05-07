import os
import sys
import pandas as pd

class read_data:
    def __init__(self,file_path):
        self.path = file_path

    def data_reading_initiated(self):
        return pd.read_csv(os.path.join(os.getcwd(),self.path))


