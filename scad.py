import copy
import opsc
import oobb
import oobb_base
import math

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "drive_shaft_output_inner"
        #filter = "inner_rotor_main"
        #filter = "outer_rotor_main"
        #filter = "outer_rotor_outer_drive_shaft"
        #filter = "inner_rotor_drive_shaft"
        filter = "outer_rotor_spacer"
        #filter = ["outer_rotor_outer_drive_shaft", "outer_rotor_inner_drive_shaft", "inner_rotor_drive_shaft"]

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]        
        #kwargs["modes"] = ["3dpr"]
        kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 12
        kwargs["height"] = 12
        kwargs["thickness"] = 6

    # project_variables
    if True:
        #cycloidal ones
        kwargs["lobe_number"] = 79        
        kwargs["lobe_radius"] = 3/2
        kwargs["radius_offset"] = 0.75
        kwargs["radius_output_drive_pins"] = 2.5
        #size ones
        thickness_inner_rotor = 9
        kwargs["thickness_inner_rotor"] = thickness_inner_rotor
        thickness_outer_rotor = 12
        kwargs["thickness_outer_rotor"] = thickness_outer_rotor
        # output shaft
        output_shaft_pin_distance = [15,15] # oobb_3 at 45 degrees
        kwargs["output_shaft_pin_distance"] = output_shaft_pin_distance

    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_oobb_gearbox_cycloidal_working_version_2"
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = thickness_inner_rotor
        part["kwargs"] = p3
        part["name"] = "inner_rotor_drive_shaft"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)        
        p3["thickness"] = thickness_outer_rotor
        part["kwargs"] = p3
        part["name"] = "outer_rotor_inner_drive_shaft"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)        
        p3["thickness"] = thickness_outer_rotor
        part["kwargs"] = p3        
        part["name"] = "outer_rotor_outer_drive_shaft"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 3
        part["kwargs"] = p3
        part["name"] = "inner_rotor_main"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 3 
        part["kwargs"] = p3
        part["name"] = "outer_rotor_main"
        parts.append(part)

        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 3 
        part["kwargs"] = p3
        part["name"] = "outer_rotor_spacer"
        parts.append(part)
        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")            
            if not isinstance(filter, list):
                filter = [filter]
            generate = False
            for f in filter:
                if f in name:
                    generate = True
            if generate:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_outer_rotor_inner_drive_shaft(thing, **kwargs):
    p3 = copy.deepcopy(kwargs)
    p3["center_offset"] = False
    get_inner_rotor_drive_shaft(thing, **p3)

def get_inner_rotor_drive_shaft(thing, **kwargs):
    center_offset = kwargs.get("center_offset", True)

    thickness = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    if center_offset:
        radius_offset = kwargs.get("radius_offset", 1.5)
    else:
        radius_offset = 0
    
    depth = thickness

    drive_shaft_input_radius = 28/2    

    #add _cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = drive_shaft_input_radius
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)     
    pos1[0] += radius_offset
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add_bearing
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_bearing"
    p3["bearing"] = "6705"
    pos1 = copy.deepcopy(pos)
    pos1[0] += radius_offset    
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    #add center hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m6"
    pos1 = copy.deepcopy(pos)
    pos1[0] += 0
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    
    #add joining holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3"
    p3["depth"] = depth
    p3["nut_include"] = True
    p3["zz"] = "bottom"
    poss = []
    if True:
        offset = 7.5
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth/2    
        pos13 = copy.deepcopy(pos1)
        pos13[1] += offset
        poss.append(pos13)
        pos14 = copy.deepcopy(pos1)
        pos14[1] += -offset
        poss.append(pos14)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3"
    p3["depth"] = depth
    p3["nut_include"] = True
    p3["zz"] = "top"
    p3["rot"] = [0,180,0]
    poss = []
    if True:
        offset = 7.5
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth/2    
        pos11 = copy.deepcopy(pos1)
        #do all four permutations
        pos11[0] += offset
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -offset
        poss.append(pos12)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add oobb holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"
    p3["depth"] = depth
    poss = []
    if True:
        offset = 5.303        
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth/2
        pos11 = copy.deepcopy(pos1)
        pos11[0] += offset
        pos11[1] += offset
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -offset
        pos12[1] += offset
        poss.append(pos12)
        pos13 = copy.deepcopy(pos1)
        pos13[0] += offset
        pos13[1] += -offset
        poss.append(pos13)
        pos14 = copy.deepcopy(pos1)
        pos14[0] += -offset
        pos14[1] += -offset
        poss.append(pos14)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
