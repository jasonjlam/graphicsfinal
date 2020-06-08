from math import log, e, sin, pi, asin

def vector_interpolation(start_frame, end_frame, start_vector, end_vector, f):
    delta = []
    for i in range(3):
        delta.append((end_vector[i] - start_vector[i]) / (end_frame - start_frame))

    if f == start_frame:
        value = start_vector
        return value
    elif f >= start_frame and f <= end_frame:
        value = []
        for i in range(3):
            value.append(start_vector[i] + delta[i] * (f - start_frame))
            return value 


def linear_interpolation(start_frame, end_frame, start_value, end_value, f):
    delta = (end_value - start_value) / (end_frame - start_frame)

    if f == start_frame:
        value = start_value
        return value
    elif f >= start_frame and f <= end_frame:
        value = start_value + delta * (f - start_frame)
        return value

def quadratic_interpolation(start_frame, end_frame, start_value, end_value, f):
    delta = 1 / (end_frame - start_frame)
    if f == start_frame:
        value = start_value
        return value
    elif f >= start_frame and f <= end_frame:
        value = start_value + (delta * (f - start_frame))**2 * (end_value - start_value)
        return value
def cubic_interpolation(start_frame, end_frame, start_value, end_value, f):
    delta = 1 / (end_frame - start_frame)
    if f == start_frame:
        value = start_value
        return value
    elif f >= start_frame and f <= end_frame:
        value = start_value + (delta * (f - start_frame))**3 * (end_value - start_value)
        return value
def logarithmic_interpolation(start_frame, end_frame, start_value, end_value, f):
    # print (end_frame - start_frame)
    delta =  (e-1) / (end_frame - start_frame)
    # print (delta)
    if f == start_frame:
        value = start_value
        return value
    elif f >= start_frame and f <= end_frame:
        value = start_value + log(1 + delta * f) * (end_value - start_value)
        return value

def oscillation_interpolation(start_frame, end_frame, start_value, end_value, f):
    start = asin(start_value)
    print (end_value * pi / 2)
    target = asin(end_value)
    delta = start + (2 * pi * (end_frame - start_frame) - target)/(100 * (end_frame - start_frame))
    if f == start_frame:
        value = start_value
        return value
    elif f >= start_frame and f <= end_frame:
        value = sin(start + (f-start_frame) * delta)
        return value
