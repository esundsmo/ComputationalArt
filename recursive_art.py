""" For Software Design F2016 Olin College

    Generates random computer art using recursive functions to develop random functions that red blue and green colours are mapped to.
    Does not require input. May change image size via test_image() inputs.
    Current colour function depth ranges; can change these values by making appropriate changes to build_random_function().

    Thanks to Rebecca Patterson for clarifying how to use recursion in the function building process!!! :)

    Note: excessive doctesting was foregone in favor of checking mathematical logic by hand/calculator/computer


    @author: Elizabeth Sundsmo  4/19/16
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
    functions = {
                "x":  lambda x: x,
                "y":  lambda y: y,
                "pwr3":   lambda x: x**3,
                "pwr4":   lambda x: x**4,
                "cos_pi":   lambda x: math.cos(math.pi*x),
                "sin_pi":   lambda x: math.sin(math.pi*x),
                "avg":   lambda a, b: (a+b)/2,
                "prod":  lambda a, b: a*b
                } 
    function_inputs = {"x": 0,"y": 0,"pwr3":1,"pwr4":1,"cos_pi":1,"sin_pi":1,"avg":2,"prod":2}
    func_names = function_inputs.keys()

    #Determine which functions are usable given current depth
    if max_depth==1: #if 1 before max depth, final function w/o inputs to make stop
        possible = [f for f in func_names if function_inputs[f]==0]
        chosen = random.choice(possible)
    elif min_depth > 0: #hasn't reached min depth yet-- keep going! (min deepth can be negative!)
        possible = [f for f in func_names if function_inputs[f]>0]
        chosen = random.choice(possible)
    else: #btwn min and max! Take your pick!
        chosen = random.choice(func_names)

    fn = functions[chosen]

    #Check chosen function input requirements and build function
    if function_inputs[chosen] == 0:
        return fn
    elif function_inputs[chosen] == 1:
        args=[build_random_function(min_depth-1, max_depth-1)]
    else:
        args=[ build_random_function(min_depth-1, max_depth-1), 
               build_random_function(min_depth-1, max_depth-1) ] 

    #Return built function
    return lambda x,y: fn(*[arg(x, y) for arg in args])

def remap_interval(val,input_interval_start,input_interval_end,output_interval_start,output_interval_end):
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
    red_function = build_random_function(2,6)
    green_function = build_random_function(5,9)
    blue_function = build_random_function(9,12)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = ( 
                    color_map(red_function(x, y)),
                    color_map(green_function(x, y)),
                    color_map(blue_function(x, y))   )
    im.save(filename)

if __name__ == '__main__':
    # import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(evaluate_random_function, globals(), verbose=True)

  # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("test18.png")

  # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")