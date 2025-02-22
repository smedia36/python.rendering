# Drawing multiple frames for a rotating sand clock


layers: list = []
for i in range(0, 24, 1):
    layers.append(layer(f"sand_clock{i}"))
    
r = rect((0, 0), (72, 72), fill="#303e52", stroke="#303e52", stroke_width=0)

lines = group()
lines.append(line((0, 0), (19, 0), stroke="white", stroke_width=1.5))
lines.append(line((1 / 2, 0 + 1.5 / 2), (1 / 2, 8), stroke="white", stroke_width=1))
lines.append(line((0 + 0.373, 8 - 0.334), (12, 21), stroke="white", stroke_width=1))

d0 = duplicate(lines, transform="translate(19, 0)")
d1 = duplicate(lines, transform="translate(0, 20.77)")
d2 = duplicate(lines, transform="translate(19, 20.77)")

apply_action("object-flip-horizontal", [d0])
apply_action("object-flip-vertical", [d1])
apply_action("object-flip-horizontal; object-flip-vertical", [d2])

gr = group()
gr.extend([lines, d0, d1, d2])

apply_action('object-align:hcenter drawing;object-align:vcenter drawing', [r, gr])
layers[0].extend([r, gr])

for i in range(1, 24, 1):
    gr_d = duplicate(gr, transform=f"translate({i * 180}, 9.808) rotate(-{i * 15})")
    layers[i].append(gr_d)
    r_i = rect((0, 0), (72, 72), fill="#303e52", stroke="#303e52", stroke_width=0)
    apply_action('object-align:hcenter drawing;object-align:vcenter drawing', [r_i, gr_d])
    layers[i].extend([r_i, gr_d])
