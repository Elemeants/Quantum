# Quantum

Quantum is a Python script for windows to generate, build and manage C++ Projects

### Prerequisites

What things you need to install the software and how to install them

```
* [Python](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe) - To execute the file
* [C++ Compiler](http://pumath.dl.osdn.jp/mingw/69774/gcc-c++-7.3.0-1-mingw32-bin.tar.xz) - MinGW toolchain
```

### Installing

For install the script you can run the install.bat inside the Installer folder

```
run install.bat as admin
```

or manual instalation:
```
Save the folder and add to your system PATH the folder, after you need to install python and also install a g++ compiler and add to the PATH the bin folder
```

## Deployment

Generate a new project
```
Quantum new <project name>
```

Deletes the folder of the project
```
Quantum clean <project folder>
```

Compiling a c++ project
```
cd <Project folder>
Quantum build
```

Run the exe of the project
```
cd <Project folder>
Quantum run
```

Add a library or a class to the project
```
cd <Project folder>
Quantum add class <class name>

or 

Quantum add library <library name>
```

## Built With

* [Python](https://www.python.org/) - Language used in the script 

## Authors

* **Daniel Polanco** - *Author* - [Elemeants](https://github.com/Elemeants)

## License

This project is licensed under the GLP-3.0 License - see the [LICENSE.md](LICENSE.md) file for details