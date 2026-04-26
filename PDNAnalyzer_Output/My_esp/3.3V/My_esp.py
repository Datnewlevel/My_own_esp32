designFile = "C:/Users/Public/Documents/Altium/My_own_esp32(2)/PDNAnalyzer_Output/My_esp/odb.tgz"

powerNets = ["3.3V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("U1", "2") ],
"ground_pins": [ ("U1", "1") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("U8", "2") ],
"ground_pins": [ ("U8", "1"), ("U8", "15"), ("U8", "38"), ("U8", "pdna_pin_39_1"), ("U8", "pdna_pin_39_2"), ("U8", "pdna_pin_39_3"), ("U8", "pdna_pin_39_4"), ("U8", "pdna_pin_39_5"), ("U8", "pdna_pin_39_6"), ("U8", "pdna_pin_39_7"), ("U8", "pdna_pin_39_8"), ("U8", "pdna_pin_39_9") ],
"current": 0.0001,
"Rpin": 1846.15384615385,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GND', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.3, 'Thickness': 0.0014986},
        {'name': 'PWR', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
