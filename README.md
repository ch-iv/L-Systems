🌿 L-systems (Lindenmayer systems)
=============================

I created this project in 2018 to better understand parallel rewriting systems
and formal grammar. I used python to implement the L-system logic and image generation.
You can learn more about L-systems from this
[Wikipedia article on L-Systems](https://en.wikipedia.org/wiki/L-system).

The various scripts in this directory (`barnsley_fern .py, dragon_curve.py, sierpinski_triangle.py`),
show some examples of L-systems in action. When executed, they generate an image
of the result in an `./output` directory.

The current repo was made by me in 2022 with the purpose of refactoring and improving
my old 2018 code.

Running the scripts
-------------------
This projects uses [Pillow](https://python-pillow.org/) and [Turtle](https://pythonturtle.org/)
python libraries to generate images. *For pillow to work properly you must install
[Ghostscript](https://ghostscript.com/) and have it in your `PATH` system variable.

To run on windows:
```
python -m venv env

./env/Scripts/activate.bat

pip install -r requirements.txt

python dragon_curve.py
```
An image file should appear in an `/output` folder in your project directory.

