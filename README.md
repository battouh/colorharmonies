# Color Harmonies

## Synopsis

Simple library to generate color harmonies (monochromatic, complementary, analogous, triadic, split complementary and tetradic) from a RGB color input.

https://en.wikipedia.org/wiki/Harmony_(color)


## Installation

Code running with Python 3.x

```
pip install colorharmonies

```

We recommend to create a virtual environment:

with virtualenv
```
cd colorharmonies
virtualenv vEnv --no-site-packages -p python3
source vEnv/bin/activate
pip install colorharmonies
```
with Python's venv (better for Mac OSX)
```
cd colorharmonies
python3 -m venv vEnv
source vEnv/bin/activate
pip install colorharmonies
```

## Manual

Color is an object with 3 attributes RGB, HLS, HSV: 
* RGB : [int(0 to 255), int(0 to 255), int(0 to 255)]
* HLS : [int(0 to 360), int(0 to 100), int(0 to 100)]
* HSV : [int(0 to 360), int(0 to 100), int(0 to 100)]

Each attribute represents one color space.


### Import all functions
```
from colorharmonies import Color, complementaryColor, triadicColor, splitComplementaryColor, tetradicColor, analogousColor, monochromaticColor
```

### Color Object
Create a color object and assign it a value to its RGB attributes
```
Cyan = Color([0, 255, 255],"","")
```

### complentaryColor
complentaryColor returns the complementary color of a Color object. 
Return the color in RGB format
```
complementaryColor(Cyan)
# return [255, 0, 0]
```

### triadicColor
triadicColor returns the two triadic colors of a Color object. 
Return a list of the two colors in RGB format
```
triadicColor(Cyan)
# return [[255, 0, 255], [255, 255, 0]]
```

### splitComplementaryColor
splitComplementaryColor returns the two split complementary colors of a Color object.
Return a list of the two colors in RGB format
```
splitComplementaryColor(Cyan)
#return [[255, 0, 128], [255, 128, 0]]
```

### tetradicColor
tetradicColor returns the three tetradic colors of a Color object.
Return a list of the three colors in RGB format
```
tetradicColor(Cyan)
# return [[0, 0, 255], [255, 0, 0], [255, 255, 0]]
```

### analogousColor
analogousColor returns the two analogous colors of a Color object.
Return a list of the two colors in RGB format
```
analogousColor(Cyan)
# return [[0, 127, 255], [0, 255, 128]]
```

### monochromaticColor
monochromaticColor returns a list of monochromatic colors of a Color object.
Return a list of colors in RGB format
```
monochromaticColor(Cyan)
# return [[0, 255, 255], [0, 242, 242], [0, 230, 230], [13, 255, 255], [12, 242, 242], [11, 230, 230], [25, 255, 255], [24, 242, 242], [23, 230, 230]]
```