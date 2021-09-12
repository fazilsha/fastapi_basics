blocks =[
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": False, "school": True, "store": False}]

def facility_req(requirements):
    optimal =[]
    for block in range(len(blocks)):
        for _ in blocks[block]:
            for req in requirements:
                if blocks[block][req]:
                    

requirements = [ "gym", "school", "store" ]