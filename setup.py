from setuptools import setup

setup(
    name='humidor',
    version='0.1.0',    
    description='Humidor monitoring application',
    url='https://github.com/sittingfrog/humidor',
    author='sittingfrog',
    license='MIT',
    packages=['humidor'],
    install_requires=[
        'pyyaml',
        'inkbird @ https://github.com/sittingfrog/inkbird/archive/refs/tags/0.1.0.tar.gz',
        'pandas',
        'matplotlib',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',    
        'Programming Language :: Python :: 3',
    ],
)
