from setuptools import find_packages, setup

package_name = 'moverobotphase1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+package_name+'/launch',['launch/Phase1.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shidhin Varghese Philip',
    maintainer_email='ShidhinVarghesePhilip98@gmail.com',
    description='A Pub and Sub for Robot',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'pub1_node=moverobotphase1.Phase1Publisher:main',
        	'sub1_node=moverobotphase1.Phase1Subscriber:main',
        ],
    },
)
