import xlrd
import matplotlib.pyplot as plt
import copy

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
    t,p=0,0
    while 'A'<=cell_str_1[p]<='Z':
        t=ord(cell_str_1[p])-ord('A')+1+t*26
        p+=1
    cord1=[t-1, int(cell_str_1[p:])-1]
    t,p=0,0
    while 'A'<=cell_str_2[p]<='Z':
        t=ord(cell_str_1[p])-ord('A')+1+t*26
        p+=1
    cord2=[t-1, int(cell_str_2[p:])-1]
    x_step=1 if cord2[0]-cord1[0]>0 else 0
    y_step=1 if cord2[1]-cord1[1]>0 else 0
    while cord1[0]<=cord2[0] and cord1[1]<=cord2[1]:
        ret.append(sheet.cell_value(cord1[1], cord1[0]))
        cord1[0]+=x_step
        cord1[1]+=y_step
        if x_step==0 and y_step==0: # only one cell
            break
    return ret

def figure_template_1(prp_data,cp_name=None,cp_data=None,color='r',clear=True,save_name='1.pdf'):
    """
    figure_template_1
    prp_data: proposed data =[[area],[frequency]]=[[area_u=1, area_u=2,..], [...]]
    """
    if clear:
        plt.figure(figsize=(8, 8), dpi=80)
        plt.xlabel("Delay(ms)")
        plt.ylabel("ALM")
        plt.title("Area-time complexity (n=256)")
    plt.plot(prp_data[1],prp_data[0],marker='o',markersize=5,linewidth=1,color=color)
    t=1
    for i in range(len(prp_data[0])):
        c_str='u='
        plt.text(prp_data[1][i],prp_data[0][i],c_str+str(t))
        t*=2
    if cp_name:
        plt.plot(cp_data[1],cp_data[0],marker='*',markersize=5,linewidth=1,color=color)
        for i in range(len(cp_name)):
            s=copy.deepcopy(cp_name[i])
            plt.text(cp_data[1][i],cp_data[0][i],s)
    #plt.show()
    plt.savefig(save_name)
    return plt
if __name__=="__main__":
    plt.figure(figsize=(5,5))
    x=eline_to_list("AD4", "AD6")
    print(x)
    plt.plot(x,x,marker='o',markersize=3,linewidth=1,color='r')
    plt.plot([490],[490],marker='x')
    plt.legend("abc")
    plt.annotate("h=1",xy=[x[0],x[0]])
    plt.show()