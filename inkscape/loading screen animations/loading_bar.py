# Drawing multiple frames of a progressing loading bar

fill: str = "#303e52"
stroke: str = "white"

for i in range(0, 10, 1):
    l = layer(f"loading_bar{i}")
    frame = rect((0 + i * 120, 0), (101 + i * 120, 15), fill=fill, stroke=stroke, stroke_width=1)
    l.append(frame)
    for j in range(0, i + 1, 1):
        loading_bar = rect((1 + i * 120 + j * 10, 1), (10 + i * 120 + j * 10, 14), fill="white", stroke=stroke, stroke_width=0)
        l.append(loading_bar)
