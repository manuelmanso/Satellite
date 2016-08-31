import sys
sys.dont_write_bytecode = True
from visual import *
import get_info
import sat_functions

def main():
    sat_info_dict = get_info.get_info()

    satelite, earth, time, star_arrow = sat_functions.create_and_draw_objects()
    
    info_entry = 0
    while info_entry < 5799:
    
        sleep(0.001)
        info_entry += 1
    

        satelite.pos = (sat_info_dict["Info Entry "+str(info_entry)]["sat_x_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_y_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_z_pos"])
        
        star_arrow.pos,  star_arrow.axis = sat_functions.calc_arrow_pos_and_axis(star_arrow, satelite, earth, info_entry)

        points(pos=(star_arrow.pos + star_arrow.axis), color=color.green)

        day, hours, minutes = sat_functions.convert_julian_to_real_time(sat_info_dict["Info Entry "+str(info_entry)]["time"])
        time.text =("Time:   "+str(day)+" "+str(hours)+":"+str(minutes))
        time.visible=False
        

    sat_functions.end_loop(satelite) 


main()
