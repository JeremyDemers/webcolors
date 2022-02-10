"""
Utility functions for working with the color names and color value
formats defined by the HTML and CSS specifications for use in
documents on the Web.

See documentation (in docs/ directory of source distribution) for
details of the supported formats, conventions and conversions.

"""

import re
import string
from typing import NamedTuple, Tuple, Union

__version__ = "1.11.1"


def _reversedict(d: dict) -> dict:
    """
    Internal helper for generating reverse mappings; given a
    dictionary, returns a new dictionary with keys and values swapped.

    """
    return {value: key for key, value in d.items()}


HEX_COLOR_RE = re.compile(r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")

COLOR_HEXA = "color_hexa"
HTML4 = "html4"
CSS2 = "css2"
CSS21 = "css21"
CSS3 = "css3"

SUPPORTED_SPECIFICATIONS = (HTML4, CSS2, CSS21, CSS3)

SPECIFICATION_ERROR_TEMPLATE = "{{spec}} is not a supported specification for color name lookups; \
supported specifications are: {supported}.".format(
    supported=",".join(SUPPORTED_SPECIFICATIONS)
)

IntegerRGB = NamedTuple("IntegerRGB", [("red", int), ("green", int), ("blue", int)])
PercentRGB = NamedTuple("PercentRGB", [("red", str), ("green", str), ("blue", str)])
HTML5SimpleColor = NamedTuple(
    "HTML5SimpleColor", [("red", int), ("green", int), ("blue", int)]
)

IntTuple = Union[IntegerRGB, HTML5SimpleColor, Tuple[int, int, int]]
PercentTuple = Union[PercentRGB, Tuple[str, str, str]]

# Mappings of color names to normalized hexadecimal color values.
#################################################################

# The HTML 4 named colors.
#
# The canonical source for these color definitions is the HTML 4
# specification:
#
# http://www.w3.org/TR/html401/types.html#h-6.5
#
# The file tests/definitions.py in the source distribution of this
# module downloads a copy of the HTML 4 standard and parses out the
# color names to ensure the values below are correct.
HTML4_NAMES_TO_HEX = {
    "aqua": "#00ffff",
    "black": "#000000",
    "blue": "#0000ff",
    "fuchsia": "#ff00ff",
    "green": "#008000",
    "gray": "#808080",
    "lime": "#00ff00",
    "maroon": "#800000",
    "navy": "#000080",
    "olive": "#808000",
    "purple": "#800080",
    "red": "#ff0000",
    "silver": "#c0c0c0",
    "teal": "#008080",
    "white": "#ffffff",
    "yellow": "#ffff00",
}

# CSS 2 used the same list as HTML 4.
CSS2_NAMES_TO_HEX = HTML4_NAMES_TO_HEX

# CSS 2.1 added orange.
CSS21_NAMES_TO_HEX = {"orange": "#ffa500", **HTML4_NAMES_TO_HEX}

# The CSS 3/SVG named colors.
#
# The canonical source for these color definitions is the SVG
# specification's color list (which was adopted as CSS 3's color
# definition):
#
# http://www.w3.org/TR/SVG11/types.html#ColorKeywords
#
# CSS 3 also provides definitions of these colors:
#
# http://www.w3.org/TR/css3-color/#svg-color
#
# SVG provides the definitions as RGB triplets. CSS 3 provides them
# both as RGB triplets and as hexadecimal. Since hex values are more
# common in real-world HTML and CSS, the mapping below is to hex
# values instead. The file tests/definitions.py in the source
# distribution of this module downloads a copy of the CSS 3 color
# module and parses out the color names to ensure the values below are
# correct.
CSS3_NAMES_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgrey": "#a9a9a9",
    "darkgreen": "#006400",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "grey": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32",
}

