#!/usr/bin/env python3



import os
import time
import random
import math
import threading

try:
    import shytlight
except:
    import shytlight_simulator as shytlight


import numpy as np

h = 6.626e-34
c = 299792458
k = 1.38e-23

def xyz_from_xy(x, y):
    """Return the vector (x, y, 1-x-y)."""
    return np.array((x, y, 1-x-y))

class ColourSystem:
    """A class representing a colour system.

    A colour system defined by the CIE x, y and z=1-x-y coordinates of
    its three primary illuminants and its "white point".

    TODO: Implement gamma correction

    """

    # The CIE colour matching function for 380 - 780 nm in 5 nm intervals
    cie_path = os.path.join(os.path.dirname(__file__), 'cie-cmf.txt')
    cmf = np.genfromtxt(cie_path, delimiter=",")
    def __init__(self, red, green, blue, white):
        """Initialise the ColourSystem object.

        Pass vectors (ie NumPy arrays of shape (3,)) for each of the
        red, green, blue  chromaticities and the white illuminant
        defining the colour system.

        """

        # Chromaticities
        self.red, self.green, self.blue = red, green, blue
        self.white = white
        # The chromaticity matrix (rgb -> xyz) and its inverse
        self.M = np.vstack((self.red, self.green, self.blue)).T 
        self.MI = np.linalg.inv(self.M)
        # White scaling array
        self.wscale = self.MI.dot(self.white)
        # xyz -> rgb transformation matrix
        self.T = self.MI / self.wscale[:, np.newaxis]

    def xyz_to_rgb(self, xyz, out_fmt=None):
        """Transform from xyz to rgb representation of colour.

        The output rgb components are normalized on their maximum
        value. If xyz is out the rgb gamut, it is desaturated until it
        comes into gamut.

        By default, fractional rgb components are returned; if
        out_fmt='html', the HTML hex string '#rrggbb' is returned.

        """

        rgb = self.T.dot(xyz)
        if np.any(rgb < 0):
            # We're not in the RGB gamut: approximate by desaturating
            w = - np.min(rgb)
            rgb += w
        if not np.all(rgb==0):
            # Normalize the rgb vector
            rgb /= np.max(rgb)

        if out_fmt == 'html':
            return self.rgb_to_hex(rgb)
        return rgb

    def rgb_to_hex(self, rgb):
        """Convert from fractional rgb values to HTML-style hex string."""

        hex_rgb = (255 * rgb).astype(int)
        return '#{:02x}{:02x}{:02x}'.format(*hex_rgb)

    def spec_to_xyz(self, spec):
        """Convert a spectrum to an xyz point.

        The spectrum must be on the same grid of points as the colour-matching
        function, self.cmf: 380-780 nm in 5 nm steps.

        """

        XYZ = np.sum(spec[:, np.newaxis] * self.cmf, axis=0)
        den = np.sum(XYZ)
        if den == 0.:
            return XYZ
        return XYZ / den

    def spec_to_rgb(self, spec, out_fmt=None):
        """Convert a spectrum to an rgb value."""

        xyz = self.spec_to_xyz(spec)
        return self.xyz_to_rgb(xyz, out_fmt)

illuminant_D65 = xyz_from_xy(0.3127, 0.3291)
cs_hdtv = ColourSystem(red=xyz_from_xy(0.67, 0.33),
                       green=xyz_from_xy(0.21, 0.71),
                       blue=xyz_from_xy(0.15, 0.06),
                       white=illuminant_D65)



def planck(lam, T):
    """ Returns the spectral radiance of a black body at temperature T.

    Returns the spectral radiance, B(lam, T), in W.sr-1.m-2 of a black body
    at temperature T (in K) at a wavelength lam (in nm), using Planck's law.

    """

    lam_m = lam / 1.e9
    fac = h*c/lam_m/k/T
    B = 2*h*c**2/lam_m**5 / (np.exp(fac) - 1)
    return B

def black_body_color(K):
    lam = np.arange(380., 781., 5)

    spec = planck(lam, K)
    rgb = cs_hdtv.spec_to_rgb(spec)
    return rgb*255

def adsr(periode,a_d_s_r,overdrive):
    times = [round(x * periode) for x in a_d_s_r]
    t = 1
    
    times[3] = periode - times[0] - times[1] - times[2]

    if overdrive > 1:
        slevel = 1./overdrive
        alevel = 1

    else:
        s = overdrive
        alevel = overdrive
        slevel = 1
    
    return np.concatenate((np.linspace(0,alevel,times[0]), np.linspace(alevel,slevel,times[1]),
        np.linspace(slevel,slevel,times[2]), np.linspace(slevel,0,times[3])))

class ChampagnePattern(threading.Thread):
    def __init__(self):
        super(ChampagnePattern, self).__init__()
        self.stopping = False
        # calculate colors
        self.colormap = [black_body_color(10000*(i/256.)+2000) for i in range(256)]
        self.chance = 0.01
        self.rep = 2
        self.frame = shytlight.t_chitframe()
        self.period = 255
        self.sparck_freq = 7.
        self.particles = [self.period]*40

        self.a_d_s_r = [0.1,0.4,0.2,0.3]
        self.overdrive = 1.2

        self.envel = adsr(self.period, self.a_d_s_r, self.overdrive)

        self.k_center = 60
        self.amp = 10

    def stop(self):
        self.stopping = True

    def get_brightness(self,t):
        if t<len(self.envel):
            return self.envel[t]
        else:
            return 0.0
        
    def get_color(self,t):
        return self.colormap[int(round(np.sin(2*np.pi*self.sparck_freq/self.period*t)*self.amp+self.k_center))]


    def run(self):
        while not self.stopping:
            for i, color in enumerate(self.particles):
                   if self.stopping:
                       break
                   if random.random() < self.chance:
                        if self.particles[i] >= self.period:
                             self.particles[i] = 0
                   if (color>=0 and color<self.period):
                       self.particles[i]+=1
                       envelope = self.get_brightness(self.particles[i])
                       self.frame.brightness[(i//8)][(i%8)][:] = [int (f) for f in self.get_color(color)*envelope]
            if not self.stopping:
                shytlight.add_frame(self.rep, self.frame)
