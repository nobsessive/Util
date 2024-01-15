from PyPDF2 import PdfFileMerger
import os

foldername="pdfsrc"
filelist=[]
for (dirpath, dirname, filename ) in os.walk (foldername):
    filelist.extend(filename)
    break
os.chdir(foldername)
print(filelist)
pdflist=[]
for i in pdflist:
    if i[-3:]=='pdf':
        pdflist.append(i)
pdflist.sort()
# pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

for pdf in pdflist:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()