# The COLOR_HEXA named colors.
#
# The canonical source for these color definitions is the list
# of colors located at:
# https://www.colorhexa.com/color-names
COLOR_HEXA_NAMES_TO_HEX = {
    'Air Force Blue (Usaf)': '#00308f',
    'Air Superiority Blue': '#72a0c1',
    'Alabama Crimson': '#a32638',
    'Alice Blue': '#f0f8ff',
    'Alizarin Crimson': '#e32636',
    'Alloy Orange': '#c46210',
    'Almond': '#efdecd',
    'Amaranth': '#e52b50',
    'Amber': '#ffbf00',
    'Amber (Sae/Ece)': '#ff7e00',
    'American Rose': '#ff033e',
    'Amethyst': '#9966cc',
    'Android Green': '#a4c639',
    'Anti-Flash White': '#f2f3f4',
    'Antique Brass': '#cd9575',
    'Antique Fuchsia': '#915c83',
    'Antique Ruby': '#841b2d',
    'Antique White': '#faebd7',
    'Ao (English)': '#008000',
    'Apple Green': '#8db600',
    'Apricot': '#fbceb1',
    'Aqua': '#00ffff',
    'Aquamarine': '#7fffd4',
    'Army Green': '#4b5320',
    'Arsenic': '#3b444b',
    'Arylide Yellow': '#e9d66b',
    'Ash Grey': '#b2beb5',
    'Asparagus': '#87a96b',
    'Atomic Tangerine': '#ff9966',
    'Auburn': '#a52a2a',
    'Aureolin': '#fdee00',
    'Aurometalsaurus': '#6e7f80',
    'Avocado': '#568203',
    'Azure': '#007fff',
    'Azure Mist/Web': '#f0ffff',
    'Baby Blue': '#89cff0',
    'Baby Blue Eyes': '#a1caf1',
    'Baby Pink': '#f4c2c2',
    'Ball Blue': '#21abcd',
    'Banana Mania': '#fae7b5',
    'Banana Yellow': '#ffe135',
    'Barn Red': '#7c0a02',
    'Battleship Grey': '#848482',
    'Bazaar': '#98777b',
    'Beau Blue': '#bcd4e6',
    'Beaver': '#9f8170',
    'Beige': '#f5f5dc',
    'Big Dip ORuby': '#9c2542',
    'Bisque': '#ffe4c4',
    'Bistre': '#3d2b1f',
    'Bittersweet': '#fe6f5e',
    'Bittersweet Shimmer': '#bf4f51',
    'Black': '#000000',
    'Black Bean': '#3d0c02',
    'Black Leather Jacket': '#253529',
    'Black Olive': '#3b3c36',
    'Blanched Almond': '#ffebcd',
    'Blast-Off Bronze': '#a57164',
    'Bleu De France': '#318ce7',
    'Blizzard Blue': '#ace5ee',
    'Blond': '#faf0be',
    'Blue': '#0000ff',
    'Blue Bell': '#a2a2d0',
    'Blue (Crayola)': '#1f75fe',
    'Blue Gray': '#6699cc',
    'Blue-Green': '#0d98ba',
    'Blue (Munsell)': '#0093af',
    'Blue (Ncs)': '#0087bd',
    'Blue (Pigment)': '#333399',
    'Blue (Ryb)': '#0247fe',
    'Blue Sapphire': '#126180',
    'Blue-Violet': '#8a2be2',
    'Blush': '#de5d83',
    'Bole': '#79443b',
    'Bondi Blue': '#0095b6',
    'Bone': '#e3dac9',
    'Boston University Red': '#cc0000',
    'Bottle Green': '#006a4e',
    'Boysenberry': '#873260',
    'Brandeis Blue': '#0070ff',
    'Brass': '#b5a642',
    'Brick Red': '#cb4154',
    'Bright Cerulean': '#1dacd6',
    'Bright Green': '#66ff00',
    'Bright Lavender': '#bf94e4',
    'Bright Maroon': '#c32148',
    'Bright Pink': '#ff007f',
    'Bright Turquoise': '#08e8de',
    'Bright Ube': '#d19fe8',
    'Brilliant Lavender': '#f4bbff',
    'Brilliant Rose': '#ff55a3',
    'Brink Pink': '#fb607f',
    'British Racing Green': '#004225',
    'Bronze': '#cd7f32',
    'Brown (Traditional)': '#964b00',
    'Brown (Web)': '#a52a2a',
    'Bubble Gum': '#ffc1cc',
    'Bubbles': '#e7feff',
    'Buff': '#f0dc82',
    'Bulgarian Rose': '#480607',
    'Burgundy': '#800020',
    'Burlywood': '#deb887',
    'Burnt Orange': '#c50',
    'Burnt Sienna': '#e97451',
    'Burnt Umber': '#8a3324',
    'Byzantine': '#bd33a4',
    'Byzantium': '#702963',
    'Cadet': '#536872',
    'Cadet Blue': '#5f9ea0',
    'Cadet Grey': '#91a3b0',
    'Cadmium Green': '#006b3c',
    'Cadmium Orange': '#ed872d',
    'Cadmium Red': '#e30022',
    'Cadmium Yellow': '#fff600',
    'Café Au Lait': '#a67b5b',
    'Café Noir': '#4b3621',
    'Cal Poly Green': '#1e4d2b',
    'Cambridge Blue': '#a3c1ad',
    'Camel': '#c19a6b',
    'Cameo Pink': '#efbbcc',
    'Camouflage Green': '#78866b',
    'Canary Yellow': '#ffef00',
    'Candy Apple Red': '#ff0800',
    'Candy Pink': '#e4717a',
    'Capri': '#00bfff',
    'Caput Mortuum': '#592720',
    'Cardinal': '#c41e3a',
    'Caribbean Green': '#00cc99',
    'Carmine': '#960018',
    'Carmine (M&P)': '#d70040',
    'Carmine Pink': '#eb4c42',
    'Carmine Red': '#ff0038',
    'Carnation Pink': '#ffa6c9',
    'Carnelian': '#b31b1b',
    'Carolina Blue': '#99badd',
    'Carrot Orange': '#ed9121',
    'Catalina Blue': '#062a78',
    'Ceil': '#92a1cf',
    'Celadon': '#ace1af',
    'Celadon Blue': '#007ba7',
    'Celadon Green': '#2f847c',
    'Celeste (Colour)': '#b2ffff',
    'Celestial Blue': '#4997d0',
    'Cerise': '#de3163',
    'Cerise Pink': '#ec3b83',
    'Cerulean': '#007ba7',
    'Cerulean Blue': '#2a52be',
    'Cerulean Frost': '#6d9bc3',
    'Cg Blue': '#007aa5',
    'Cg Red': '#e03c31',
    'Chamoisee': '#a0785a',
    'Champagne': '#fad6a5',
    'Charcoal': '#36454f',
    'Charm Pink': '#e68fac',
    'Chartreuse (Traditional)': '#dfff00',
    'Chartreuse (Web)': '#7fff00',
    'Cherry': '#de3163',
    'Cherry Blossom Pink': '#ffb7c5',
    'Chestnut': '#cd5c5c',
    'China Pink': '#de6fa1',
    'China Rose': '#a8516e',
    'Chinese Red': '#aa381e',
    'Chocolate (Traditional)': '#7b3f00',
    'Chocolate (Web)': '#d2691e',
    'Chrome Yellow': '#ffa700',
    'Cinereous': '#98817b',
    'Cinnabar': '#e34234',
    'Cinnamon': '#d2691e',
    'Citrine': '#e4d00a',
    'Classic Rose': '#fbcce7',
    'Cobalt': '#0047ab',
    'Cocoa Brown': '#d2691e',
    'Coffee': '#6f4e37',
    'Columbia Blue': '#9bddff',
    'Congo Pink': '#f88379',
    'Cool Black': '#002e63',
    'Cool Grey': '#8c92ac',
    'Copper': '#b87333',
    'Copper (Crayola)': '#da8a67',
    'Copper Penny': '#ad6f69',
    'Copper Red': '#cb6d51',
    'Copper Rose': '#996666',
    'Coquelicot': '#ff3800',
    'Coral': '#ff7f50',
    'Coral Pink': '#f88379',
    'Coral Red': '#ff4040',
    'Cordovan': '#893f45',
    'Corn': '#fbec5d',
    'Cornell Red': '#b31b1b',
    'Cornflower Blue': '#6495ed',
    'Cornsilk': '#fff8dc',
    'Cosmic Latte': '#fff8e7',
    'Cotton Candy': '#ffbcd9',
    'Cream': '#fffdd0',
    'Crimson': '#dc143c',
    'Crimson Glory': '#be0032',
    'Cyan': '#00ffff',
    'Cyan (Process)': '#00b7eb',
    'Daffodil': '#ffff31',
    'Dandelion': '#f0e130',
    'Dark Blue': '#00008b',
    'Dark Brown': '#654321',
    'Dark Byzantium': '#5d3954',
    'Dark Candy Apple Red': '#a40000',
    'Dark Cerulean': '#08457e',
    'Dark Chestnut': '#986960',
    'Dark Coral': '#cd5b45',
    'Dark Cyan': '#008b8b',
    'Dark Electric Blue': '#536878',
    'Dark Goldenrod': '#b8860b',
    'Dark Gray': '#a9a9a9',
    'Dark Green': '#013220',
    'Dark Imperial Blue': '#00416a',
    'Dark Jungle Green': '#1a2421',
    'Dark Khaki': '#bdb76b',
    'Dark Lava': '#483c32',
    'Dark Lavender': '#734f96',
    'Dark Magenta': '#8b008b',
    'Dark Midnight Blue': '#003366',
    'Dark Olive Green': '#556b2f',
    'Dark Orange': '#ff8c00',
    'Dark Orchid': '#9932cc',
    'Dark Pastel Blue': '#779ecb',
    'Dark Pastel Green': '#03c03c',
    'Dark Pastel Purple': '#966fd6',
    'Dark Pastel Red': '#c23b22',
    'Dark Pink': '#e75480',
    'Dark Powder Blue': '#003399',
    'Dark Raspberry': '#872657',
    'Dark Red': '#8b0000',
    'Dark Salmon': '#e9967a',
    'Dark Scarlet': '#560319',
    'Dark Sea Green': '#8fbc8f',
    'Dark Sienna': '#3c1414',
    'Dark Slate Blue': '#483d8b',
    'Dark Slate Gray': '#2f4f4f',
    'Dark Spring Green': '#177245',
    'Dark Tan': '#918151',
    'Dark Tangerine': '#ffa812',
    'Dark Taupe': '#483c32',
    'Dark Terra Cotta': '#cc4e5c',
    'Dark Turquoise': '#00ced1',
    'Dark Violet': '#9400d3',
    'Dark Yellow': '#9b870c',
    'Dartmouth Green': '#00703c',
    'Davy Grey': '#555555',
    'Debian Red': '#d70a53',
    'Deep Carmine': '#a9203e',
    'Deep Carmine Pink': '#ef3038',
    'Deep Carrot Orange': '#e9692c',
    'Deep Cerise': '#da3287',
    'Deep Champagne': '#fad6a5',
    'Deep Chestnut': '#b94e48',
    'Deep Coffee': '#704241',
    'Deep Fuchsia': '#c154c1',
    'Deep Jungle Green': '#004b49',
    'Deep Lilac': '#9955bb',
    'Deep Magenta': '#cc00cc',
    'Deep Peach': '#ffcba4',
    'Deep Pink': '#ff1493',
    'Deep Ruby': '#843f5b',
    'Deep Saffron': '#f93',
    'Deep Sky Blue': '#00bfff',
    'Deep Tuscan Red': '#66424d',
    'Denim': '#1560bd',
    'Desert': '#c19a6b',
    'Desert Sand': '#edc9af',
    'Dim Gray': '#696969',
    'Dodger Blue': '#1e90ff',
    'Dogwood Rose': '#d71868',
    'Dollar Bill': '#85bb65',
    'Drab': '#967117',
    'Duke Blue': '#00009c',
    'Earth Yellow': '#e1a95f',
    'Ebony': '#555d50',
    'Ecru': '#c2b280',
    'Eggplant': '#614051',
    'Eggshell': '#f0ead6',
    'Egyptian Blue': '#1034a6',
    'Electric Blue': '#7df9ff',
    'Electric Crimson': '#ff003f',
    'Electric Cyan': '#00ffff',
    'Electric Green': '#00ff00',
    'Electric Indigo': '#6f00ff',
    'Electric Lavender': '#f4bbff',
    'Electric Lime': '#ccff00',
    'Electric Purple': '#bf00ff',
    'Electric Ultramarine': '#3f00ff',
    'Electric Violet': '#8f00ff',
    'Electric Yellow': '#ffff00',
    'Emerald': '#50c878',
    'English Lavender': '#b48395',
    'Eton Blue': '#96c8a2',
    'Fallow': '#c19a6b',
    'Falu Red': '#801818',
    'Fandango': '#b53389',
    'Fashion Fuchsia': '#f400a1',
    'Fawn': '#e5aa70',
    'Feldgrau': '#4d5d53',
    'Fern Green': '#4f7942',
    'Ferrari Red': '#ff2800',
    'Field Drab': '#6c541e',
    'Fire Engine Red': '#ce2029',
    'Firebrick': '#b22222',
    'Flame': '#e25822',
    'Flamingo Pink': '#fc8eac',
    'Flavescent': '#f7e98e',
    'Flax': '#eedc82',
    'Floral White': '#fffaf0',
    'Fluorescent Orange': '#ffbf00',
    'Fluorescent Pink': '#ff1493',
    'Fluorescent Yellow': '#ccff00',
    'Folly': '#ff004f',
    'Forest Green (Traditional)': '#014421',
    'Forest Green (Web)': '#228b22',
    'French Beige': '#a67b5b',
    'French Blue': '#0072bb',
    'French Lilac': '#86608e',
    'French Lime': '#ccff00',
    'French Raspberry': '#c72c48',
    'French Rose': '#f64a8a',
    'Fuchsia': '#ff00ff',
    'Fuchsia (Crayola)': '#c154c1',
    'Fuchsia Pink': '#ff77ff',
    'Fuchsia Rose': '#c74375',
    'Fulvous': '#e48400',
    'Fuzzy Wuzzy': '#cc6666',
    'Gainsboro': '#dcdcdc',
    'Gamboge': '#e49b0f',
    'Ghost White': '#f8f8ff',
    'Ginger': '#b06500',
    'Glaucous': '#6082b6',
    'Glitter': '#e6e8fa',
    'Gold (Metallic)': '#d4af37',
    'Gold (Web) (Golden)': '#ffd700',
    'Golden Brown': '#996515',
    'Golden Poppy': '#fcc200',
    'Golden Yellow': '#ffdf00',
    'Goldenrod': '#daa520',
    'Granny Smith Apple': '#a8e4a0',
    'Gray': '#808080',
    'Gray-Asparagus': '#465945',
    'Gray (Html/Css Gray)': '#808080',
    'Gray (X11 Gray)': '#bebebe',
    'Green (Color Wheel) (X11 Green)': '#00ff00',
    'Green (Crayola)': '#1cac78',
    'Green (Html/Css Green)': '#008000',
    'Green (Munsell)': '#00a877',
    'Green (Ncs)': '#009f6b',
    'Green (Pigment)': '#00a550',
    'Green (Ryb)': '#66b032',
    'Green-Yellow': '#adff2f',
    'Grullo': '#a99a86',
    'Guppie Green': '#00ff7f',
    'Halayà úBe': '#663854',
    'Han Blue': '#446ccf',
    'Han Purple': '#5218fa',
    'Hansa Yellow': '#e9d66b',
    'Harlequin': '#3fff00',
    'Harvard Crimson': '#c90016',
    'Harvest Gold': '#da9100',
    'Heart Gold': '#808000',
    'Heliotrope': '#df73ff',
    'Hollywood Cerise': '#f400a1',
    'Honeydew': '#f0fff0',
    'Honolulu Blue': '#007fbf',
    'Hooker Green': '#49796b',
    'Hot Magenta': '#ff1dce',
    'Hot Pink': '#ff69b4',
    'Hunter Green': '#355e3b',
    'Iceberg': '#71a6d2',
    'Icterine': '#fcf75e',
    'Imperial Blue': '#002395',
    'Inchworm': '#b2ec5d',
    'India Green': '#138808',
    'Indian Red': '#cd5c5c',
    'Indian Yellow': '#e3a857',
    'Indigo': '#6f00ff',
    'Indigo (Dye)': '#00416a',
    'Indigo (Web)': '#4b0082',
    'International Klein Blue': '#002fa7',
    'International Orange (Aerospace)': '#ff4f00',
    'International Orange (Engineering)': '#ba160c',
    'International Orange (Golden Gate Bridge)': '#c0362c',
    'Iris': '#5a4fcf',
    'Isabelline': '#f4f0ec',
    'Islamic Green': '#009000',
    'Ivory': '#fffff0',
    'Jade': '#00a86b',
    'Jasmine': '#f8de7e',
    'Jasper': '#d73b3e',
    'Jazzberry Jam': '#a50b5e',
    'Jet': '#343434',
    'Jonquil': '#fada5e',
    'June Bud': '#bdda57',
    'Jungle Green': '#29ab87',
    'Kelly Green': '#4cbb17',
    'Kenyan Copper': '#7c1c05',
    'Khaki (Html/Css) (Khaki)': '#c3b091',
    'Khaki (X11) (Light Khaki)': '#f0e68c',
    'Ku Crimson': '#e8000d',
    'La Salle Green': '#087830',
    'Languid Lavender': '#d6cadd',
    'Lapis Lazuli': '#26619c',
    'Laser Lemon': '#fefe22',
    'Laurel Green': '#a9ba9d',
    'Lava': '#cf1020',
    'Lavender Blue': '#ccccff',
    'Lavender Blush': '#fff0f5',
    'Lavender (Floral)': '#b57edc',
    'Lavender Gray': '#c4c3d0',
    'Lavender Indigo': '#9457eb',
    'Lavender Magenta': '#ee82ee',
    'Lavender Mist': '#e6e6fa',
    'Lavender Pink': '#fbaed2',
    'Lavender Purple': '#967bb6',
    'Lavender Rose': '#fba0e3',
    'Lavender (Web)': '#e6e6fa',
    'Lawn Green': '#7cfc00',
    'Lemon': '#fff700',
    'Lemon Chiffon': '#fffacd',
    'Lemon Lime': '#e3ff00',
    'Licorice': '#1a1110',
    'Light Apricot': '#fdd5b1',
    'Light Blue': '#add8e6',
    'Light Brown': '#b5651d',
    'Light Carmine Pink': '#e66771',
    'Light Coral': '#f08080',
    'Light Cornflower Blue': '#93ccea',
    'Light Crimson': '#f56991',
    'Light Cyan': '#e0ffff',
    'Light Fuchsia Pink': '#f984ef',
    'Light Goldenrod Yellow': '#fafad2',
    'Light Gray': '#d3d3d3',
    'Light Green': '#90ee90',
    'Light Khaki': '#f0e68c',
    'Light Pastel Purple': '#b19cd9',
    'Light Pink': '#ffb6c1',
    'Light Red Ochre': '#e97451',
    'Light Salmon': '#ffa07a',
    'Light Salmon Pink': '#ff9999',
    'Light Sea Green': '#20b2aa',
    'Light Sky Blue': '#87cefa',
    'Light Slate Gray': '#778899',
    'Light Taupe': '#b38b6d',
    'Light Thulian Pink': '#e68fac',
    'Light Yellow': '#ffffe0',
    'Lilac': '#c8a2c8',
    'Lime (Color Wheel)': '#bfff00',
    'Lime Green': '#32cd32',
    'Lime (Web) (X11 Green)': '#00ff00',
    'Limerick': '#9dc209',
    'Lincoln Green': '#195905',
    'Linen': '#faf0e6',
    'Lion': '#c19a6b',
    'Little Boy Blue': '#6ca0dc',
    'Liver': '#534b4f',
    'Lust': '#e62020',
    'Magenta': '#ff00ff',
    'Magenta (Dye)': '#ca1f7b',
    'Magenta (Process)': '#ff0090',
    'Magic Mint': '#aaf0d1',
    'Magnolia': '#f8f4ff',
    'Mahogany': '#c04000',
    'Maize': '#fbec5d',
    'Majorelle Blue': '#6050dc',
    'Malachite': '#0bda51',
    'Manatee': '#979aaa',
    'Mango Tango': '#ff8243',
    'Mantis': '#74c365',
    'Mardi Gras': '#880085',
    'Maroon (Crayola)': '#c32148',
    'Maroon (Html/Css)': '#800000',
    'Maroon (X11)': '#b03060',
    'Mauve': '#e0b0ff',
    'Mauve Taupe': '#915f6d',
    'Mauvelous': '#ef98aa',
    'Maya Blue': '#73c2fb',
    'Meat Brown': '#e5b73b',
    'Medium Aquamarine': '#66ddaa',
    'Medium Blue': '#0000cd',
    'Medium Candy Apple Red': '#e2062c',
    'Medium Carmine': '#af4035',
    'Medium Champagne': '#f3e5ab',
    'Medium Electric Blue': '#035096',
    'Medium Jungle Green': '#1c352d',
    'Medium Lavender Magenta': '#dda0dd',
    'Medium Orchid': '#ba55d3',
    'Medium Persian Blue': '#0067a5',
    'Medium Purple': '#9370db',
    'Medium Red-Violet': '#bb3385',
    'Medium Ruby': '#aa4069',
    'Medium Sea Green': '#3cb371',
    'Medium Slate Blue': '#7b68ee',
    'Medium Spring Bud': '#c9dc87',
    'Medium Spring Green': '#00fa9a',
    'Medium Taupe': '#674c47',
    'Medium Turquoise': '#48d1cc',
    'Medium Tuscan Red': '#79443b',
    'Medium Vermilion': '#d9603b',
    'Medium Violet-Red': '#c71585',
    'Mellow Apricot': '#f8b878',
    'Mellow Yellow': '#f8de7e',
    'Melon': '#fdbcb4',
    'Midnight Blue': '#191970',
    'Midnight Green (Eagle Green)': '#004953',
    'Mikado Yellow': '#ffc40c',
    'Mint': '#3eb489',
    'Mint Cream': '#f5fffa',
    'Mint Green': '#98ff98',
    'Misty Rose': '#ffe4e1',
    'Moccasin': '#faebd7',
    'Mode Beige': '#967117',
    'Moonstone Blue': '#73a9c2',
    'Mordant Red 19': '#ae0c00',
    'Moss Green': '#addfad',
    'Mountain Meadow': '#30ba8f',
    'Mountbatten Pink': '#997a8d',
    'Msu Green': '#18453b',
    'Mulberry': '#c54b8c',
    'Mustard': '#ffdb58',
    'Myrtle': '#21421e',
    'Nadeshiko Pink': '#f6adc6',
    'Napier Green': '#2a8000',
    'Naples Yellow': '#fada5e',
    'Navajo White': '#ffdead',
    'Navy Blue': '#000080',
    'Neon Carrot': '#ffa343',
    'Neon Fuchsia': '#fe4164',
    'Neon Green': '#39ff14',
    'New York Pink': '#d7837f',
    'Non-Photo Blue': '#a4dded',
    'North Texas Green': '#059033',
    'Ocean Boat Blue': '#0077be',
    'Ochre': '#cc7722',
    'Office Green': '#008000',
    'Old Gold': '#cfb53b',
    'Old Lace': '#fdf5e6',
    'Old Lavender': '#796878',
    'Old Mauve': '#673147',
    'Old Rose': '#c08081',
    'Olive': '#808000',
    'Olive Drab #7': '#3c341f',
    'Olive Drab (Web) (Olive Drab #3)': '#6b8e23',
    'Olivine': '#9ab973',
    'Onyx': '#353839',
    'Opera Mauve': '#b784a7',
    'Orange (Color Wheel)': '#ff7f00',
    'Orange Peel': '#ff9f00',
    'Orange-Red': '#ff4500',
    'Orange (Ryb)': '#fb9902',
    'Orange (Web Color)': '#ffa500',
    'Orchid': '#da70d6',
    'Otter Brown': '#654321',
    'Ou Crimson Red': '#900',
    'Outer Space': '#414a4c',
    'Outrageous Orange': '#ff6e4a',
    'Oxford Blue': '#002147',
    'Pakistan Green': '#006600',
    'Palatinate Blue': '#273be2',
    'Palatinate Purple': '#682860',
    'Pale Aqua': '#bcd4e6',
    'Pale Blue': '#afeeee',
    'Pale Brown': '#987654',
    'Pale Carmine': '#af4035',
    'Pale Cerulean': '#9bc4e2',
    'Pale Chestnut': '#ddadaf',
    'Pale Copper': '#da8a67',
    'Pale Cornflower Blue': '#abcdef',
    'Pale Gold': '#e6be8a',
    'Pale Goldenrod': '#eee8aa',
    'Pale Green': '#98fb98',
    'Pale Lavender': '#dcd0ff',
    'Pale Magenta': '#f984e5',
    'Pale Pink': '#fadadd',
    'Pale Plum': '#dda0dd',
    'Pale Red-Violet': '#db7093',
    'Pale Robin Egg Blue': '#96ded1',
    'Pale Silver': '#c9c0bb',
    'Pale Spring Bud': '#ecebbd',
    'Pale Taupe': '#bc987e',
    'Pale Violet-Red': '#db7093',
    'Pansy Purple': '#78184a',
    'Papaya Whip': '#ffefd5',
    'Paris Green': '#50c878',
    'Pastel Blue': '#aec6cf',
    'Pastel Brown': '#836953',
    'Pastel Gray': '#cfcfc4',
    'Pastel Green': '#77dd77',
    'Pastel Magenta': '#f49ac2',
    'Pastel Orange': '#ffb347',
    'Pastel Pink': '#dea5a4',
    'Pastel Purple': '#b39eb5',
    'Pastel Red': '#ff6961',
    'Pastel Violet': '#cb99c9',
    'Pastel Yellow': '#fdfd96',
    'Patriarch': '#800080',
    'Payne Grey': '#536878',
    'Peach': '#ffe5b4',
    'Peach (Crayola)': '#ffcba4',
    'Peach-Orange': '#ffcc99',
    'Peach Puff': '#ffdab9',
    'Peach-Yellow': '#fadfad',
    'Pear': '#d1e231',
    'Pearl': '#eae0c8',
    'Pearl Aqua': '#88d8c0',
    'Pearly Purple': '#b768a2',
    'Peridot': '#e6e200',
    'Periwinkle': '#ccccff',
    'Persian Blue': '#1c39bb',
    'Persian Green': '#00a693',
    'Persian Indigo': '#32127a',
    'Persian Orange': '#d99058',
    'Persian Pink': '#f77fbe',
    'Persian Plum': '#701c1c',
    'Persian Red': '#cc3333',
    'Persian Rose': '#fe28a2',
    'Persimmon': '#ec5800',
    'Peru': '#cd853f',
    'Phlox': '#df00ff',
    'Phthalo Blue': '#000f89',
    'Phthalo Green': '#123524',
    'Piggy Pink': '#fddde6',
    'Pine Green': '#01796f',
    'Pink': '#ffc0cb',
    'Pink Lace': '#ffddf4',
    'Pink-Orange': '#f96',
    'Pink Pearl': '#e7accf',
    'Pink Sherbet': '#f78fa7',
    'Pistachio': '#93c572',
    'Platinum': '#e5e4e2',
    'Plum (Traditional)': '#8e4585',
    'Plum (Web)': '#dda0dd',
    'Portland Orange': '#ff5a36',
    'Powder Blue (Web)': '#b0e0e6',
    'Princeton Orange': '#ff8f00',
    'Prune': '#701c1c',
    'Prussian Blue': '#003153',
    'Psychedelic Purple': '#df00ff',
    'Puce': '#cc8899',
    'Pumpkin': '#ff7518',
    'Purple Heart': '#69359c',
    'Purple (Html/Css)': '#800080',
    'Purple Mountain Majesty': '#9678b6',
    'Purple (Munsell)': '#9f00c5',
    'Purple Pizzazz': '#fe4eda',
    'Purple Taupe': '#50404d',
    'Purple (X11)': '#a020f0',
    'Quartz': '#51484f',
    'Rackley': '#5d8aa8',
    'Radical Red': '#ff355e',
    'Rajah': '#fbab60',
    'Raspberry': '#e30b5d',
    'Raspberry Glace': '#915f6d',
    'Raspberry Pink': '#e25098',
    'Raspberry Rose': '#b3446c',
    'Raw Umber': '#826644',
    'Razzle Dazzle Rose': '#ff33cc',
    'Razzmatazz': '#e3256b',
    'Red': '#ff0000',
    'Red-Brown': '#a52a2a',
    'Red Devil': '#860111',
    'Red (Munsell)': '#f2003c',
    'Red (Ncs)': '#c40233',
    'Red-Orange': '#ff5349',
    'Red (Pigment)': '#ed1c24',
    'Red (Ryb)': '#fe2712',
    'Red-Violet': '#c71585',
    'Redwood': '#ab4e52',
    'Regalia': '#522d80',
    'Resolution Blue': '#002387',
    'Rich Black': '#004040',
    'Rich Brilliant Lavender': '#f1a7fe',
    'Rich Carmine': '#d70040',
    'Rich Electric Blue': '#0892d0',
    'Rich Lavender': '#a76bcf',
    'Rich Lilac': '#b666d2',
    'Rich Maroon': '#b03060',
    'Rifle Green': '#414833',
    'Robin Egg Blue': '#0cc',
    'Rose': '#ff007f',
    'Rose Bonbon': '#f9429e',
    'Rose Ebony': '#674846',
    'Rose Gold': '#b76e79',
    'Rose Madder': '#e32636',
    'Rose Pink': '#f6c',
    'Rose Quartz': '#aa98a9',
    'Rose Taupe': '#905d5d',
    'Rose Vale': '#ab4e52',
    'Rosewood': '#65000b',
    'Rosso Corsa': '#d40000',
    'Rosy Brown': '#bc8f8f',
    'Royal Azure': '#0038a8',
    'Royal Blue (Traditional)': '#002366',
    'Royal Blue (Web)': '#4169e1',
    'Royal Fuchsia': '#ca2c92',
    'Royal Purple': '#7851a9',
    'Royal Yellow': '#fada5e',
    'Rubine Red': '#d10056',
    'Ruby': '#e0115f',
    'Ruby Red': '#9b111e',
    'Ruddy': '#ff0028',
    'Ruddy Brown': '#bb6528',
    'Ruddy Pink': '#e18e96',
    'Rufous': '#a81c07',
    'Russet': '#80461b',
    'Rust': '#b7410e',
    'Rusty Red': '#da2c43',
    'Sacramento State Green': '#00563f',
    'Saddle Brown': '#8b4513',
    'Safety Orange (Blaze Orange)': '#ff6700',
    'Saffron': '#f4c430',
    'Salmon': '#ff8c69',
    'Salmon Pink': '#ff91a4',
    'Sand': '#c2b280',
    'Sand Dune': '#967117',
    'Sandstorm': '#ecd540',
    'Sandy Brown': '#f4a460',
    'Sandy Taupe': '#967117',
    'Sangria': '#92000a',
    'Sap Green': '#507d2a',
    'Sapphire': '#0f52ba',
    'Sapphire Blue': '#0067a5',
    'Satin Sheen Gold': '#cba135',
    'Scarlet': '#ff2400',
    'Scarlet (Crayola)': '#fd0e35',
    'School Bus Yellow': '#ffd800',
    'Screamin Green': '#76ff7a',
    'Sea Blue': '#006994',
    'Sea Green': '#2e8b57',
    'Seal Brown': '#321414',
    'Seashell': '#fff5ee',
    'Selective Yellow': '#ffba00',
    'Sepia': '#704214',
    'Shadow': '#8a795d',
    'Shamrock Green': '#009e60',
    'Shocking Pink': '#fc0fc0',
    'Shocking Pink (Crayola)': '#ff6fff',
    'Sienna': '#882d17',
    'Silver': '#c0c0c0',
    'Sinopia': '#cb410b',
    'Skobeloff': '#007474',
    'Sky Blue': '#87ceeb',
    'Sky Magenta': '#cf71af',
    'Slate Blue': '#6a5acd',
    'Slate Gray': '#708090',
    'Smalt (Dark Powder Blue)': '#039',
    'Smokey Topaz': '#933d41',
    'Smoky Black': '#100c08',
    'Snow': '#fffafa',
    'Spiro Disco Ball': '#0fc0fc',
    'Spring Bud': '#a7fc00',
    'Spring Green': '#00ff7f',
    'St. Patrick Blue': '#23297a',
    'Steel Blue': '#4682b4',
    'Stil De Grain Yellow': '#fada5e',
    'Stizza': '#900',
    'Stormcloud': '#4f666a',
    'Straw': '#e4d96f',
    'Sunglow': '#ffcc33',
    'Sunset': '#fad6a5',
    'Tan': '#d2b48c',
    'Tangelo': '#f94d00',
    'Tangerine': '#f28500',
    'Tangerine Yellow': '#ffcc00',
    'Tango Pink': '#e4717a',
    'Taupe': '#483c32',
    'Taupe Gray': '#8b8589',
    'Tea Green': '#d0f0c0',
    'Tea Rose (Orange)': '#f88379',
    'Tea Rose (Rose)': '#f4c2c2',
    'Teal': '#008080',
    'Teal Blue': '#367588',
    'Teal Green': '#00827f',
    'Telemagenta': '#cf3476',
    'Tenné (Tawny)': '#cd5700',
    'Terra Cotta': '#e2725b',
    'Thistle': '#d8bfd8',
    'Thulian Pink': '#de6fa1',
    'Tickle Me Pink': '#fc89ac',
    'Tiffany Blue': '#0abab5',
    'Tiger Eye': '#e08d3c',
    'Timberwolf': '#dbd7d2',
    'Titanium Yellow': '#eee600',
    'Tomato': '#ff6347',
    'Toolbox': '#746cc0',
    'Topaz': '#ffc87c',
    'Tractor Red': '#fd0e35',
    'Trolley Grey': '#808080',
    'Tropical Rain Forest': '#00755e',
    'True Blue': '#0073cf',
    'Tufts Blue': '#417dc1',
    'Tumbleweed': '#deaa88',
    'Turkish Rose': '#b57281',
    'Turquoise': '#30d5c8',
    'Turquoise Blue': '#00ffef',
    'Turquoise Green': '#a0d6b4',
    'Tuscan Red': '#7c4848',
    'Twilight Lavender': '#8a496b',
    'Tyrian Purple': '#66023c',
    'Ua Blue': '#0033aa',
    'Ua Red': '#d9004c',
    'Ube': '#8878c3',
    'Ucla Blue': '#536895',
    'Ucla Gold': '#ffb300',
    'Ufo Green': '#3cd070',
    'Ultra Pink': '#ff6fff',
    'Ultramarine': '#120a8f',
    'Ultramarine Blue': '#4166f5',
    'Umber': '#635147',
    'Unbleached Silk': '#ffddca',
    'United Nations Blue': '#5b92e5',
    'University Of California Gold': '#b78727',
    'Unmellow Yellow': '#ffff66',
    'Up Forest Green': '#014421',
    'Up Maroon': '#7b1113',
    'Upsdell Red': '#ae2029',
    'Urobilin': '#e1ad21',
    'Usafa Blue': '#004f98',
    'Usc Cardinal': '#990000',
    'Usc Gold': '#ffcc00',
    'Utah Crimson': '#d3003f',
    'Vanilla': '#f3e5ab',
    'Vegas Gold': '#c5b358',
    'Venetian Red': '#c80815',
    'Verdigris': '#43b3ae',
    'Vermilion (Cinnabar)': '#e34234',
    'Vermilion (Plochere)': '#d9603b',
    'Veronica': '#a020f0',
    'Violet': '#8f00ff',
    'Violet-Blue': '#324ab2',
    'Violet (Color Wheel)': '#7f00ff',
    'Violet (Ryb)': '#8601af',
    'Violet (Web)': '#ee82ee',
    'Viridian': '#40826d',
    'Vivid Auburn': '#922724',
    'Vivid Burgundy': '#9f1d35',
    'Vivid Cerise': '#da1d81',
    'Vivid Tangerine': '#ffa089',
    'Vivid Violet': '#9f00ff',
    'Warm Black': '#004242',
    'Waterspout': '#a4f4f9',
    'Wenge': '#645452',
    'Wheat': '#f5deb3',
    'White': '#ffffff',
    'White Smoke': '#f5f5f5',
    'Wild Blue Yonder': '#a2add0',
    'Wild Strawberry': '#ff43a4',
    'Wild Watermelon': '#fc6c85',
    'Wine': '#722f37',
    'Wine Dregs': '#673147',
    'Wisteria': '#c9a0dc',
    'Wood Brown': '#c19a6b',
    'Xanadu': '#738678',
    'Yale Blue': '#0f4d92',
    'Yellow': '#ffff00',
    'Yellow-Green': '#9acd32',
    'Yellow (Munsell)': '#efcc00',
    'Yellow (Ncs)': '#ffd300',
    'Yellow Orange': '#ffae42',
    'Yellow (Process)': '#ffef00',
    'Yellow (Ryb)': '#fefe33',
    'Zaffre': '#0014a8',
    'Zinnwaldite Brown': '#2c1608'
}

