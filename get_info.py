import os

def get_info():
    with open(os.path.expanduser("~/Desktop/satelite/dados_satelite.txt")) as textfile:
        data = textfile.read().replace('\n', '').split(" ")

    return create_sat_info_dict(data)


def create_sat_info_dict(lst):

    sat_info_dict={}
    day=0
    
    while day<5799:
        
        day +=1
        
        index = lst.index("HD")
        temp_list = lst[index:index+14]

        sat_info_dict["day"+str(day)]={"star" : temp_list[0] + temp_list[1] + temp_list[2],
                                      "rotation_period" : float(temp_list[3]),
                                      "sat_declination" : float(temp_list[4]),
                                      "sat_right_ascension" : float(temp_list[5]),
                                      "time_measured" : float(temp_list[6]),
                                      "sat_x_pos" : int(float(temp_list[7]))/1000,
                                      "sat_y_pos" : int(float(temp_list[8]))/1000,
                                      "sat_z_pos" : int(float(temp_list[9]))/1000,
                                      "quaternion_1" : float(temp_list[10]),
                                      "quaternion_i" : float(temp_list[11]),
                                      "quaternion_j" : float(temp_list[12]),
                                      "quaternion_k" : float(temp_list[13])}

        lst.pop(index)

    return sat_info_dict
