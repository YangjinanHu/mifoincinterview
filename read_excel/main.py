import pandas as pd
def read_excel(filename, sheet):
    filepath = "./" + filename
    df = pd.read_excel(filepath, sheet)
    return df



if __name__ == '__main__':
    df = read_excel('SampleData.xlsx', 1)
    print(df)
