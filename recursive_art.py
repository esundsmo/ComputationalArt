""" For Software Design F2016 Olin College

    Generates random computer art using recursive functions to develop random functions that red blue and green colours are mapped to.
    Does not require input. May change image size via test_image() inputs.
    Current colour function depth ranges 7:9, can change these values by making appropriate changes to build_random_function() and evaluate_random_function().

    Thanks to Rebecca Patterson for clarifying how to use recursion in the function building process!!! :)

    Note: excessive doctesting was foregone in favor of checking mathematical logic by hand/calculator/computer


    @author: Elizabeth Sundsmo  2/16/16
"""

import random
import math
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)

        --------No doctests because this function relies on random!!--------
    """
    if max_depth == 1: #if 1 before max depth, final function w/o inputs to make stop
    	choose = random.randint(0,1)
    	if choose == 0:
    		return ["x"]
    	if choose == 1:
    		return ["y"]

    elif min_depth > 0: #hasn't reached min depth yet-- keep going!
    	choose2 = random.randint(0,5)#need to make 2 more functions -check!
    	if choose2 == 0:
    		return ["sin_pi", build_random_function(min_depth-1, max_depth-1)]
    	if choose2 == 1:
    		return ["cos_pi", build_random_function(min_depth-1, max_depth-1)]
    	if choose2 == 2:
    		return ["avg", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
    	if choose2 == 3:
    		return ["prod", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
    	if choose2 == 4:
    		return ["pwr4", build_random_function(min_depth-1, max_depth-1)]
    	if choose2 == 5:
    		return ["circ", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]

    else: #btwn min and max! Take your pick!
    	choose3 = random.randint(0,7) #need to make 2 more functions -check!
    	if choose3 == 0:
    		return ["x"]
    	if choose3 == 1:
    		return ["y"]
    	if choose3 == 2:
    		return ["sin_pi", build_random_function(min_depth-1, max_depth-1)]
    	if choose3 == 3:
    		return ["cos_pi", build_random_function(min_depth-1, max_depth-1)]
    	if choose3 == 4:
    		return ["avg", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
    	if choose3 == 5:
    		return ["prod", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
    	if choose3 == 6:
    		return ["pwr4", build_random_function(min_depth-1, max_depth-1)]
    	if choose3 == 7:
    		return ["circ", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]




def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02

        -------Can't write doctests beyond first two conditional because relies on random!-------
    """
    if f[0] == "x":
    	return x
    if f[0] == "y":
    	return y

    if f[0] == "sin_pi":
    	return math.sin(math.pi*evaluate_random_function(f[1], x, y))
    if f[0] == "cos_pi":
    	return math.cos(math.pi*evaluate_random_function(f[1], x, y))

    if f[0] == "avg":
    	return 0.5*((evaluate_random_function(f[1], x, y) + evaluate_random_function(f[1], x, y)))
    if f[0] == "prod":
    	return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[1], x, y)
    if f[0] == "pwr4":
    	return evaluate_random_function(f[1], x, y)**4
    if f[0] == "circ":
    	return (math.sqrt(evaluate_random_function(f[1], x, y)**2 + evaluate_random_function(f[1], x, y)**2)) - 1


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    
    num = (float(val - input_interval_start) * float(output_interval_end - output_interval_start)) 
    denom = float(input_interval_end - input_interval_start) 
    scaled_val = (num/denom)+ output_interval_start

    return scaled_val

def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7,9)
    green_function = build_random_function(7,9)
    blue_function = build_random_function(7,9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(evaluate_random_function, globals(), verbose=True)


  # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("sun_myart13.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")
