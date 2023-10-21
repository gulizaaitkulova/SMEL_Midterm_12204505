from setuptools import setup

package_name = 'dynamic_fleet_management'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gulizaaitkulova',
    maintainer_email='gulizaaitkulova@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = dynamic_fleet_management.fleet_management_server_cli:main',
            'client = dynamic_fleet_management.fleet_management_client_cli:main',
        ],
    },
)
