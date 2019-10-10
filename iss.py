#!/usr/bin/env python

__author__ = 'mwilliamson with LOTS of help from Zach and Piero'

import requests
import turtle
import time
# import json


# def astronaut_names():
#     crew = requests.get('http://api.open-notify.org/astros.json')
#     dictionary = crew.text
#     dictionary = json.loads(dictionary)
#     for person in dictionary['people']:
#         print('{} is on the ISS orbiting the Earth'.format(
#             person['name']))
def astronaut_names():
    r = requests.get('http://api.open-notify.org/astros.json')
    d = r.json()
    return d['people']


def get_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    result = r.json()

    location_dict = result['iss_position']
    lat = float(location_dict['latitude'])
    lon = float(location_dict['longitude'])
    t = time.ctime(result['timestamp'])
    print('current ISS location:lat={}, lon={}, time={}'.format(lat, lon, t))
    return (lon, lat)


def pass_Indy():
    r = requests.get('http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349') 

    pass_over = r.json()
    pass_over = pass_over['response'][0]
    pass_over = time.ctime(pass_over['risetime'])
    return 'next passover {}'.format(pass_over)


def graphics_map(position, pass_time):
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(position)
    Indy_pos = turtle.Turtle()
    Indy_pos.shape('circle')
    Indy_pos.color('yellow')
    Indy_pos.penup()
    Indy_pos.goto(-86.1349, 40.273502)
    message = turtle.Turtle()
    message.color('yellow')
    message.write(pass_time, True, align='center',font=('Arial', 20, 'normal') )

    screen.exitonclick()


def main():
    # collecting astronaut names
    astros = astronaut_names()
    for person in astros:
        print('{} is on {}'.format(
            person['name'], person['craft']))
    p = pass_Indy()
    # collecting current ISS location
    coords = get_coordinates()
    graphics_map(coords, p)
    


if __name__ == '__main__':
    main()
