# Imports all modules needed
from visual import *
from PIL import Image
import math

# Creates the two screens, one for the entire solar system, and one for each object view
solar_system_scene = display(title='Solar System', x=680, y=0, width=800, height=730, center=(0, 0, 0))
object_scene = display(title='Object View', x=0, y=0, width=680, height=730, center=(0, 0, 0))
solar_system_scene.select()

# Opens the texture images
sun_img = Image.open(r"C:\Users\devra\Pictures\8k_sun.jpg")
mercury_img = Image.open(r"C:\Users\devra\Pictures\2k_mercury.jpg")
venus_img = Image.open(r"C:\Users\devra\Pictures\2k_venus.jpg")
earth_img = Image.open(r"C:\Users\devra\Pictures\2k_earth.jpg")
mars_img = Image.open(r"C:\Users\devra\Pictures\2k_mars.jpg")
jupiter_img = Image.open(r"C:\Users\devra\Pictures\2k_jupiter.jpg")
saturn_img = Image.open(r"C:\Users\devra\Pictures\2k_saturn.jpg")
uranus_img = Image.open(r"C:\Users\devra\Pictures\2k_uranus.jpg")
neptune_img = Image.open(r"C:\Users\devra\Pictures\2k_neptune.jpg")

# Creates the textures
sun_texture = materials.texture(data=sun_img, mapping="spherical")
sun_view_texture = materials.texture(data=sun_img, mapping="spherical")
mercury_texture = materials.texture(data=mercury_img, mapping="spherical")
mercury_view_texture = materials.texture(data=mercury_img, mapping="spherical")
venus_texture = materials.texture(data=venus_img, mapping="spherical")
venus_view_texture = materials.texture(data=venus_img, mapping="spherical")
earth_texture = materials.texture(data=earth_img, mapping="spherical")
earth_view_texture = materials.texture(data=earth_img, mapping="spherical")
mars_texture = materials.texture(data=mars_img, mapping="spherical")
mars_view_texture = materials.texture(data=mars_img, mapping="spherical")
jupiter_texture = materials.texture(data=jupiter_img, mapping="spherical")
jupiter_view_texture = materials.texture(data=jupiter_img, mapping="spherical")
saturn_texture = materials.texture(data=saturn_img, mapping="spherical")
saturn_view_texture = materials.texture(data=saturn_img, mapping="spherical")
uranus_texture = materials.texture(data=uranus_img, mapping="spherical")
uranus_view_texture = materials.texture(data=uranus_img, mapping="spherical")
neptune_texture = materials.texture(data=neptune_img, mapping="spherical")
neptune_view_texture = materials.texture(data=neptune_img, mapping="spherical")

# Selects the solar_system_scene
solar_system_scene.select()

# Creates Sunlight
solar_system_scene.lights = []
sunlight = local_light(pos=vector(0, 0, 0), color=color.white)

determine_planet = -1  # Presets the view to the Sun
saved_planet = -1
forward = True  # All planets are moving forward (Preset value of True)
backward = False
rotation_multiplier = 1  # Used to rotation clockwise or counter clockwise depending on movement


# Class to create a planet
class Planet:
    def __init__(self, radius, position, orbit_speed, trail_color, given_texture):
        x, y, z = position
        self.radius = radius
        self.theta = orbit_speed
        self.material = given_texture
        # Creates a sphere
        self.planet = sphere(radius=radius, pos=vector(x, y, z), material=self.material,
                             make_trail=True, trail_type="points", interval=1000, retain=50)
        self.planet.trail_object.color = trail_color

    # Gets the texture package
    def get_material(self):
        return self.material

    # Gets the value of the radius
    def get_radius(self):
        return self.radius

    # Gets the position
    def get_position(self):
        return self.planet.pos.x, self.planet.pos.y, self.planet.pos.z

    # Sets the position
    def set_position(self, given_position):
        x, y, z = given_position
        self.planet.pos = vector(x, y, z)

    # Sets the rotation
    def set_rotation(self, rotation_speed, rotation_axis):
        self.planet.rotate(angle=radians(rotation_speed), axis=rotation_axis)

    # Gets the value of Theta
    def get_theta(self):
        return self.theta

    # Sets the value of Theta
    def set_theta(self, increment):
        self.theta += increment

    # Deletes the planet object
    def delete(self):
        self.planet.visible = False
        del self.planet


