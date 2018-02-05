from setuptools import setup

setup(
    name='usb_manager',
    version='0.1',
    packages=['usb_manager'],
    install_requires=[
        'pyserial',
    ],
    url='https://github.com/M-Gregoire/usb_manager',
    keywords=['usb'],
    classifiers=[],
    author='Grégoire Martinache',
    author_email='gregoire@martinache.net',
    description='A Python library to interact with USB devices.'
)