# Mappings of normalized hexadecimal color values to color names.
#################################################################

HTML4_HEX_TO_NAMES = _reversedict(HTML4_NAMES_TO_HEX)

CSS2_HEX_TO_NAMES = HTML4_HEX_TO_NAMES

CSS21_HEX_TO_NAMES = _reversedict(CSS21_NAMES_TO_HEX)

CSS3_HEX_TO_NAMES = _reversedict(CSS3_NAMES_TO_HEX)

COLOR_HEXA_HEX_TO_NAMES = _reversedict(COLOR_HEXA_NAMES_TO_HEX)

# CSS3 defines both 'gray' and 'grey', as well as defining either
# variant for other related colors like 'darkgray'/'darkgrey'. For a
# 'forward' lookup from name to hex, this is straightforward, but a
# 'reverse' lookup from hex to name requires picking one spelling.
#
# The way in which _reversedict() generates the reverse mappings will
# pick a spelling based on the ordering of dictionary keys, which
# varies according to the version and implementation of Python in use,
# and in some Python versions is explicitly not to be relied on for
# consistency. So here we manually pick a single spelling that will
# consistently be returned. Since 'gray' was the only spelling
# supported in HTML 4, CSS1, and CSS2, 'gray' and its varients are
# chosen.
CSS3_HEX_TO_NAMES["#a9a9a9"] = "darkgray"
CSS3_HEX_TO_NAMES["#2f4f4f"] = "darkslategray"
CSS3_HEX_TO_NAMES["#696969"] = "dimgray"
CSS3_HEX_TO_NAMES["#808080"] = "gray"
CSS3_HEX_TO_NAMES["#d3d3d3"] = "lightgray"
CSS3_HEX_TO_NAMES["#778899"] = "lightslategray"
CSS3_HEX_TO_NAMES["#708090"] = "slategray"


