import sys
sys.dont_write_bytecode = True
from visual import *
import get_info
import sat_functions

def main():
    sat_info_dict = get_info.get_info()

    satelite, earth, time, sat_axis_x, sat_axis_y, sat_axis_z = sat_functions.create_and_draw_objects()
    
    info_entry = 0
    while info_entry < 5799:
    
        sleep(0.0001)
        info_entry += 1
    

        satelite.pos = (sat_info_dict["Info Entry "+str(info_entry)]["sat_x_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_y_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_z_pos"])
        
        quaternion = [sat_info_dict["Info Entry "+str(info_entry)]["quaternion_w"],
                      sat_info_dict["Info Entry "+str(info_entry)]["quaternion_i"],
                      sat_info_dict["Info Entry "+str(info_entry)]["quaternion_j"],
                      sat_info_dict["Info Entry "+str(info_entry)]["quaternion_k"]]
        
        sat_axis_x.pos = satelite.pos
        sat_axis_y.pos = satelite.pos
        sat_axis_z.pos = satelite.pos
        
        sat_axis_xyz = sat_functions.calc_sat_axis(satelite, earth, quaternion,sat_info_dict["Info Entry "+str(info_entry)]["declination"],
                                                                           sat_info_dict["Info Entry "+str(info_entry)]["right_ascension"])

        sat_axis_x.axis= sat_axis_xyz[0]*20000
        sat_axis_y.axis= sat_axis_xyz[1]*20000
        sat_axis_z.axis= sat_axis_xyz[2]*20000
        
        day, hours, minutes = sat_functions.convert_julian_to_real_time(sat_info_dict["Info Entry "+str(info_entry)]["time"])
        time.text =("Time:   "+str(day)+" "+str(hours)+":"+str(minutes))


    sat_functions.end_loop(satelite) 


main()
