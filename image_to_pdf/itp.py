import img2pdf
from os import walk
import os
from PIL import Image

pdflist=[]
for (dirpath, dirname, filename ) in walk ('imgsrc'):
    pdflist.extend(filename)
    break
os.chdir('imgsrc')
print(pdflist)
jpg2000list=[]
for i in pdflist:
    if i[-3:]=='jpg' or i[-3:]=='JPG':
        jpg2000list.append(i)
jpg2000list.sort()
with open("HW2 Pengzhou_He.pdf","wb") as f:
    f.write(img2pdf.convert(jpg2000list))

'''
#pdflist=['1.jpg', '2.jpg']
pdflist=[]
for (dirpath, dirname, filename ) in walk ('imgsrc'):
    pdflist.extend(filename)
    break
os.chdir('imgsrc')

jpg2000list=[]
for i in pdflist:
    if i.find('JPG')!=-1:
        jpg2000list.append(i)

for i in jpg2000list:
    im=Image.open(i)
    im.convert('RGBA').save(i,'JPEG2000',quality_mode='dB')


with open("ECE-8455 - Pengzhou He.pdf","wb") as f:
    f.write(img2pdf.convert(jpg2000list))
    '''