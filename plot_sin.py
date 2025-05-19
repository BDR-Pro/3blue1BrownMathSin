from manim import *
import numpy as np

class PlotSin(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1.5, 1.5],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE}
        )

        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        # ❌ DO NOT USE LaTeX (commented out)
        # graph_label = axes.get_graph_label(graph, label='\\sin(x)')

        # ✅ Use plain text instead
        graph_label = Text("sin(x)", font_size=24).next_to(graph, RIGHT)

        self.play(Create(axes), run_time=2)
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait()
