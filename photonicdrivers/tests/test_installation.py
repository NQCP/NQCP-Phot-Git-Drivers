"""
Simple test file to verify the installation.

This test file is included so that the tests can run immediately after the
template creation of the repo
"""

from photonicdrivers.hello_world import greeter, hello_world, myadd


def test_greeter():
    assert greeter("name") == f"Hello, name!"
	
def test_myadd():
	x = 2
	y = 2
	assert myadd(x,y) == x+y 

