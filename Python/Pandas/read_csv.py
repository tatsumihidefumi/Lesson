# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # CSVファイルの読み込み
    df = pd.read_csv("anko.csv")
    # 表示
    print(df)


if __name__ == '__main__':
    main()
