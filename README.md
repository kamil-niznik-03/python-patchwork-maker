# Python Patchwork Maker

A Python graphics project that generates configurable geometric patchworks using user-selected sizes and colours.

This project was originally developed as part of my first-year Programming module at university. The submitted challenge-version implementation received a grade of **82%**.

## Overview

The application asks the user to choose a patchwork size and three different colours. It then generates a square patchwork made up of 100 × 100 pixel patches.

The patchwork design is based on the coursework requirements, where different patch layouts and geometric designs are generated using Python graphics commands.

## Features

- Generates square patchworks
- Supports patchwork sizes of 5×5, 7×7 and 9×9
- Allows the user to choose three different colours
- Validates user input for size and colour choices
- Draws geometric patch designs using Python graphics objects
- Uses functions to separate drawing logic
- Uses loops to generate repeated graphical patterns
- Includes an attempted challenge-mode selection/editing feature

## Technology Stack

- Python
- `graphics.py`
- Coordinate-based graphical drawing

## Project Structure

```text
python-patchwork-maker/
├── patchwork_maker.py
├── README.md
├── .gitignore
└── LICENSE
```

## Requirements

This project requires:

- Python 3
- The educational `graphics.py` module

The program imports the graphics module using:

```python
from graphics import *
```

If the `graphics` module is not installed or available, the program may show an error such as:

```text
ModuleNotFoundError: No module named 'graphics'
```

## Note on `graphics.py`

This project uses the educational `graphics.py` library commonly used for beginner Python graphics programming.

The `graphics.py` file is not included in this repository. To run the project locally, make sure the module is installed or available in the same directory as `patchwork_maker.py`.

## Running the Application

Clone the repository:

```bash
git clone https://github.com/kamil-niznik-03/python-patchwork-maker.git
cd python-patchwork-maker
```

Run the program:

```bash
python patchwork_maker.py
```

On some systems, you may need to use:

```bash
python3 patchwork_maker.py
```

## How to Use

1. Run `patchwork_maker.py`.
2. Enter a valid patchwork size when prompted.

Valid sizes are:

```text
5
7
9
```

3. Enter three different colours when prompted.

Valid colours are:

```text
red
green
blue
magenta
orange
yellow
cyan
```

4. The program opens a graphics window and draws the generated patchwork.

## Main Functionality

The application includes functions for:

- drawing lines
- drawing text
- drawing squares
- drawing the final patch design
- drawing the penultimate patch design
- validating the selected window size
- validating colour choices
- generating the patchwork grid
- opening the graphics window

## Academic Context

This project was originally developed as part of my first-year Programming module at university.

The submitted challenge-version implementation received a grade of **82%**.

The task was to create a Python program that generated patchworks using user input, validation, functions, loops and graphical drawing.

This repository contains my submitted challenge-version implementation, with minor documentation and repository-structure improvements made afterward for portfolio presentation.

## Current Limitations

- The project depends on the external `graphics.py` module.
- The application is designed as a coursework prototype.
- The challenge-mode editing functionality was attempted but is not fully completed.
- There is no automated test suite.
- The program uses a simple shell-based input system before opening the graphics window.
- The visual design is based on fixed 100 × 100 pixel patch sizes.

## Potential Improvements

Future improvements could include:

- Completing the challenge-mode editing functionality
- Allowing selected patches to be recoloured after drawing
- Allowing selected patches to switch between patch designs
- Adding a clearer graphical user interface for choosing colours and sizes
- Refactoring the code into separate files
- Adding automated tests for validation functions
- Supporting additional patch sizes
- Supporting custom patch designs
- Replacing `graphics.py` with Tkinter or Pygame for easier installation

## What I Learned

This project helped me practise core Python programming concepts, including functions, loops, user input, validation and graphical drawing.

It also introduced me to coordinate-based design, where graphical elements are positioned using x and y values inside a drawing window.

## Author

**Kamil Niznik**

Software Engineering student interested in web development, backend development and software engineering.

## Licence

This project is licensed under the MIT Licence.