# Normalization functions.
#################################################################


def normalize_hex(hex_value: str) -> str:
    """
    Normalize a hexadecimal color value to 6 digits, lowercase.

    """
    match = HEX_COLOR_RE.match(hex_value)
    if match is None:
        raise ValueError(
            "'{}' is not a valid hexadecimal color value.".format(hex_value)
        )
    hex_digits = match.group(1)
    if len(hex_digits) == 3:
        hex_digits = "".join(2 * s for s in hex_digits)
    return "#{}".format(hex_digits.lower())


def _normalize_integer_rgb(value: int) -> int:
    """
    Internal normalization function for clipping integer values into
    the permitted range (0-255, inclusive).

    """
    return 0 if value < 0 else 255 if value > 255 else value


def normalize_integer_triplet(rgb_triplet: IntTuple) -> IntegerRGB:
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    """
    return IntegerRGB._make(_normalize_integer_rgb(value) for value in rgb_triplet)


def _normalize_percent_rgb(value: str) -> str:
    """
    Internal normalization function for clipping percent values into
    the permitted range (0%-100%, inclusive).

    """
    value = value.split("%")[0]
    percent = float(value) if "." in value else int(value)

    return "0%" if percent < 0 else "100%" if percent > 100 else "{}%".format(percent)


def normalize_percent_triplet(rgb_triplet: PercentTuple) -> PercentRGB:
    """
    Normalize a percentage ``rgb()`` triplet so that all values are
    within the range 0%-100% inclusive.

    """
    return PercentRGB._make(_normalize_percent_rgb(value) for value in rgb_triplet)


# Conversions from color names to various formats.
#################################################################


def name_to_hex(name: str, spec: str = CSS3) -> str:
    """
    Convert a color name to a normalized hexadecimal color value.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color of that name exists in the given specification,
    ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = name.lower()
    hex_value = {
        CSS2: CSS2_NAMES_TO_HEX,
        CSS21: CSS21_NAMES_TO_HEX,
        CSS3: CSS3_NAMES_TO_HEX,
        HTML4: HTML4_NAMES_TO_HEX,
        COLOR_HEXA: COLOR_HEXA_NAMES_TO_HEX,
    }[spec].get(normalized)
    if hex_value is None:
        raise ValueError(
            "'{name}' is not defined as a named color in {spec}".format(
                name=name, spec=spec
            )
        )
    return hex_value


