"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""


from setuptools import setup

setup(
    name='flightanalysis',
    version='0.0.1',
    description='module for analysing flight log data',
    author='Thomas David',
    author_email='thomasdavid0@gmail.com',
    packages=['flightanalysis'],
    install_requires=['numpy', 'pandas', 'flightdata', 'geometry', 'scipy'],
)
