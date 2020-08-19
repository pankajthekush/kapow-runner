from setuptools import setup,find_packages

setup(
    name='kapow_runner',
    version='1.0',
    packages=['kapow_runner'],
    entry_points ={'console_scripts': ['kstop = kapow_runner.kapow_runner:stop_sersver',
                                       'kstart = kapow_runner.kapow_runner:runrobo_sersver',
                                       'ds = kapow_runner.kapow_runner:start_design_studio',
                                       ]}
)
