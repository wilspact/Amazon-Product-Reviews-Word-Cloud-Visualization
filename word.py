import pandas as pd 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
df=pd.read_csv("C:\\Users\\Lenovo\\Desktop\\dataset\\project\\wordcloud\\Amazon_Reviews.csv",encoding='utf-8',on_bad_lines='skip',engine='python')
text=" ".join(review for review in df['Reviewer Name'])
import re
text = re.sub(r'[^\w\s]', '', text) 
wc=WordCloud(width=800,height=400,background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("wordcloud.png")
