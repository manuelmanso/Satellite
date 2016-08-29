from visual import *
import time

def create_and_draw_objects(sat_info):
    """creates and draws the vpython window, day text, earth and satelite"""
    
    scene = display(width = 800, height = 800, forward=(-1,0,0), up=(0,0,1))
    
    draw_lights()
    
    draw_day = text(text="Day 1",pos = (0,8000,8000), color=color.orange, up=(0,0,1),
                    width =1000, height = 1000, axis= (0,1,0))

    earth = sphere(pos=(0,0,0), radius= 6371, material = materials.earth,
                  up=(0,0,1))
    
    """
    sun = sphere(pos=(149600000,0,0), color=color.orange, radius = 695.700)
    earth.rotate(angle=0.01745, axis=(0,0,1), origin=earth.pos)
    equator = ring(pos=(0,0,0),color=color.red, axis=(0,0,1),
                   radius=6371, thickness=50)
    ecliptic_vector = rotate((0,0,1), angle = 0.4084, axis=(1,0,0))
    ecliptic = ring(pos=(0,0,0),color=color.orange, axis=ecliptic_vector,
                   radius=6371, thickness=50)
    
    X_loc_blue = sphere(pos=(7500,0,0), color=color.blue, radius= 500)
    Y_loc_yellow = sphere(pos=(0,7500,0), color=color.yellow, radius= 500)
    Z_loc_green = sphere(pos=(0,0,7500), color=color.green, radius= 500)
    """
    
    satelite = box(pos=(sat_info["day1"]["sat_x_pos"],
                        sat_info["day1"]["sat_y_pos"],
                        sat_info["day1"]["sat_z_pos"]),
                        color=color.red, length = 100, width=100, height=100,
                        make_trail=false)

    return satelite, earth, draw_day


def draw_lights():
    lamp1 = local_light(pos=(0,-50000,0), color=color.white)
    lamp2 = local_light(pos=(0,50000,0), color=color.white)
    lamp3 = local_light(pos=(-50000,0,0), color=color.white)
    lamp4 = local_light(pos=(50000,0,0), color=color.white)

    
def day_to_day_loop(sat_info, satelite, earth, draw_day):
    """Gets the satelite position for the current day and the next day,
    creates a vector between those two positions and measures the size
    of the vector. Calls the during_a_day_loop function and after the
    satelite orbits the earth once the next day begins"""

    day = 0
    while day < 5799:
    
        sleep(0.001)
        day += 1
        draw_day.text = "Day " +str(day)

        current_day_pos = vector(sat_info["day"+str(day)]["sat_x_pos"],
                                 sat_info["day"+str(day)]["sat_y_pos"],
                                 sat_info["day"+str(day)]["sat_z_pos"])

        next_day_pos = vector(sat_info["day"+str(day+1)]["sat_x_pos"],
                              sat_info["day"+str(day+1)]["sat_y_pos"],
                              sat_info["day"+str(day+1)]["sat_z_pos"])

        movement_vector = current_day_pos - next_day_pos

        current_to_next_day_dist = mag(movement_vector)
        satelite_pos_to_next_day_dist = mag(next_day_pos - satelite.pos)

        during_a_day_loop(current_to_next_day_dist, satelite_pos_to_next_day_dist,
                          next_day_pos, movement_vector, earth, satelite)

        satelite.pos = next_day_pos
        

def during_a_day_loop(current_to_next_day_dist, satelite_pos_to_next_day_dist,
                      next_day_pos, movement_vector, earth, satelite):
    """to write"""

    gravity_constant = 13e8
    
    while satelite_pos_to_next_day_dist >=  current_to_next_day_dist/2:

            sleep(0.001)

            dist_to_earth = (satelite.pos.x**2 + satelite.pos.y**2 + satelite.pos.z**2)**0.5
            radial_vector = (earth.pos - satelite.pos)/dist_to_earth
            Fgrav = gravity_constant*radial_vector/dist_to_earth**2
            movement_vector +=Fgrav
            satelite.pos+= movement_vector

            satelite_pos_to_next_day_dist = mag(next_day_pos - satelite.pos)
    
def end_loop():
    """if all 5799 days pass the satelite stops and turns green"""
    
    while True:
        sleep(0.01)
        satelite.color = color.green
