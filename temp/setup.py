#coding:utf-8
from distutils.core import setup
from Cython.Build import cythonize
setup(name='Helloworldapp',ext_modules=cythonize("hello.py"))
#pip install Cython
#cd C:\gitLab\brownser01\temp
#python setup.py build_ext --inplace