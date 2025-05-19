# Eaxmple using 3Blue1Brown Animation

## 📈 Plotting `sin(x)` with Manim (No LaTeX Required)

This project demonstrates how to animate the mathematical function `f(x) = sin(x)` using the [Manim Community Edition](https://docs.manim.community). The animation includes:

- Coordinate axes
- A live-drawn sine wave
- A simple `sin(x)` label rendered without LaTeX

## 🧪 What You’ll See

<video src="media/videos/plot_sin/480p15/PlotSin.mp4" controls width="500"></video>

The animation smoothly draws the sine function on a graph using Manim's `Axes` and `plot()` methods.

---

## 🛠 How to Run

1. Clone this repo or copy the code into a `plot_sin.py` file.
2. Open a terminal and run:

```bash
python -m manim -pql plot_sin.py PlotSin
````

This will generate and preview a video in the `media/videos` folder.

---

## 📦 Dependencies

Make sure you have the following installed:

```bash
pip install manim numpy
```

---

## 💡 Code Overview

```python
axes = Axes(...)
graph = axes.plot(lambda x: np.sin(x))
label = Text("sin(x)").next_to(graph, RIGHT)
self.play(Create(axes), Create(graph), Write(label))
```

---
> [!NOTE]
> 💡 This animation uses `Text()` instead of `Tex()`, so **you don’t need a full LaTeX setup**.
> It works out of the box with **TinyTeX** or even with **no LaTeX installed at all**.
>
> 🔢 If you want to display math using LaTeX (e.g. `\\sin(x)`), you’ll need to install [TinyTeX](https://yihui.org/tinytex/) or TeX Live, and make sure both `pdflatex` and `dvisvgm` are available in your system `PATH`.

---

## 🎬 Output

Your video will be saved to:

```txt
./media/videos/plot_sin/480p15/PlotSin.mp4
```

---

## 🔄 Next Steps

Try modifying the code to:

- Plot other functions (`cos(x)`, `x²`, `e^x`)
- Animate function transformations
- Add axis ticks and gridlines
- Use `Tex()` for math-mode labels if LaTeX is available

---
\
*Happy animating! 🎥✨*
