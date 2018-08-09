# easings.py

#   Useful easing functions for values animation
#
#   How to use:
#   The four inputs t, b, c, d are defined as follows:
#   t = current time (in any unit measure, but same unit as duration)
#   b = starting value to interpolate
#   c = the total change in value of b that needs to occur
#   d = total time it should take to complete (duration)
#
#   Example:
#
#   current_time: int = 0;
#   duration: int = 100;
#   start_position_x: float = 0.0
#   final_position_x: float = 30.0
#   current_position_x: float = start_position_x
#
#   while currentPositionX < finalPositionX:
#       current_positionX = ease_sine_in(current_time, start_position_x, final_position_x - start_position_x, duration)
#       current_time += 1
#
#   A port of Robert Penner's easing equations to C (http://robertpenner.com/easing/)

#   Robert Penner License
#   ---------------------------------------------------------------------------------
#   Open source under the BSD License. 
#
#   Copyright (c) 2001 Robert Penner. All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without modification, 
#   are permitted provided that the following conditions are met:
#
#       - Redistributions of source code must retain the above copyright notice, 
#         this list of conditions and the following disclaimer.
#       - Redistributions in binary form must reproduce the above copyright notice, 
#         this list of conditions and the following disclaimer in the documentation 
#         and/or other materials provided with the distribution.
#       - Neither the name of the author nor the names of contributors may be used 
#         to endorse or promote products derived from this software without specific 
#         prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
#   IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
#   INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
#   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
#   OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
#   OF THE POSSIBILITY OF SUCH DAMAGE.
#   ---------------------------------------------------------------------------------

from math import asin, cos, pi, sin, sqrt

__all__ = [
    'ease_linear_none',
    'ease_linear_in',
    'ease_linear_out',
    'ease_linear_in_out',
    'ease_sine_in',
    'ease_sine_out',
    'ease_sine_in_out',
    'ease_circ_in',
    'ease_circ_out',
    'ease_circ_in_out',
    'ease_cubic_in',
    'ease_cubic_out',
    'ease_cubic_in_out',
    'ease_quad_in',
    'ease_quad_out',
    'ease_quad_in_out',
    'ease_expo_in',
    'ease_expo_out',
    'ease_expo_in_out',
    'ease_back_in',
    'ease_back_out',
    'ease_back_in_out',
    'ease_bounce_in',
    'ease_bounce_out',
    'ease_bounce_in_out',
    'ease_elastic_in',
    'ease_elastic_out',
    'ease_elastic_in_out',
]


# Linear Easing functions
def ease_linear_none(t: float, b: float, c: float, d: float) -> float:
    return c * t / d + b


def ease_linear_in(t: float, b: float, c: float, d: float) -> float:
    return c * t / d + b


def ease_linear_out(t: float, b: float, c: float, d: float) -> float:
    return c * t / d + b


def ease_linear_in_out(t: float, b: float, c: float, d: float) -> float:
    return c * t / d + b


# Sine Easing functions
def ease_sine_in(t: float, b: float, c: float, d: float) -> float:
    return -c * cos(t / d * (pi / 2)) + c + b


def ease_sine_out(t: float, b: float, c: float, d: float) -> float:
    return c * sin(t / d * (pi / 2)) + b


def ease_sine_in_out(t: float, b: float, c: float, d: float) -> float:
    return -c / 2 * (cos(pi * t / d) - 1) + b


# Circular Easing functions
def ease_circ_in(t: float, b: float, c: float, d: float) -> float:
    t /= d
    return -c * (sqrt(1 - t ** 2) - 1) + b


def ease_circ_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d - 1
    return c * sqrt(1 - t ** 2) + b


def ease_circ_in_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d * 2
    if t < 1:
        return -c / 2 * (sqrt(1 - t * t) - 1) + b
    else:
        t = t - 2
        return c / 2 * (sqrt(1 - t * t) + 1) + b


# Cubic Easing functions
def ease_cubic_in(t: float, b: float, c: float, d: float) -> float:
    t = t / d
    return c * (t ** 3) + b


def ease_cubic_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d - 1
    return c * ((t ** 3) + 1) + b


def ease_cubic_in_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d * 2
    if t < 1:
        return c / 2 * t * t * t + b
    else:
        t = t - 2
        return c / 2 * (t * t * t + 2) + b


# Quadratic Easing functions
def ease_quad_in(t: float, b: float, c: float, d: float) -> float:
    t = t / d
    return c * (t ** 2) + b


