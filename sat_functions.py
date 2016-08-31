from visual import *
import math

def create_and_draw_objects():
    """creates and draws the vpython window, time text, earth and satelite"""
    
    scene = display(width = 800, height = 800, forward=(-1,0,0), up=(0,0,1))
    
    draw_lights()

    time= label(pos=(0,9000,17000), text='Time: ')

    earth = sphere(pos=(0,0,0), radius= 6371, material = materials.earth,
                   up=(0,0,1))

    satelite = box(pos=(0,0,0), length = 100,  width=100, height=100,
                   color=color.red, make_trail=true)

    star_arrow = arrow(pos=(0,0,0), axis=(0,1,0), shaftwidth=100, make_trail=True)

    return satelite, earth, time, star_arrow


def draw_lights():
    """lights the scene"""
    lamp1 = local_light(pos=(0,-50000,0), color=color.white)
    lamp2 = local_light(pos=(0,50000,0), color=color.white)
    lamp3 = local_light(pos=(-50000,0,0), color=color.white)
    lamp4 = local_light(pos=(50000,0,0), color=color.white)

def convert_julian_to_real_time(julian_time):
    """converts a julian day starting from 1/1/2000 to normal time"""
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

def calc_arrow_pos_and_axis(star_arrow, satelite, earth, info_entry):
    """calculates the position and direction of the arrow that points to the star"""
    star_arrow.pos = satelite.pos
    
    declination = 0000.357728
    right_ascension = 0001.338847
    declination_vector = rotate((1,0,0), angle=declination, axis=(0,-1,0))
    right_ascension_vector = rotate((1,0,0), angle=right_ascension, axis=(0,0,1))

    star_direction = declination_vector + right_ascension_vector
    """
    if info_entry <= 250:
        star_arrow.axis = star_direction*10000
    elif 250 < info_entry <=500:
        star_arrow.axis = star_direction*15000
    elif 500 < info_entry <=750:
        star_arrow.axis = star_direction*20000
    elif 750 < info_entry <=1000:
        star_arrow.axis = star_direction*30000
    elif 1000 < info_entry <=1250:
        star_arrow.axis = star_direction*40000
    elif 1250 < info_entry <=1500:
        star_arrow.axis = star_direction*50000
    elif 1500 < info_entry <=1750:
        star_arrow.axis = star_direction*75000
    elif 1750 < info_entry <=2000:
        star_arrow.axis = star_direction*100000
    elif 2000 < info_entry <=2250:
        star_arrow.axis = star_direction*150000
    elif info_entry >2250:
        star_arrow.axis = star_direction*200000
    """    
    star_arrow.axis = star_direction*40000
    if check_collision_arrow_earth(star_arrow, earth):
        star_arrow.visible = False
    else:
        star_arrow.visible = True
    
    return star_arrow.pos, star_arrow.axis

def check_collision_arrow_earth(star_arrow, earth):
    """checks if the arrow goes through the earth, and if it does, it becomes invisible"""
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
        
