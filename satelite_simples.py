import sys
sys.dont_write_bytecode = True
from visual import *
import get_info
import sat_functions

def main():
    satelite_info_dict = get_info.get_info()

    scene = display(width = 700, height = 700)

    draw_day = text(text="Day 0",pos = (5000, 8000,0),
                color=color.orange, width =1000, height = 1000)

    earth = sphere(pos=(0,0,0), radius= 6371, material = materials.earth)

    satelite = box(pos=(satelite_info_dict["day1"]["sat_x_pos"],
                        satelite_info_dict["day1"]["sat_y_pos"],
                        satelite_info_dict["day1"]["sat_z_pos"]),
                        color=color.red, length = 100, width=100, height=100)

    day = 0
    while day < 5799:
    
        sleep(0.001)
        day += 1
    

        satelite.pos = (satelite_info_dict["day"+str(day)]["sat_x_pos"],
                        satelite_info_dict["day"+str(day)]["sat_y_pos"],
                        satelite_info_dict["day"+str(day)]["sat_z_pos"])
    
        draw_day.text = "Day " +str(day)

    sat_functions.end_loop() 


main()
