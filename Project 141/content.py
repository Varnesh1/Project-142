from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df.columns = ['timestamp',	'eventType','contentId','	personId', 'sessionId', 'userAgent', 'userRegion','userCountry']
df.head(1)
view = 0
like = 0
bookmark = 0
follow = 0
comment_created = 0
for o in df1.columns:
  if o == 'timestamp':
    view+=1
  if o == 'eventType':
    like+=1
  if o == 'personId':
    bookmark+=1
  if o == 'sessionId':
    follow+=1
  if o == 'userAgent':
    comment_created+=1
print(view, like, bookmark, follow, comment_created)