def get_outer_rotor_outer_drive_shaft(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20
    depth = kwargs.get("thickness", 3)

    #add _cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = 55/2
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add_bearing
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_bearing"
    p3["bearing"] = "6810"
    pos1 = copy.deepcopy(pos)      
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add_bearing
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_bearing"
    p3["bearing"] = "6705"
    pos1 = copy.deepcopy(pos)      
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    
    #add joining holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3"
    p3["depth"] = depth
    p3["nut_include"] = True
    p3["zz"] = "bottom"
    poss = []
    if True:
        offset = 20
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth/2  
        xy = []
        xy.append([18.478,7.654,0])  
        xy.append([7.654,-18.478,0])
        xy.append([-18.478,-7.654,0])
        xy.append([-7.654,18.478,0])
        for p in xy:
            pos11 = copy.deepcopy(pos1)
            pos11[0] += p[0]
            pos11[1] += p[1]
            pos11[2] += p[2]
            poss.append(pos11)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)    

    
    #add oobb holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"        
    poss = []
    if True:
        pos1 = copy.deepcopy(pos)        
        xy = []
        xy.append([22.5,0,0])  
        xy.append([0,22.5,0])
        xy.append([-22.5,0,0])
        xy.append([0,-22.5,0])
        for p in xy:
            pos11 = copy.deepcopy(pos1)
            pos11[0] += p[0]
            pos11[1] += p[1]
            pos11[2] += p[2]
            poss.append(pos11)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)   
    
    #nuts
    p4 = copy.deepcopy(p3)
    p4["shape"] = f"oobb_nut" 
    p4["zz"] = "middle"
    poss = []
    if True:
        pos1 = copy.deepcopy(pos)        
        xy = []
        xy.append([22.5,0,0]) 
        xy.append([-22.5,0,0])
        for p in xy:
            pos11 = copy.deepcopy(pos1)
            pos11[0] += p[0]
            pos11[1] += p[1]
            pos11[2] += p[2]
            poss.append(pos11)
    p4["rot"] = [0,0,360/12]
    p4["pos"] = poss
    #p4["overhang"] = True # not needed here and not quite working in opsc
    p4["m"] = "#"
    oobb_base.append_full(thing,**p4)
    p4 = copy.deepcopy(p3)
    p4["shape"] = f"oobb_nut" 
    p4["zz"] = "middle"
    poss = []
    if True:
        pos1 = copy.deepcopy(pos)        
        xy = []
        xy.append([0,22.5,0]) 
        xy.append([0,-22.5,0])
        for p in xy:
            pos11 = copy.deepcopy(pos1)
            pos11[0] += p[0]
            pos11[1] += p[1]
            pos11[2] += p[2]
            poss.append(pos11)
    #p4["rot"] = [0,0,360/12]
    p4["pos"] = poss
    #p4["overhang"] = True # not needed here and not quite working in opsc
    p4["m"] = "#"
    oobb_base.append_full(thing,**p4)



    #add drive pins    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m2d5"
    shift_screw = 6
    p3["depth"] = depth - shift_screw
    p3["clearance"] = "top"
    p3["nut_include"] = True
    p3["zz"] = "top"
    p3["rot"] = [0,180,0]
    poss = []
    if True:        
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth/2 + depth  - shift_screw
        xy = []
        outer_rotor_outer_drive_shaft = kwargs.get("output_shaft_pin_distance", 0)
        shift = outer_rotor_outer_drive_shaft
        
        xy.append([shift[0],shift[1],0])
        xy.append([-shift[0],shift[1],0])
        xy.append([-shift[0],-shift[1],0])
        xy.append([shift[0],-shift[1],0])
        for p in xy:
            pos11 = copy.deepcopy(pos1)
            pos11[0] += p[0]
            pos11[1] += p[1]
            pos11[2] += p[2]
            poss.append(pos11)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3) 

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 100
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)


        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
def get_outer_rotor_main(thing, **kwargs):
 
    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    lobe_radius = kwargs.get("lobe_radius", 6/2)
    lobe_number = kwargs.get("lobe_number", 6)
    lobe_number += 1
    radius_offset = kwargs.get("radius_offset", 1.5)
    radius_pin = kwargs.get("lobe_radius", 6/2)
    depth = kwargs.get("thickness", 3)

    outer_rotor_radius = lobe_number*radius_offset + radius_pin    
    


    #add _cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = outer_rotor_radius + 5
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)     
    p3["pos"] = pos1
    p3["zz"] = "bottom"
    oobb_base.append_full(thing,**p3)

    #add wing oobb parts
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"
    p3["width"] = 11
    p3["height"] = 1
    p3["depth"] = depth
    p3["holes"] = ["top","bottom"]    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    p4 = copy.deepcopy(p3)
    p4["shape"] = f"oobb_holes"
    #p4["m"] = "#"
    oobb_base.append_full(thing,**p4)
    
    #add wing oobb parts
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"
    p3["width"] = 1
    p3["height"] = 11
    p3["depth"] = depth
    p3["holes"] = ["left","right"]    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    p4 = copy.deepcopy(p3)
    p4["shape"] = f"oobb_holes"
    #p4["m"] = "#"
    oobb_base.append_full(thing,**p4)
    
    #add pins
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m6"
    p3["depth"] = depth
    if lobe_radius == 3/2:
        p3["radius_name"] = "m3"
    
    
    offset = outer_rotor_radius
    poss = []
    posa = copy.deepcopy(pos)
    posa[2] += -depth/2
    for i in range(lobe_number+1):
        pos1 = copy.deepcopy(posa)
        pos1[0] += offset * math.cos(i * 2 * math.pi / (lobe_number))
        pos1[1] += offset * math.sin(i * 2 * math.pi / (lobe_number))
        pos1[2] += depth/2
        poss.append(pos1)   
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add 6810 bearing
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_bearing"
    p3["bearing"] = "6810"
    p3["exclude_clearance"] = True
    pos1 = copy.deepcopy(pos)
    pos1[2] += -20
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add bearing plate connection
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3"
    p3["depth"] = 25
    p3["nut_include"] = False
    p3["zz"] = "top"
    poss = []
    if True:
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth
        pos11 = copy.deepcopy(pos1)
        pos11[0] += 22.5
        pos11[1] += 30
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -22.5
        pos12[1] += -30
        poss.append(pos12)
        p3["pos"] = poss
        pos13 = copy.deepcopy(pos1)
        pos13[0] += 30
        pos13[1] += -22.5
        poss.append(pos13)
        pos14 = copy.deepcopy(pos1)
        pos14[0] += -30
        pos14[1] += 22.5
        poss.append(pos14)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

