from setuptools import setup, find_packages
#from distutils.extension import Extension
#from Cython.Build import cythonize


#extensions = [
#]

install_requires = [
        'nmslib',
        'numpy'
        ]


setup(
    name='simplex-sampling',
    version='0.0.1',
    author='Yue Zhang',
    author_email='yjzhang@cs.washington.edu',
    url='https://github.com/yjzhang/simplex_sample',
    license='MIT',
    install_requires=install_requires,
#    ext_modules = cythonize(extensions),
    packages=find_packages("."),
    test_suite='nose.collector',
    tests_require=['nose'],
)
