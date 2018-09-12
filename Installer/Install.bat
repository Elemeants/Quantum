    @echo off

echo ----------------------------------------------------------------------------------
echo                            Installer QUANTUM Script
echo ----------------------------------------------------------------------------------
cd %~dp0
cd ..
echo Adding %cd% to PATH
call %cd%\Scripts\AddPath %cd%
echo ----------------------------------------------------------------------------------
echo Downloading C++ compiler
mkdir %cd%\Compilers\MinGW
cd %cd%\Compilers\MinGW
..\..\Scripts\Curl\bin\curl.exe http://pumath.dl.osdn.jp/mingw/69774/gcc-c++-7.3.0-1-mingw32-bin.tar.xz -o MinGW.tar.xz
echo ----------------------------------------------------------------------------------
echo Uncompressing C++ compiler
..\..\Scripts\7z\7za.exe x MinGW.tar.xz
del MinGW.tar.xz
..\..\Scripts\7z\7za.exe x MinGW.tar
del MinGW.tar
echo ----------------------------------------------------------------------------------
echo Adding C++ Compiler in %cd% to PATH
cd %~dp0
call %cd%\Scripts\AddPath %cd%\Compilers\MinGW\bin
echo ----------------------------------------------------------------------------------
cd %~dp0
cd Compilers
mkdir Python36_64
..\..\Scripts\Curl\bin\curl.exe http://pumath.dl.osdn.jp/mingw/69774/gcc-c++-7.3.0-1-mingw32-bin.tar.xz -o MinGW.tar.xz
https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe

echo                            Instalacion Finalizada

PAUSE