def get_outer_rotor_spacer(thing, **kwargs):
 
    depth = kwargs.get("thickness", 3)
    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add main_cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = 55/2
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)     
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add dount hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = 30/2
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)     
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    

    #add bearing plate connection
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"    
    poss = []
    spacing = [15.91,15.91]
    if True:
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth
        pos11 = copy.deepcopy(pos1)
        pos11[0] += spacing[0]
        pos11[1] += spacing[1]
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -spacing[0]
        pos12[1] += -spacing[1]
        poss.append(pos12)
        pos13 = copy.deepcopy(pos1)
        pos13[0] += spacing[0]
        pos13[1] += -spacing[1]
        poss.append(pos13)
        pos14 = copy.deepcopy(pos1)
        pos14[0] += -spacing[0]
        pos14[1] += spacing[1]
        poss.append(pos14)        
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add 12 mm spacer holes at 0,22.5 etc
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius"] = 12/2
    
    poss = []
    spacing = 22.5
    if True:
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth
        pos11 = copy.deepcopy(pos1)
        pos11[0] += spacing        
        pos11[1] += 0
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -spacing
        pos12[1] += 0
        poss.append(pos12)
        pos13 = copy.deepcopy(pos1)
        pos13[0] += 0
        pos13[1] += spacing
        poss.append(pos13)
        pos14 = copy.deepcopy(pos1)
        pos14[0] += 0
        pos14[1] += -spacing
        poss.append(pos14)
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

def get_inner_rotor_main(thing, **kwargs):
  
    width = kwargs.get("width", 12)
    pos = kwargs.get("pos", [0, 0, 0])
    lobe_number = kwargs.get("lobe_number", 6)
    radius_offset = kwargs.get("radius_offset", 1.5)
    radius_pin = kwargs.get("lobe_radius", 6/2)
    radius_output_drive_pins = kwargs.get("radius_output_drive_pins", 2.5)
    depth = kwargs.get("thickness", 8)
    prepare_print = kwargs.get("prepare_print", True)

    

    #add _cycloid
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"cycloid"
    p3["lobe_number"] = lobe_number
    p3["radius_offset"] = radius_offset
    p3["radius_pin"] = radius_pin
    p3["offset"] = -0.25
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos) 
    pos1[2] += -depth/2   
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add center bearing
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_bearing"
    p3["bearing"] = "6705"
    pos1 = copy.deepcopy(pos)    
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    bearing = False

    #add output shaft bearings
    output_shaft_pin_distance = kwargs.get("output_shaft_pin_distance", 0)
    if True:
        poss = []
        pos1 = copy.deepcopy(pos)    
        pos1[2] += 0
        pos11 = copy.deepcopy(pos1)
        pos11[0] += output_shaft_pin_distance[0]
        pos11[1] += output_shaft_pin_distance[1]
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -output_shaft_pin_distance[0]
        pos12[1] += -output_shaft_pin_distance[1]
        pos13 = copy.deepcopy(pos1)
        pos13[1] += output_shaft_pin_distance[1]
        pos13[0] += -output_shaft_pin_distance[0]
        pos14 = copy.deepcopy(pos1)
        pos14[1] += -output_shaft_pin_distance[1]
        pos14[0] += output_shaft_pin_distance[0]
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        
    if bearing:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_bearing"
        #p3["bearing"] = "606"
        p3["bearing"] = "676"
        p3["pos"] = poss
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    else:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"        
        r = (radius_output_drive_pins + (radius_offset * 2))/2 
        p3["radius"] = r
        p3["pos"] = poss
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

    #add connecting screws
    b = "6705"
    w = 3
    h = 3    
    t = 9        
    size="oobb"
    item = {"type": "bearing_plate", 
            "width": w, 
            "height": h, 
            "thickness": t, 
            "bearing": b,
            "size": size, 
            "extra":"missing_middle_3_mm",
            "just_screws": True}
    thing_2 = oobb_base.get_thing_from_dict(item)
    thing["components"].append(thing_2["components"])
    

    


    if False: #prepare_print:
        # add copy with a twist
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += width * 15
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

        #add output shaft pins add slice
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

















###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]
    func(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)