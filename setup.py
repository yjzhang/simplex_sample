from setuptools import setup, find_packages
#from distutils.extension import Extension
#from Cython.Build import cythonize
import numpy


#extensions = [
#]


setup(
    name='simplex-sampling',
    version='0.0.1',
    author='Yue Zhang',
    author_email='yjzhang@cs.washington.edu',
    url='https://github.com/yjzhang/simplex_sample',
    license='MIT',
    include_dirs=[numpy.get_include()],
#    ext_modules = cythonize(extensions),
    packages=find_packages("."),
    test_suite='nose.collector',
    tests_require=['nose', 'flaky'],
)