"""
perlin noise generator
author: Андрій Будильников

this program generates perlin noise, a type of gradient noise used in computer graphics
"""

import math
import random

class PerlinNoise:
    """perlin noise generator class"""
    
    permutation = [
        151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,
        8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,
        35,11,32,57,177,33,88,237,149,56,87,174,20,125,136,171,168,68,175,74,165,71,
        134,139,48,27,166,77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,
        55,46,245,40,244,102,143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,
        18,169,200,196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,
        250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,
        189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,221,153,101,155,167,43,
        172,9,129,22,39,253,19,98,108,110,79,113,224,232,178,185,112,104,218,246,97,
        228,251,34,242,193,238,210,144,12,191,179,162,241,81,51,145,235,249,14,239,
        107,49,192,214,31,181,199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,
        138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180
    ]
    
    p = []
    
    @classmethod
    def initialize(cls):
        """initialize the permutation table"""
        cls.p = [0] * 512
        for i in range(256):
            cls.p[i] = cls.p[i + 256] = cls.permutation[i]
    
    @staticmethod
    def lerp(a, b, t):
        """linear interpolation"""
        return a + t * (b - a)
    
    @staticmethod
    def fade(t):
        """fade function as defined by perlin"""
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    @staticmethod
    def grad(hash_val, x, y, z):
        """gradient function"""
        h = hash_val & 15
        u = x if h < 8 else y
        v = y if h < 4 else (x if h == 12 or h == 14 else z)
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)
    
    @classmethod
    def noise(cls, x, y, z):
        """3d perlin noise"""
        X = int(math.floor(x)) & 255
        Y = int(math.floor(y)) & 255
        Z = int(math.floor(z)) & 255
        
        x -= math.floor(x)
        y -= math.floor(y)
        z -= math.floor(z)
        
        u = cls.fade(x)
        v = cls.fade(y)
        w = cls.fade(z)
        
        A = cls.p[X] + Y
        AA = cls.p[A] + Z
        AB = cls.p[A + 1] + Z
        B = cls.p[X + 1] + Y
        BA = cls.p[B] + Z
        BB = cls.p[B + 1] + Z
        
        return cls.lerp(
            cls.lerp(
                cls.lerp(cls.grad(cls.p[AA], x, y, z), cls.grad(cls.p[BA], x - 1, y, z), u),
                cls.lerp(cls.grad(cls.p[AB], x, y - 1, z), cls.grad(cls.p[BB], x - 1, y - 1, z), u),
                v),
            cls.lerp(
                cls.lerp(cls.grad(cls.p[AA + 1], x, y, z - 1), cls.grad(cls.p[BA + 1], x - 1, y, z - 1), u),
                cls.lerp(cls.grad(cls.p[AB + 1], x, y - 1, z - 1), cls.grad(cls.p[BB + 1], x - 1, y - 1, z - 1), u),
                v),
            w)
    
    @classmethod
    def noise2d(cls, x, y):
        """2d perlin noise (z = 0)"""
        return cls.noise(x, y, 0)
    
    @classmethod
    def octave_noise(cls, x, y, octaves, persistence):
        """octave perlin noise for more natural looking results"""
        total = 0
        frequency = 1
        amplitude = 1
        max_value = 0
        
        for i in range(octaves):
            total += cls.noise(x * frequency, y * frequency, 0) * amplitude
            max_value += amplitude
            amplitude *= persistence
            frequency *= 2
        
        return total / max_value

def main():
    """main function to demonstrate perlin noise"""
    PerlinNoise.initialize()
    
    print("perlin noise examples")
    print("===================")
    
    # simple 2d noise
    print(f"simple 2d noise at (0.5, 0.5): {PerlinNoise.noise2d(0.5, 0.5)}")
    print(f"simple 2d noise at (1.0, 1.0): {PerlinNoise.noise2d(1.0, 1.0)}")
    print(f"simple 2d noise at (2.3, 4.7): {PerlinNoise.noise2d(2.3, 4.7)}")
    
    # octave noise
    print(f"\noctave noise at (0.5, 0.5): {PerlinNoise.octave_noise(0.5, 0.5, 4, 0.5)}")
    print(f"octave noise at (1.0, 1.0): {PerlinNoise.octave_noise(1.0, 1.0, 4, 0.5)}")
    print(f"octave noise at (2.3, 4.7): {PerlinNoise.octave_noise(2.3, 4.7, 4, 0.5)}")

if __name__ == "__main__":
    main()