def name_to_rgb(name: str, spec: str = CSS3) -> IntegerRGB:
    """
    Convert a color name to a 3-tuple of integers suitable for use in
    an ``rgb()`` triplet specifying that color.

    """
    return hex_to_rgb(name_to_hex(name, spec=spec))


def name_to_rgb_percent(name: str, spec: str = CSS3) -> PercentRGB:
    """
    Convert a color name to a 3-tuple of percentages suitable for use
    in an ``rgb()`` triplet specifying that color.

    """
    return rgb_to_rgb_percent(name_to_rgb(name, spec=spec))


# Conversions from hexadecimal color values to various formats.
#################################################################


def hex_to_name(hex_value: str, spec: str = CSS3) -> str:
    """
    Convert a hexadecimal color value to its corresponding normalized
    color name, if any such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color name for the value is found in the given
    specification, ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = normalize_hex(hex_value)
    name = {
        CSS2: CSS2_HEX_TO_NAMES,
        CSS21: CSS21_HEX_TO_NAMES,
        CSS3: CSS3_HEX_TO_NAMES,
        HTML4: HTML4_HEX_TO_NAMES,
        COLOR_HEXA: COLOR_HEXA_HEX_TO_NAMES,
    }[spec].get(normalized)
    if name is None:
        raise ValueError("'{}' has no defined color name in {}".format(hex_value, spec))
    return name


def hex_to_rgb(hex_value: str) -> IntegerRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.

    """
    int_value = int(normalize_hex(hex_value)[1:], 16)
    return IntegerRGB(int_value >> 16, int_value >> 8 & 0xFF, int_value & 0xFF)