# Class to create a star such as our sun
class Star(Planet):
    # Initializes by inheriting from the Planet class
    def __init__(self, radius, position, orbit_speed, trail_color, given_texture):
        Planet.__init__(self, radius, position, orbit_speed, trail_color, given_texture)


# Class used to display info text on the screen
class Info:
    def __init__(self, info_text, height):
        self.info_text = info_text
        # Creates a new text object
        self.info = text(text=self.info_text, pos=vector(1.5, 1, 0), height=height, depth=(height / 6), color=color.white)

    # Sets the text
    def set_text(self, object_info_text):
        self.info_text = object_info_text

    # Deletes the text
    def delete(self):
        self.info.visible = False
        del self.info


# Creates the sun and all the planets, their sizes are all relative to Earth's
# Earth's size = 0.1 radius (12, 742 km)
sun = Star(10.9, (0, 0, 0), 0, color.white, sun_texture)
mercury = Planet(0.0383, (0, 0, 454.48), 0.016075, color.red, mercury_texture)
venus = Planet(0.095, (0, 0, 849.16), 0.011760, color.orange, venus_texture)
earth = Planet(0.1, (0, 0, 1174.07), 0.01, color.yellow, earth_texture)
mars = Planet(0.0533, (0, 0, 1788.57), 0.008085, color.green, mars_texture)
jupiter = Planet(1.121, (0, 0, 6109.72), 0.004389, color.cyan, jupiter_texture)
saturn = Planet(0.945, (0, 0, 11246.27), 0.003254, color.blue, saturn_texture)
uranus = Planet(0.401, (0, 0, 22531.78), 0.002287, color.magenta, uranus_texture)
neptune = Planet(0.388, (0, 0, 35277.04), 0.001823, color.white, neptune_texture)

# Creates the rings by extruding a circular object
space_between_rings = shapes.circle(radius=2, thickness=0.7)
saturn_ring_frame = frame(pos=vector(0, 0, 11246.27))
saturn_ring_frame.rotate(angle=radians(63.27), axis=vector(1, 0, 0))  # Angle of 26.73 (same as Saturn's)
saturn_rings = extrusion(frame=saturn_ring_frame, pos=vector(0, 0, 0), path=[vector(0, 0, 0), vector(0, 0, -0.1)],
                         shape=space_between_rings)

object_scene.select()  # Selects the individual planet View screen

# Creates a object used for the individual planet view
planet_dupe = Planet(1, (0, 0, 0), 0, color.white, sun_view_texture)
# Creates the info text
info_text = Info("SUN \n\nMass:   1.989 x 10^30 kg \nRadius:  695,508 km \nRotation Speed:    1997 m/s "
                 "\nTilt Angle:     0 Degrees \nSurface Temperature:    5,778 K", 0.2)

solar_system_scene.select()

# Lists of the planets and sets the value of theta of saturn's rings
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
saturn_ring_theta = saturn.get_theta()

# List of all the info text of the objects and texture packages
material_list = [mercury_view_texture, venus_view_texture, earth_view_texture, mars_view_texture,
                 jupiter_view_texture, saturn_view_texture, uranus_view_texture, neptune_view_texture,]
