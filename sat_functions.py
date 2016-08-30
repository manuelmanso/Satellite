from visual import *
import math

def create_and_draw_objects():
    """creates and draws the vpython window, time text, earth and satelite"""
    
    scene = display(width = 800, height = 800, forward=(-1,0,0), up=(0,0,1))
    
    draw_lights()
    
    time = text(text="Time: ",pos = (0,2000,9000), color=color.orange, up=(0,0,1),
                    width =1000, height = 1000, axis= (0,1,0))

    earth = sphere(pos=(0,0,0), radius= 6371, material = materials.earth,
                   up=(0,0,1))

    satelite = box(pos=(0,0,0), length = 100,  width=100, height=100,
                   color=color.red, make_trail=false)

    return satelite, earth, time

    """
    sun = sphere(pos=(149600000,0,0), color=color.orange, radius = 695.700)
    earth.rotate(angle=0.01745, axis=(0,0,1), origin=earth.pos)
    
    X_loc_blue = sphere(pos=(7500,0,0), color=color.blue, radius= 500)
    Y_loc_yellow = sphere(pos=(0,7500,0), color=color.yellow, radius= 500)
    Z_loc_green = sphere(pos=(0,0,7500), color=color.green, radius= 500)
    """


def draw_lights():
    """lights the scene"""
    lamp1 = local_light(pos=(0,-50000,0), color=color.white)
    lamp2 = local_light(pos=(0,50000,0), color=color.white)
    lamp3 = local_light(pos=(-50000,0,0), color=color.white)
    lamp4 = local_light(pos=(50000,0,0), color=color.white)

def convert_julian_to_real_time(julian_time):
    julian_day = int(julian_time)
    if julian_day == 6896:
        day = "18 Nov 2018"
    elif julian_day == 6897:
        day = "19 Nov 2018"
    elif julian_day == 6898:
        day = "20 Nov 2018"
    elif julian_day == 6899:
        day = "21 Nov 2018"
    elif julian_day == 6900:
        day = "22 Nov 2018"
    
    decimal = julian_time - int(julian_time)
    seconds_in_a_day = 86400
    total_seconds = int(decimal * seconds_in_a_day)

    hours, minutes = divmod(total_seconds, 3600)
    minutes = int(math.ceil(float(minutes)/60))

    return day, hours, minutes
    
def end_loop():
    """if there is no more positional info the satelite stops and turns green"""
    
    while True:
        sleep(0.01)
        satelite.color = color.green
        
