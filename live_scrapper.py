import pandas as pd

df = pd.DataFrame()
categories = ['Abrasives', 'aerospace_defence', ...]  # 180+ Categories
for category in categories:

    raw_data = pd.read_html(
        "https://www.moneycontrol.com/stocks/marketstats/industry-classification/bse/{0}.html".format(category))

    df_temp = raw_data[0]  # list to dataframe
    df_temp[['Company', 'others']] = df_temp['Company Name'].str.split(
        r"\bAdd\b", expand=True)
    df_temp['Company Name'] = df_temp['Company']
    df_temp = df_temp.iloc[::7, :7:]
    df_temp['Category'] = category
    # print(df_temp)
    df = pd.concat([df, df_temp], axis=0)

print(df.head())
