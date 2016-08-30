from visual import *
import math

def create_and_draw_objects():
    """creates and draws the vpython window, time text, earth and satelite"""
    
    scene = display(width = 800, height = 800, forward=(-1,0,0), up=(0,0,1))
    
    draw_lights()

    time= label(pos=(0,9000,17000), text='Time: ')
    #time= label(pos=(0,150000,200000), text='Time: ')

    earth = sphere(pos=(0,0,0), radius= 6371, material = materials.earth,
                   up=(0,0,1))

    satelite = box(pos=(0,0,0), length = 100,  width=100, height=100,
                   color=color.red, make_trail=false)

    star_arrow = arrow(pos=(0,0,0), axis=(0,1,0), shaftwidth=100)

    return satelite, earth, time, star_arrow

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

def calc_arrow_pos_and_axis(star_arrow, satelite, earth):
    star_arrow.pos = satelite.pos
    
    declination = 0000.357728
    right_ascension = 0001.338847
    declination_vector = rotate((1,0,0), angle=declination, axis=(0,-1,0))
    right_ascension_vector = rotate((1,0,0), angle=right_ascension, axis=(0,0,1))
    star_direction = declination_vector + right_ascension_vector
    star_distance = 15000
    star_pos= star_direction*star_distance
    
    star_arrow.axis = star_pos - satelite.pos
    
    if check_collision_arrow_earth(star_arrow, earth):
        star_arrow.visible = False
    else:
        star_arrow.visible = True
    
    return star_arrow.pos, star_arrow.axis

def check_collision_arrow_earth(star_arrow, earth):
    projection = proj(-star_arrow.pos, star_arrow.axis)
    closest_point_to_earth = star_arrow.pos + projection
    if mag(closest_point_to_earth) <= earth.radius:
        return True
    else:
        return False

def end_loop(satelite):
    """if there is no more positional info the satelite stops and turns green"""
    
    while True:
        sleep(0.01)
        satelite.color = color.green
        
