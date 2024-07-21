from solid import cylinder, scad_render, rotate
from solid.utils import left, forward, up
from math import sin, cos, pi, sqrt


d = []
n = 20

for i in range(n):
    d.append(
        left(sin(i * pi * 2 / n) * n / 1.5)(
            forward(cos(i * pi * 2 / n) * n / 1.5)(
                rotate([0, 0, 90])(
                    rotate([30 * cos(i * pi * 2 / n), 30 * sin(i * pi * 2 / n), 0])(
                        cylinder(2, 10, segments=20) - up(0.5)(cylinder(1.5, 10, segments=20))
                    )
                )
            )
        )
    )

d.append(
    up(-1.1)(up(0.1)(cylinder(n / 1.5 + 2, 1.4, segments=20)) - cylinder(n / 1.5 - 2, 1.6, segments=20))
)


with open("out.scad", 'w') as f:
    f.write(scad_render(sum(d)))
