from setuptools import setup, Extension

module = Extension ('csp_cython_solver', sources=['csp_cython_solver.pyx'])

setup(
    name='csp_cython_solver',
    version='1.0',
    author='jetbrains',
    ext_modules=[module]
)