info_texts = ["MERCURY \n\nMass:  3.285 x 10^23 kg \nRadius:  2,440 km \nRotation Period:     176 Earth Days"
                 "\nTilt Angle:     2.04 Degrees \nOrbital Period:      88 Earth Days \nDistance from Sun:      57.91 million km",
              "VENUS \n\nMass:    4.867 x 10^24 kg \nRadius:  6,052 km \nRotation Period:     243 Earth Days"
                 "\nTilt Angle:     177.36 Degrees \nOrbital Period:    225 Earth Days \nDistance from Sun:     108.2 million km",
              "EARTH \n\nMass:    5.972 x 10^24 kg \nRadius:  6,371 km \nRotation Period:     1 Earth Day"
                 "\nTilt Angle:     23.50 Degrees \nOrbital Period:     365 Earth Days \nDistance from Sun:     149.6 million km",
              "MARS \n\nMass:     6.390 x 10^23 kg \nRadius:  3,390 km \nRotation Period:     24.65 Earth Hours"
                 "\nTilt Angle:     25.19 Degrees \nOrbital Period:     687 Earth Days \nDistance from Sun:     227.9 million km",
              "JUPITER \n\nMass:  1.898 x 10^27 kg \nRadius:  69,911 km \nRotation Period:    9.9 Earth hours"
                 "\nTilt Angle:     3.13 Degrees \nOrbital Period:      12 Earth Years \nDistance from Sun:     778.5 million km",
              "SATURN \n\nMass:   5.683 x 10^26 kg \nRadius:  58,232 km \nRotation Period:    10.23 Earth Hours"
                 "\nTilt Angle:     26.73 Degrees \nOrbital Period:     29 Earth Years \nDistance from Sun:     1.433 billion km",
              "URANUS \n\nMass:   8.681 x 10^25 kg \nRadius:  25,362 km \nRotation Period:    17.23 Earth Hours"
                 "\nTilt Angle:     97.77 Degrees \nOrbital Period:     84 Earth Years \nDistance from Sun:     2.871 billion km",
              "NEPTUNE \n\nMass:  1.024 x 10^26 kg \nRadius:  24,622 km \nRotation Period:    16.11 Earth Hours"
                 "\nTilt Angle:     28.32 Degrees \nOrbital Period:     165 Earth Years \nDistance from Sun:    4.495 billion km"]


# Movement of the planets relative to earth's movement speed
# Earth's orbit speed = 0.01 (29.78 m/s)
def object_movement():
    # This controls the path of each orbit
    mercury.set_position((455.48 * math.sin(mercury.get_theta()), 0, 454.48 * math.cos(mercury.get_theta())))
    venus.set_position((850.16 * math.sin(venus.get_theta()), 0, 849.16 * math.cos(venus.get_theta())))
    earth.set_position((1175.07 * math.sin(earth.get_theta()), 0, 1174.07 * math.cos(earth.get_theta())))
    mars.set_position((1789.57 * math.sin(mars.get_theta()), 0, 1788.57 * math.cos(mars.get_theta())))
    jupiter.set_position((6110.72 * math.sin(jupiter.get_theta()), 0, 6109.72 * math.cos(jupiter.get_theta())))
    saturn.set_position((11247.27 * math.sin(saturn.get_theta()), 0, 11246.27 * math.cos(saturn.get_theta())))
    saturn_ring_frame.pos = vector(11247.27 * math.sin(saturn.get_theta()), 0, 11246.27 * math.cos(saturn.get_theta()))
    uranus.set_position((22532.78 * math.sin(uranus.get_theta()), 0, 22531.78 * math.cos(uranus.get_theta())))
    neptune.set_position((35278.04 * math.sin(neptune.get_theta()), 0, 35277.04 * math.cos(neptune.get_theta())))


# Handles all the rotation of the planets, rings and the sun relative to earth's rotation speed
# Earth's rotation speed = 0.1 (460 m/s)
def object_rotation(rotation_multiplier):
    # This controls the rotational speeds and angles
    sun.set_rotation(4.341 * rotation_multiplier, (0, 1, 0))  # Angle of 0
    mercury.set_rotation(0.001705 * rotation_multiplier, (3.56198, 100, 0))  # Angle of 2.04
    venus.set_rotation(-0.0004115 * rotation_multiplier, (-4.61093, 100, 0))  # Angle of 177.36 (Retrograde motion)
    earth.set_rotation(0.1 * rotation_multiplier, (43.48124, 100, 0))  # Angle of 23.5
    mars.set_rotation(0.09748 * rotation_multiplier, (47.03511, 100, 0))  # Angle of 25.19
    jupiter.set_rotation(0.2418 * rotation_multiplier, (5.46832, 100, 0))  # Angle of 3.13
    saturn.set_rotation(0.2275 * rotation_multiplier, (50.36038, 100, 0))  # Angle of 26.73
    uranus.set_rotation(0.1392 * rotation_multiplier, (100, 13.64, 0))  # Angle of 97.77
    neptune.set_rotation(0.149 * rotation_multiplier, (53.89, 100, 0))  # Angle of 28.32


