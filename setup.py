from setuptools import setup
import PyCubing

# Get the README.md file and create the doc
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description: str = fh.read()

# Get the project requirements
with open('requirements.txt', 'r', encoding='utf-8') as fh:
    project_requirements: str = fh.read() 

# Setup
setup(
    name='PyCubing',
    version=PyCubing.__version__,
    author='Samuel de Oliveira',
    author_email='samwolfg12@gmail.com',
    packages=['PyCubing'],
    url='https://github.com/Samuel-de-Oliveira/PyCubing',
    license='MIT',
    description='A Python module to make speedcubing projects a piece of cake.',
    keywords = 'cubing rubik rubik\'s cube solver scramble cube',
    long_description=long_description,
    python_requires='>=3.10',
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
    project_urls={
        "Source": "https://github.com/Samuel-de-Oliveira/PyCubing",
    },
    setup_requires=["wheel==0.45.1"],
)
