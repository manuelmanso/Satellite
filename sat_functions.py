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
                   color=color.red, make_trail=False)

    sat_axis_x = arrow(pos=(0,0,0), axis=(1,0,0), shaftwidth=100, make_trail=False, color=color.green)
    sat_axis_y = arrow(pos=(0,0,0), axis=(0,1,0), shaftwidth=100, make_trail=False, color=color.red)
    sat_axis_z = arrow(pos=(0,0,0), axis=(0,0,1), shaftwidth=100, make_trail=False, color=color.blue)

    return satelite, time, sat_axis_x, sat_axis_y, sat_axis_z


def draw_lights():
    """lights the earth so it isn't too dark"""
    
    lamp1 = local_light(pos=(0,-50000,0), color=color.white)
    lamp2 = local_light(pos=(0,50000,0), color=color.white)
    lamp3 = local_light(pos=(-50000,0,0), color=color.white)
    lamp4 = local_light(pos=(50000,0,0), color=color.white)

def calc_sat_axis(quaternion, declination, right_ascension):
    """calculates the axis of the satelite using their specific functions"""
    
    z_axis = calc_z_axis(declination, right_ascension, quaternion)

    temp_x_axis = vector_rotation_by_quaternion([1,0,0],quaternion)
    x_axis = calc_x_axis(temp_x_axis, z_axis)
    
    y_axis= cross(x_axis, z_axis)

    return [x_axis, y_axis, z_axis]

def quaternion_mult(q,r):
    """does the hamilton product calculation"""
    
    return [r[0]*q[0]-r[1]*q[1]-r[2]*q[2]-r[3]*q[3],
            r[0]*q[1]+r[1]*q[0]-r[2]*q[3]+r[3]*q[2],
            r[0]*q[2]+r[1]*q[3]+r[2]*q[0]-r[3]*q[1],
            r[0]*q[3]-r[1]*q[2]+r[2]*q[1]+r[3]*q[0]]

def vector_rotation_by_quaternion(v,q):
    """receives a vector and a quaternion as arguments and returns the resulting vector from the hamilton product"""
    
    r = [0]+v
    q_conj = [q[0],-1*q[1],-1*q[2],-1*q[3]]
    vector_as_list = quaternion_mult(quaternion_mult(q,r),q_conj)[1:]
    end_vector = vector(vector_as_list[0], vector_as_list[1], vector_as_list[2])

    return end_vector

def calc_x_axis(temp_x_axis, z_axis):
    """calcs the angle difference between the z and the x_axis and then changes
    the angle to 90 degrees to make them orthogonal"""
    
    start_angle = math.degrees((diff_angle(temp_x_axis,z_axis)))

    angle_change = 90.0 - start_angle

    x_axis = rotate(temp_x_axis, angle=radians(angle_change), axis=cross(z_axis,temp_x_axis))
    
    return x_axis
    
def calc_z_axis(declination, right_ascension, quaternion):
    """calcs the z_axis using declination and right_ascension"""
    
    declination_vector = rotate((1,0,0), angle=declination, axis=(0,-1,0))
    right_ascension_vector = rotate((1,0,0), angle=right_ascension, axis=(0,0,1))
    z_axis = norm(declination_vector + right_ascension_vector)

    return z_axis

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

def end_loop(satelite):
    """if there is no more positional info the satelite stops and turns green"""
    
    while True:
        sleep(0.01)
        satelite.color = color.green
