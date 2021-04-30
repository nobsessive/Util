# absolute off-set from left to left: left, bottom, right, head/pixel
# python -m pip install pdfCropMargins
# python -m pip install pdfCropMargins[gui] --upgrade --user
# if pdf corrupted use --gsFix option. 
#    this option requires gswin32c.exe which may be downloaded from https://www.ghostscript.com/download/gsdnld.html
from pdfCropMargins import crop
filename="test_pdf.pdf"
crop(["-p", "0", "-gui","--gsFix", filename])