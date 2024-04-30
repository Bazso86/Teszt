import ezdxf
from ezdxf import colors

LENGHT = 720 / 2
DEPTH = 250
HIGHT = 958 / 2
KFACTOR = 0.00625
BEND = 30
SHEET_THICKNESS = 1
BEND_NUMBER = 1
CORNER = 0.5938
CHAMFER = 3.01

def calculation_1(a :int , b :int , c :int , d :int ):
    """
    This function calculates X or Y coordinates

    Parameters:
        a (int): Lenght, depth or hight
        b (int): Sheet thickness
        c (int): Bend number
        d (int): Kfactor
"""
    return a  - b * c - d * c

hight_sheet_size = calculation_1 ( HIGHT, SHEET_THICKNESS, BEND_NUMBER, KFACTOR) 
lenght_sheet_size = calculation_1 (LENGHT, SHEET_THICKNESS, BEND_NUMBER, KFACTOR)
bend_sheet_size = calculation_1(BEND,SHEET_THICKNESS, BEND_NUMBER, KFACTOR)
depth_sheet_size = calculation_1 (DEPTH, SHEET_THICKNESS, BEND_NUMBER, KFACTOR)

y_0 = 0
x_0 = 0
y_1 = hight_sheet_size
x_1 = lenght_sheet_size
y_2 = y_1 + bend_sheet_size
x_2 = x_1 - bend_sheet_size
y_3 = y_2 - CHAMFER
x_3 = x_2 + 2 * bend_sheet_size
y_4 = y_1 - CORNER
x_4 = x_3 + depth_sheet_size - CHAMFER
y_5 = y_4 - CHAMFER
x_5 = x_4 + CHAMFER 
x_6 = x_5 + bend_sheet_size + CORNER -CHAMFER
x_7 = x_6 + CHAMFER


# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")




# paperspace layout or block definition).  
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...() 
msp.add_line((x_0, y_2), (x_2, y_2), dxfattribs={"color": colors.WHITE})
msp.add_line((x_2, y_2), (x_1, y_1), dxfattribs={"color": colors.WHITE})
msp.add_line((x_1, y_1), (x_3, y_2), dxfattribs={"color": colors.WHITE})
msp.add_line((x_3, y_2), (x_4, y_2), dxfattribs={"color": colors.WHITE})
msp.add_line((x_4, y_2), (x_5, y_3), dxfattribs={"color": colors.WHITE})
msp.add_line((x_5, y_3), (x_5, y_4), dxfattribs={"color": colors.WHITE})
msp.add_line((x_5, y_4), (x_6, y_4), dxfattribs={"color": colors.WHITE})
msp.add_line((x_6, y_4), (x_7, y_5), dxfattribs={"color": colors.WHITE})
msp.add_line((x_7, y_5), (x_7, y_0), dxfattribs={"color": colors.WHITE})

# Save the DXF document.
doc.saveas("test.dxf")