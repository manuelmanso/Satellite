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
    
    while satelite_pos_to_next_day_dist >=  current_to_next_day_dist/2:

            sleep(0.001)

            
            satelite.pos+= calc_new_movement_vector(satelite, earth, movement_vector)

            satelite_pos_to_next_day_dist = mag(next_day_pos - satelite.pos)

def calc_new_movement_vector(satelite, earth, movement_vector):
    gravity_constant = 13e8
    
    dist_to_earth = (satelite.pos.x**2 + satelite.pos.y**2 + satelite.pos.z**2)**0.5
    radial_vector = (earth.pos - satelite.pos)/dist_to_earth
    Fgrav = gravity_constant*radial_vector/dist_to_earth**2
    movement_vector +=Fgrav
    
    return movement_vector