def hex_to_rgb_percent(hex_value: str) -> PercentRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of percentages
    suitable for use in an ``rgb()`` triplet representing that color.

    """
    return rgb_to_rgb_percent(hex_to_rgb(hex_value))


# Conversions from  integer rgb() triplets to various formats.
#################################################################


def rgb_to_name(rgb_triplet: IntTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return hex_to_name(rgb_to_hex(normalize_integer_triplet(rgb_triplet)), spec=spec)


def rgb_to_hex(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.

    """
    return "#{:02x}{:02x}{:02x}".format(*normalize_integer_triplet(rgb_triplet))


def rgb_to_rgb_percent(rgb_triplet: IntTuple) -> PercentRGB:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of percentages suitable for use in
    representing that color.

    This function makes some trade-offs in terms of the accuracy of
    the final representation; for some common integer values,
    special-case logic is used to ensure a precise result (e.g.,
    integer 128 will always convert to '50%', integer 32 will always
    convert to '12.5%'), but for all other values a standard Python
    ``float`` is used and rounded to two decimal places, which may
    result in a loss of precision for some values.

    """
    # In order to maintain precision for common values,
    # special-case them.
    specials = {
        255: "100%",
        128: "50%",
        64: "25%",
        32: "12.5%",
        16: "6.25%",
        0: "0%",
    }
    return PercentRGB._make(
        specials.get(d, "{:.02f}%".format(d / 255.0 * 100))
        for d in normalize_integer_triplet(rgb_triplet)
    )


# Conversions from percentage rgb() triplets to various formats.
#################################################################


def rgb_percent_to_name(rgb_percent_triplet: PercentTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return rgb_to_name(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet)), spec=spec
    )


def rgb_percent_to_hex(rgb_percent_triplet: PercentTuple) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal color value for that
    color.

    """
    return rgb_to_hex(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet))
    )


