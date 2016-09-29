import bs4,requests,os,sys

images='one-piece'

os.makedirs('./desktop/'+images,exist_ok=True)
os.chdir('./desktop/'+images)

for i in range (0,30):

    try:
        a = str(i).zfill(3)
        url='http://h.mfcdn.net/store/manga/106/TBD-841.0/compressed/c' + a + '.jpg'
        print(url)
        res=requests.get(url)

        f=open('pic_'+str(i+1)+'.jpeg','wb')

        for chunk in res.iter_content(100000):
            f.write(chunk)p
            f.close()

    except:
        print ('Done')
