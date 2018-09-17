import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/greg/Dropbox/Machine Learning/data.csv', encoding='utf8')

# # DATA WRANGLING
# # CONVERTING DATE TO DATETIME
# # df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S.%f', utc=True)
# df['datetime'] = df['datetime'].astype('datetime64[ns]')
# #
# # # WORD COUNT
# df['word_count'] = df['text'].str.split().str.len()
# #
# # # CHECKS IF TEXT WAS A LINK
# df['link'] = df['text'].str.contains('http')
# #
# # # CHECKS IF TEXT CONTAINS GIF/IMAGE
# df['media'] = df['text'].str.contains('ð_')
#
# # CHECKS IF TEXT CONTAINS EMOJI
# df['contains_emoji'] = df[(df['text'].str.contains('_')) & (~df['text'].str.contains('ð', na=False))]
#
# df['greg'] = df['is_from_me'] == 1
# df['emily'] = df['is_from_me'] == 0
#
# df.drop_duplicates()
# df.to_csv('wrangled_data.csv', encoding='utf-8', index=False)
print(df['text'])