def _percent_to_integer(percent: str) -> int:
    """
    Internal helper for converting a percentage value to an integer
    between 0 and 255 inclusive.

    """
    return int(round(float(percent.split("%")[0]) / 100 * 255))


def rgb_percent_to_rgb(rgb_percent_triplet: PercentTuple) -> IntegerRGB:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of integers suitable for use in
    representing that color.

    Some precision may be lost in this conversion. See the note
    regarding precision for ``rgb_to_rgb_percent()`` for details.

    """
    return IntegerRGB._make(
        map(_percent_to_integer, normalize_percent_triplet(rgb_percent_triplet))
    )


# HTML5 color algorithms.
#################################################################

# These functions are written in a way that may seem strange to
# developers familiar with Python, because they do not use the most
# efficient or idiomatic way of accomplishing their tasks. This is
# because, for compliance, these functions are written as literal
# translations into Python of the algorithms in HTML5.
#
# For ease of understanding, the relevant steps of the algorithm from
# the standard are included as comments interspersed in the
# implementation.


def html5_parse_simple_color(input: str) -> HTML5SimpleColor:
    """
    Apply the simple color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    #
    # 2. If input is not exactly seven characters long, then return an
    #    error.
    if not isinstance(input, str) or len(input) != 7:
        raise ValueError(
            "An HTML5 simple color must be a Unicode string "
            "exactly seven characters long."
        )

    # 3. If the first character in input is not a U+0023 NUMBER SIGN
    #    character (#), then return an error.
    if not input.startswith("#"):
        raise ValueError(
            "An HTML5 simple color must begin with the " "character '#' (U+0023)."
        )

    # 4. If the last six characters of input are not all ASCII hex
    #    digits, then return an error.
    if not all(c in string.hexdigits for c in input[1:]):
        raise ValueError(
            "An HTML5 simple color must contain exactly six ASCII hex digits."
        )

    # 5. Let result be a simple color.
    #
    # 6. Interpret the second and third characters as a hexadecimal
    #    number and let the result be the red component of result.
    #
    # 7. Interpret the fourth and fifth characters as a hexadecimal
    #    number and let the result be the green component of result.
    #
    # 8. Interpret the sixth and seventh characters as a hexadecimal
    #    number and let the result be the blue component of result.
    #
    # 9. Return result.
    return HTML5SimpleColor(
        int(input[1:3], 16), int(input[3:5], 16), int(input[5:7], 16)
    )


