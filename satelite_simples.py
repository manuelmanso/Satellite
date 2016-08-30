import sys
sys.dont_write_bytecode = True
from visual import *
import get_info
import sat_functions

def main():
    sat_info_dict = get_info.get_info()

    satelite, earth, time = sat_functions.create_and_draw_objects()
    

    info_entry = 0
    while info_entry < 5799:
    
        sleep(0.001)
        info_entry += 1
    

        satelite.pos = (sat_info_dict["Info Entry "+str(info_entry)]["sat_x_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_y_pos"],
                        sat_info_dict["Info Entry "+str(info_entry)]["sat_z_pos"])

        day, hours, minutes = sat_functions.convert_julian_to_real_time(sat_info_dict["Info Entry "+str(info_entry)]["time"])
        time.text = "Time:   "+str(day)+" "+str(hours)+":"+str(minutes)

    sat_functions.end_loop() 


main()
