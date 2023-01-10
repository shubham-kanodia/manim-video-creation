# Learning Manim

## Installation of Manim on MacOS

* Run the following command to install system dependencies

    ```bash
    brew install py3cairo ffmpeg
    ```

* If using an M1 chip mac or similar, you need to install a few extra dependencies. Use the below command for that

    ```bash
    brew install pango scipy
    ```

* Once done, install the manim pip package

    ```bash
    pip3 install manim
    ```

* To run the manim animation use the following command

  ```bash
  python -m manim -pql scene.py CreateCircle
  ```
