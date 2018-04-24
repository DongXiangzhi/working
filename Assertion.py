"""
try:
except

assertion

logging

debugging
"""


marked2nd={'ns': 'green', 'ew': 'red'}
mission16th={'ns': 'red', 'ew': 'green'}


def switchLights(stopLight):
    for key in stopLight.keys():
        if stopLight[key]=='green':
            stopLight[key]='yellow'
        if stopLight[key]=='yellow':
            stopLight[key]='red'
        if stopLight[key]=='red':
            stopLight[key]='green'
    assert 'red' in stopLight.values(),\
        '不能都是绿灯'+str(stopLight)

# switchLights(marked2nd)
switchLights(mission16th)