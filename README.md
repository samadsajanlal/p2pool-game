Requirements:
-------------------------
Generic:
* Gamecredits >=0.15.1!
* Python >=2.6
* Twisted >=10.0.0

Linux:
* sudo apt-get install python-rrdtool python-pygame python-scipy python-twisted python-twisted-web python-imaging

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local gamecreditsd. For standard
configurations, using P2Pool should be as simple as:

    cd litecoin_scrypt
    sudo python setup.py install
    cd ../
    python run_p2pool.py --net gamecredits

Then run your miner program, connecting to 127.0.0.1 on port 40004 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9346 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    1L5SEddaxi114ULkjBAwJsa5zjwuD5628h

Official wiki:
-------------------------
https://en.bitcoin.it/wiki/P2Pool
p2pool.wiki (russian)

Alternate web frontend:
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (Microsoft Visual C++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool:
-------------------------
Run P2Pool with the "--net gamecredits" option.
Run your miner program, connecting to 127.0.0.1 on port 40004.
Forward port 2963 to the host running P2Pool.

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](COPYING)


