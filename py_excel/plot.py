import xlrd
import matplotlib.pyplot as plt

wb=xlrd.open_workbook("D:\\papers\\papers\\FPGA2022\\exp_data.xls")
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(1, 0))
def eline_to_list(cell_str_1, cell_str_2):
    """
    x axis: A, B, C, ... => 0, 1, 2, ...
    y axis: 1, 2, 3, ... => 0, 1, 2, ...
    sheet.cell_value(1, 0) <=> .cell_value(y=1, x=0) <=> A1
    """
    ret=[]
    cord1=[ord(cell_str_1[0])-ord('A'), int(cell_str_1[1:])-1]
    cord2=[ord(cell_str_2[0])-ord('A'), int(cell_str_2[1:])-1]
    x_step=1 if cord2[0]-cord1[0]>0 else 0
    y_step=1 if cord2[1]-cord1[1]>0 else 0
    while cord1[0]<=cord2[0] and cord1[1]<=cord2[1]:
        ret.append(sheet.cell_value(cord1[1], cord1[0]))
        cord1[0]+=x_step
        cord1[1]+=y_step
    return ret

if __name__=="__main__":
    plt.figure()
    print(eline_to_list("B4", "B6"))