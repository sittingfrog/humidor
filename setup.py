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
        'inkbird',                     
    ],
    dependency_links = [
     "git+git://github.com/sittingfrog/inkbird",
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',    
        'Programming Language :: Python :: 3',
    ],
)
