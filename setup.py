import setuptools

setuptools.setup(
    name="uhome",
    version="0.1.4",
    author="Almir Delkic",
    description="Wrapper for communication with Uponor Smatrix Wave PLUS Smart Home Gateway R-167 aka U@home.",
    url="https://github.com/almirdelkic/uhome",
    packages=setuptools.find_packages(),
    license='GNU GPLv3',
    install_requires=[
        'requests',
    ],
)
