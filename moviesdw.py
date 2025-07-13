import pandas as pd
file_path = r'filelocatioon'
pd.set_option('display.max_columns', None)
try:
    # Try reading the CSV with potential ParserError
    header_line = pd.read_csv(file_path, nrows=0, encoding='utf-8').columns.tolist()
    df = pd.read_csv(file_path, header=None, names=header_line, encoding='latin1')

except pd.errors.ParserError as e:
    print(f"ParserError_ Skipping Line details: {e}")
    header_line = pd.read_csv(file_path, nrows=0, encoding='utf-8').columns.tolist()
    df = pd.read_csv(file_path, header=None, names=header_line, on_bad_lines='skip', encoding='latin1')
    print(df)