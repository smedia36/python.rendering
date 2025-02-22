# Function to draw an arbitrary number of combinations for a 2D fence


def fence(struts: int,
          height: float,
          gap: float,
          legs: int,
          stroke: str='black',
          stroke_width: float=1):
    objs: list = []
    for i in range(0, struts, 1):
        objs.append(line((0 + stroke_width / 2 + i * gap, 0), (0 + stroke_width / 2 + i * gap, height), stroke=stroke, stroke_width=stroke_width))
        if legs == struts:
            objs.append(line((0 + stroke_width / 2 + i * gap, height), (0 + stroke_width / 2 + i * gap, 0 + height + height / 5), stroke=stroke, stroke_width=stroke_width))

    if legs > 0 and legs != struts:
        width_total: float = i * gap + stroke_width
        gap_legs: float = width_total / legs         
        for l in range(0, legs, 1): 
            objs.append(line((0 + l * gap_legs + stroke_width / 2, 0 + height), (0 + l * gap_legs + stroke_width / 2, 0 + height + height / 5), stroke=stroke, stroke_width=stroke_width))

    objs.append(line((0, 0 + stroke_width / 2), (i * gap + stroke_width, 0 + stroke_width / 2), stroke=stroke, stroke_width=stroke_width))
    objs.append(line((0, 0 - stroke_width / 2 + height), (i * gap + stroke_width, 0 - stroke_width / 2 + height), stroke=stroke, stroke_width=stroke_width))
    group(objs)