def html5_serialize_simple_color(simple_color: IntTuple) -> str:
    """
    Apply the serialization algorithm for a simple color from section
    2.4.6 of HTML5.

    """
    red, green, blue = simple_color

    # 1. Let result be a string consisting of a single "#" (U+0023)
    #    character.
    result = "#"

    # 2. Convert the red, green, and blue components in turn to
    #    two-digit hexadecimal numbers using lowercase ASCII hex
    #    digits, zero-padding if necessary, and append these numbers
    #    to result, in the order red, green, blue.
    format_string = "{:02x}"
    result += format_string.format(red)
    result += format_string.format(green)
    result += format_string.format(blue)

    # 3. Return result, which will be a valid lowercase simple color.
    return result


def html5_parse_legacy_color(input: str) -> HTML5SimpleColor:
    """
    Apply the legacy color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    if not isinstance(input, str):
        raise ValueError(
            "HTML5 legacy color parsing requires a Unicode string as input."
        )

    # 2. If input is the empty string, then return an error.
    if input == "":
        raise ValueError("HTML5 legacy color parsing forbids empty string as a value.")

    # 3. Strip leading and trailing whitespace from input.
    input = input.strip()

    # 4. If input is an ASCII case-insensitive match for the string
    #    "transparent", then return an error.
    if input.lower() == "transparent":
        raise ValueError(
            u'HTML5 legacy color parsing forbids "transparent" as a value.'
        )

    # 5. If input is an ASCII case-insensitive match for one of the
    #    keywords listed in the SVG color keywords section of the CSS3
    #    Color specification, then return the simple color
    #    corresponding to that keyword.
    keyword_hex = CSS3_NAMES_TO_HEX.get(input.lower())
    if keyword_hex is not None:
        return html5_parse_simple_color(keyword_hex)

    # 6. If input is four characters long, and the first character in
    #    input is a "#" (U+0023) character, and the last three
    #    characters of input are all ASCII hex digits, then run these
    #    substeps:
    if (
            len(input) == 4
            and input.startswith("#")
            and all(c in string.hexdigits for c in input[1:])
    ):
        # 1. Let result be a simple color.
        #
        # 2. Interpret the second character of input as a hexadecimal
        #    digit; let the red component of result be the resulting
        #    number multiplied by 17.
        #
        # 3. Interpret the third character of input as a hexadecimal
        #    digit; let the green component of result be the resulting
        #    number multiplied by 17.
        #
        # 4. Interpret the fourth character of input as a hexadecimal
        #    digit; let the blue component of result be the resulting
        #    number multiplied by 17.
        result = HTML5SimpleColor(
            int(input[1], 16) * 17, int(input[2], 16) * 17, int(input[3], 16) * 17
        )

        # 5. Return result.
        return result

    # 7. Replace any characters in input that have a Unicode code
    #    point greater than U+FFFF (i.e. any characters that are not
    #    in the basic multilingual plane) with the two-character
    #    string "00".
    input = "".join("00" if ord(c) > 0xFFFF else c for c in input)

    # 8. If input is longer than 128 characters, truncate input,
    #    leaving only the first 128 characters.
    if len(input) > 128:
        input = input[:128]

    # 9. If the first character in input is a "#" (U+0023) character,
    #    remove it.
    if input.startswith("#"):
        input = input[1:]

    # 10. Replace any character in input that is not an ASCII hex
    #     digit with the character "0" (U+0030).
    input = "".join(c if c in string.hexdigits else "0" for c in input)

    # 11. While input's length is zero or not a multiple of three,
    #     append a "0" (U+0030) character to input.
    while (len(input) == 0) or (len(input) % 3 != 0):
        input += "0"

    # 12. Split input into three strings of equal length, to obtain
    #     three components. Let length be the length of those
    #     components (one third the length of input).
    length = int(len(input) / 3)
    red = input[:length]
    green = input[length: length * 2]
    blue = input[length * 2:]

    # 13. If length is greater than 8, then remove the leading
    #     length-8 characters in each component, and let length be 8.
    if length > 8:
        red, green, blue = (red[length - 8:], green[length - 8:], blue[length - 8:])
        length = 8

    # 14. While length is greater than two and the first character in
    #     each component is a "0" (U+0030) character, remove that
    #     character and reduce length by one.
    while (length > 2) and (red[0] == "0" and green[0] == "0" and blue[0] == "0"):
        red, green, blue = (red[1:], green[1:], blue[1:])
        length -= 1

    # 15. If length is still greater than two, truncate each
    #     component, leaving only the first two characters in each.
    if length > 2:
        red, green, blue = (red[:2], green[:2], blue[:2])

    # 16. Let result be a simple color.
    #
    # 17. Interpret the first component as a hexadecimal number; let
    #     the red component of result be the resulting number.
    #
    # 18. Interpret the second component as a hexadecimal number; let
    #     the green component of result be the resulting number.
    #
    # 19. Interpret the third component as a hexadecimal number; let
    #     the blue component of result be the resulting number.
    #
    # 20. Return result.
    return HTML5SimpleColor(int(red, 16), int(green, 16), int(blue, 16))
