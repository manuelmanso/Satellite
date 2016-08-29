import sys
sys.dont_write_bytecode = True
import get_info
import sat_functions


def main():
    """Gets satelite info with get_info, then creates and draws the window,
    earth, satelite and day text, then calls the day_to_day_loop function
    for the satelite to orbit the earth"""
    
    satelite_info_dict = get_info.get_info()

    satelite,earth, draw_day = sat_functions.create_and_draw_objects(satelite_info_dict)

    sat_functions.day_to_day_loop(satelite_info_dict, satelite, earth, draw_day)
    
    sat_functions.end_loop()


main()
