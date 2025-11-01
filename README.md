# Manim Tutorial

> It is recommended to start from ManimCE (renders to mp4), and then move on to ManimGL for interactive rendering and more advanced features.

## Quick Start

### Step1: Install uv

[`uv`](https://github.com/astral-sh/uv) is an extremely fast Python package and project manager, written in Rust.

```
$ uv venv
$ uv sync
```

### Step 2: Install Manim and Latex

Windows:

- Miktex: https://miktex.org/download

Linux:

```
$ sudo apt install texlive-full
```

### Step 3: Check installation

```
# Windows
$ .venv\Scripts\activate

# Linux
$ source .venv/bin/activate

$ uv run manim checkhealth
```


## Beginner

> [!IMPORTANT]
> Don't forget to activate the virtual environment before running examples.

```
$ manim -pql tutorial_01.py TextDemo
```

![](beginner/tutorial_01.gif)

```
$ manim -pql tutorial_02.py SquareAndCircle 
```

![](beginner/tutorial_02.gif)


```
$ manim -pql tutorial_03.py SquareToCircle
```

![](beginner/tutorial_03.gif)

```
$ manim -pql tutorial_04.py AnimatedSquareToCircle --format gif
```

![](beginner/tutorial_04.gif)

## Intermediate
