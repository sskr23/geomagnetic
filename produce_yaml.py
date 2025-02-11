import yaml

example = {
    'FAST@TA1': {'elevation': 15.1, 'azimuth': 89.7, 'location': 'Utah-BRM'},
    'FAST@TA2': {'elevation': 15.1, 'azimuth': 59.76, 'location': 'Utah-BRM'},
    'FAST@TA3': {'elevation': 14.9, 'azimuth': 29.95, 'location': 'Utah-BRM'}
    }
with open('example.yaml','w')as f:
    yaml.dump(example, f, default_flow_style=False, allow_unicode=True)


example2 = {
    'Utah-BRM': {
        "WWM2020": {'alt':80,'az':90, 'declination':90,'azimuth':80,'intensity':90},
        "IRGF": {}
        }
    }

example4 = {
    "Utah-BR": {"elevation": 1404, "altitude", "azimuth"}
}

with open('example2.yaml','w')as f:
    yaml.dump(example2, f, default_flow_style=False, allow_unicode=True)

example3 = {'Telescope pointing':example,'Magnetic field':{'Utah':example2}}
with open('example3.yaml','w')as f:
    yaml.dump(example3, f, default_flow_style=False, allow_unicode=True) 


"""
Ladislav Chytka
  9月25日 17:47
Alt:+015° 38' 14.89"
Az: +235° 45' 53.81"


Ladislav Chytka
  9月27日 18:37
49.9130672N, 14.7820616E

"""