from PIL import Image

names=['D:\\papers\\papers\\FPGA2022\\cyclone.png']
image1 = Image.open(r'D:\\papers\\papers\\FPGA2022\\cyclone.png')
im1 = image1.convert('RGB')
im1.save(r'D:\\papers\\papers\\FPGA2022\\cyclone.pdf')