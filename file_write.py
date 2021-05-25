import pandas as pd

def main():
  url = 'https://raw.githubusercontent.com/phonnapar/my_data/main/database.txt'
  #f_tmp1 = open(url, "r", encoding="utf8")
  #exit()

  df = pd.read_csv(url, error_bad_lines=False)
  print(df)
  exit()
  #print(df.to_string())
  #x = df.itertuples()
  for row in df.itertuples(index=False, name=None):
    for k,v in enumerate(row):
      print("column: {0}".format(df.columns.values[k]))
      print("value: {0}".format(v))
  #print(x)

if __name__ == '__main__':
  main()
