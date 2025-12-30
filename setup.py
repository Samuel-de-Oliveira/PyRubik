from setuptools import setup, find_packages
import PyRubik

# Get the README.md file and create the doc
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description: str = fh.read()

# Get the project requirements
with open('requirements.txt', 'r', encoding='utf-8') as fh:
    project_requirements: str = fh.read()

# Setup
setup(
    name='PyRubik',
    version=PyRubik.__version__,
    author='Samuel de Oliveira',
    author_email='samwolfg12@gmail.com',
    packages=find_packages(),
    project_urls={
        'Source code': 'https://github.com/Samuel-de-Oliveira/PyCubing/',
        'Documentation': 'https://pyrubik.readthedocs.io/en/latest/',
    },
    license='MIT',
    description='A Python module to make speedcubing projects a piece of cake.',
    keywords="cubing rubik rubik's cube solver scramble cube pyrubik",
    long_description=long_description,
    python_requires='>=3.10',
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
    # Package commands
    entry_points={'console_scripts': []},  # comming soon...
)
