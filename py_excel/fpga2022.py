from plot import *
if __name__=='__main__':
    # stratix
    prp_alm=eline_to_list("B4", "B12")
    prp_delay=eline_to_list("D4", "D12")
    cp_name=eline_to_list("A16","A16")
    cp_alm=eline_to_list("B16","B16")
    cp_delay=eline_to_list("C16","C16")
    plt=figure_template_1([prp_alm, prp_delay],cp_name,[cp_alm,cp_delay],'r',clear=True,save_name='stratix.pdf')
    #plt.show()
    # arria
    prp_alm=eline_to_list("AB4", "AB12")
    prp_delay=eline_to_list("AD4", "AD12")
    cp_name=eline_to_list("AA16","AA16")
    cp_alm=eline_to_list("AB16","AB16")
    cp_delay=eline_to_list("AC16","AC16")
    plt=figure_template_1([prp_alm, prp_delay],cp_name,[cp_alm,cp_delay],'g',clear=True,save_name='arria.pdf')
    #plt.show()
    # cyclone
    prp_alm=eline_to_list("BB4", "BB12")
    prp_delay=eline_to_list("BD4", "BD12")
    cp_name=eline_to_list("BA16","BA16")
    cp_alm=eline_to_list("BB16","BB16")
    cp_delay=eline_to_list("BC16","BC16")
    plt=figure_template_1([prp_alm, prp_delay],cp_name,[cp_alm,cp_delay],'b',clear=True,save_name='cyclone.pdf')
    #plt.show()