# Used to go forward
def set_forward_thetas(saturn_ring_theta):
    # This controls the orbital speeds
    mercury.set_theta(0.00016075)
    venus.set_theta(0.00011760)
    earth.set_theta(0.0001)
    mars.set_theta(0.00008085)
    jupiter.set_theta(0.00004389)
    saturn.set_theta(0.00003254)
    uranus.set_theta(0.00002287)
    neptune.set_theta(0.00001823)
    saturn_ring_theta += 0.00003254


# Used to go backward
def set_backward_thetas(saturn_ring_theta):
    # This controls the orbital speeds
    mercury.set_theta(-0.00016075)
    venus.set_theta(-0.00011760)
    earth.set_theta(-0.0001)
    mars.set_theta(-0.00008085)
    jupiter.set_theta(-0.00004389)
    saturn.set_theta(-0.00003254)
    uranus.set_theta(-0.00002287)
    neptune.set_theta(-0.00001823)
    saturn_ring_theta -= 0.00003254


"""Main Program Loop"""
while True:
    rate(150)   # Determines how fast the program will run

    # Determines which key is pressed and program acts according to it
    if solar_system_scene.kb.keys:
        key = solar_system_scene.kb.getkey()
        if key == "z":
            forward = False
            backward = True  # Sets backward to True
            rotation_multiplier = -1
        elif key == "x":
            forward = True  # Sets forward to True
            backward = False
            rotation_multiplier = 1
        if key == 'right':
            if determine_planet == 7:
                determine_planet = 7  # Sets the determine_planet to 7
            else:
                determine_planet += 1  # Adds 1 from the current value of determine_planet
        elif key == 'left':
            if determine_planet == -1:
                determine_planet = -1  # Sets the determine_planet to 7
            else:
                determine_planet -= 1  # Subtracts 1 from the current value of determine_planet

    if saved_planet != determine_planet:
        object_scene.select()
        planet_dupe.delete()  # Deletes the planet
        if determine_planet == -1:
            texture = sun_view_texture  # Sets the texture to the Sun's
        else:
            texture = material_list[determine_planet]  # Sets the texture to the corresponding planet
        planet_dupe = Planet(1, (0, 0, 0), 0, color.white, texture)  # Creates a new planet object
        info_text.delete()  # Deletes the Info Text object
        if determine_planet == -1:
            info_text = Info("SUN \n\nMass:   1.989 x 10^30 kg \nRadius:    695,508 km \nRotation Speed:    1997 m/s "
                 "\nTilt Angle:     0 Degrees \nSurface Temperature:    5,778 K", 0.2)  # Info for the Sun
        else:
            info_text = Info(info_texts[determine_planet], 0.2)  # Creates a new Info Text object with corresponding info
        saved_planet = determine_planet

    solar_system_scene.select()  # Goes back to the Solar System screen to run the following code

    # Sets the rotation of all the objects and positions in space to move
    object_movement()
    object_rotation(rotation_multiplier)

    # Displays the planet after setting its new location in space
    if determine_planet == -1:
        solar_system_scene.center = vector(sun.get_position())  # Sets the camera to the middle of the sun
    else:
        # Extracts the planar values of the position of the planets
        x, y, z = planets[determine_planet].get_position()
        solar_system_scene.center = vector(x, y, z)  # Centers the camera in the middle of each planet

        # Sets the theta to go forwards
    if forward:
        set_forward_thetas(saturn_ring_theta)

        # Sets the theta to go backwards
    elif backward:
        set_backward_thetas(saturn_ring_theta)