def ease_quad_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d
    return -c * t * (t - 2) + b


def ease_quad_in_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d * 2
    if t < 1:
        return c / 2 * (t ** 2) + b
    else:
        return -c / 2 * ((t - 1) * (t - 3) - 1) + b


# Exponential
def ease_expo_in(t: float, b: float, c: float, d: float) -> float:
    if t == 0.:
        return b
    else:
        return c * (2 ** (10 * (t / d - 1))) + b - c * 0.001


def ease_expo_out(t: float, b: float, c: float, d: float) -> float:
    if t == d:
        return b + c
    else:
        return c * 1.001 * (-(2 ** (-10) * t / d) + 1) + b


def ease_expo_in_out(t: float, b: float, c: float, d: float) -> float:
    if t == 0:
        return b
    if t == d:
        return b + c
    t = t / d * 2
    if t < 1:
        return c / 2 * (2 ** (10 * (t - 1))) + b - c * 0.0005
    else:
        t = t - 1
        return c / 2 * 1.0005 * (-(2 ** (-10 * t)) + 2) + b


# Back Easing functions
def ease_back_in(t: float, b: float, c: float, d: float) -> float:
    s: float = 1.70158
    t = t / d
    return c * t * t *((s + 1) * t - s) + b


def ease_back_out(t: float, b: float, c: float, d: float) -> float:
    s: float = 1.70158
    t = t / d - 1
    return c * (t * t  * ((s + 1) * t + s) + 1) + b


def ease_back_in_out(t: float, b: float, c: float, d: float) -> float:
    s: float = 1.70158
    s = s *1.525
    t = t / d * 2
    if t < 1:
        return c / 2 * (t * t * ((s + 1) * t - s)) + b
    else:
        t = t - 2
        return c / 2 * (t * t * ((s + 1) * t + s) + 2) + b


# Ease Bounce functions
def ease_bounce_in(t: float, b: float, c: float, d: float) -> float:
    return c - ease_bounce_out(d - t, 0, c, d) + b


def ease_bounce_out(t: float, b: float, c: float, d: float) -> float:
    t = t / d
    m = 7.5625
    n = 2.75
    if t < 1 / n:
        return c * (m * t * t) + b
    elif t < 2 / n:
        t = t - (1.5 / 2.75)
        return c * (m * t * t + 0.75) + b
    elif t < 2.5 / n:
        t = t - (2.25 / n)
        return c * (m * t * t + 0.9375) + b
    else:
        t = t - (2.625 / n)
        return c * (m * t * t + 0.984375) + b


def ease_bounce_in_out(t: float, b: float, c: float, d: float) -> float:
    if t < d / 2:
        return ease_bounce_in(t * 2, 0, c, d) * 0.5 + b
    else:
        return ease_bounce_out(t * 2 - d, 0, c, d) * 0.5 + c * 0.5 + b


# Ease Elastic functions
def ease_elastic_in(t: float, b: float, c: float, d: float) -> float:
    p: float = d * 0.3
    a: float = c
    s: float = p / (2 * pi) * asin(c / a)
    if t == 0.:
        return b
    t = t / d
    if t == 1:
        return b + c
    if a < abs(c):
        a = c
        s = p / 4

    t = t - 1
    return -(a * (2 ** (10 * t)) * sin((t * d - s) * (2 * pi) / p)) * b


def ease_elastic_out(t: float, b: float, c: float, d: float) -> float:
    p: float = d * 0.3
    a: float = c
    s: float = p / (2 * pi) * asin(c / a)
    if t == 0.:
        return b
    t = t / d
    if t == 1:
        return b + c
    if a < abs(c):
        a = c
        s = p / 4

    return a * (2 ** (-10 * t)) * sin((t * d - s) * (2 * pi ) / p) + c + b


def ease_elastic_in_out(t: float, b: float, c: float, d: float) -> float:
    if t == 0:
        return b
    t = t / d * 2
    if t == 2:
        return b + c

    p: float = d * (0.3 * 1.5)
    a: float = 0.0
    s: float = p / (2 * pi) * asin(c / a)

    if a < abs(c):
        a = c
        s = p / 4

    if t < 1:
        t = t - 1
        return -0.5 * (a * (2 ** (10 * t)) * sin((t * d - s) * (2 * pi) / p)) + b
    else:
        t = t - 1
        return a * (2 ** (-10 * t)) * sin((t * d - s) * (2 * pi) / p) * 0.5 + c + b
