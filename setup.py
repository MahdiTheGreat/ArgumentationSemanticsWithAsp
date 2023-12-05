# from setuptools import setup, Extension
#
# module = Extension ('csp_cython_solver', sources=['csp_cython_solver.pyx'])
#
# setup(
#     name='csp_cython_solver',
#     version='1.0',
#     author='jetbrains',
#     ext_modules=[module]
# )
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("csp_cython_solver.pyx")
)