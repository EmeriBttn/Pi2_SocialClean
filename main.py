import pandas as pd
from urlextract import URLExtract
import re
import emoji


def Input():
  df=pd.read_csv('/Users/emericbuttin/Desktop/S07/PI2/tweets_final2021-11-29.csv')
  #print(df['text'].iloc[5])
  df2=df.rename(columns={"url":"url du tweet","text":"tweet"})
  return df2



def testhashtag(text,char):
  text=text+' '
  listhashtag=[]
  for i in range(len(text)):
    if text[i] ==char:
      k=i+1
      mot=''
      while text[k] not in [' ','#',',','.','!','?','@']:
        mot=mot+text[k]
        k=k+1
      listhashtag.append(mot)
  for mot in listhashtag:
    row['tweet_txt'] = row['tweet_txt'].replace(mot, '')
    row['tweet_txt'] = row['tweet_txt'].replace(char, '')

  return listhashtag

def Liens(texte):
  extractor = URLExtract()
  urls = extractor.find_urls(texte)
  return urls
def Liens2(texte):
  regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
  listurl = re.findall(regex, texte)
  for mot in listurl:
    row['tweet_txt'] = row['tweet_txt'].replace(mot, '')

  return listurl


def testemoji(text):
  listemoji=[]
  for i in text:
    if emoji.is_emoji(i):
      listemoji.append(i)
  for em in listemoji:
      text2=text.replace(em,' ')
  return listemoji


if __name__ == '__main__':
  df=Input()
  df['tweet_txt']=df['tweet']
  liste_hashtag=[]
  liste_arobase=[]
  liste_liens=[]
  liste_emoji=[]

  for index, row in df.iterrows():
    row['tweet_txt']=row['tweet_txt'].replace('\n',' ')
    liste_hashtag.append(testhashtag(row['tweet_txt'],'#'))
    liste_arobase.append(testhashtag(row['tweet_txt'],'@'))
    liste_liens.append(Liens2(row['tweet_txt']))
    liste_emoji.append(testemoji(row['tweet_txt']))


  df['Hashtag']=liste_hashtag
  df['Citation (@)']=liste_arobase
  df['Liens Externes']=liste_liens
  df['Emojis'] = liste_emoji
  #print(df['tweet'])
  #print(df['tweet'].iloc[5])



