import os
import getpass
import datetime
from pathlib import Path
from string import Template
from .ColorLoger import Loger


# Class Scripting
class FolderManager:
    def __init__(self, _path: str):
        self.fatherPath = _path
        self.path = "./"
        self.deep = 0

    def createfolder(self, _foldername: str) -> bool:
        """
        Function to create a new folder
        :param _foldername: folder name to create in the path defined
        :return: If the folder was created
        """
        tempPath = "{0}{1}".format(self.path, _foldername)
        try:
            os.mkdir("./{0}".format(_foldername))
            Loger.Ok("Carpeta creada: \"{0}\"".format(tempPath))
            return True
        except FileExistsError:
            Loger.Error("La carpeta \"{0}\" ya existe".format(tempPath))
            return False

    def enterDirectory(self, _path: str) -> bool:
        """
        Function to go into a path
        :param _path: Path to access
        :return: True if can enter the folder
        """
        try:
            os.chdir(_path)
            self.path += _path + "/"
            Loger.Ok("Accediendo: \"{0}\"".format(self.path))
            self.deep += 1
            return True
        except FileNotFoundError:
            Loger.Error("Error al ingresar: \"{0}\"".format("{0}{1}".format(self.path, _path)))
            return False

    def upFolder(self, num: int):
        """
        Function to up in folders proyect
        :param num: Number of idetation
        """
        iterator = 0
        while iterator < num:
            if iterator > self.deep:
                Loger.Warning("Limite de carpeta alcanzado ROOT PATH")
                break
            os.chdir("./..")

            varLen = len(self.path) - 2
            varTemp = ""
            while self.path[varLen] != '/':
                varLen -= 1
            for x in range(varLen + 1):
                varTemp += self.path[x]
            self.path = varTemp
            iterator += 1


class FileManager:
    @staticmethod
    def createFile(_name: str, _text: str) -> bool:
        FILE = Path(_name)
        if not FILE.exists():
            try:
                FILE.touch()
                Loger.Ok("Creado el archivo \"{0}\"".format(_name))
                try:
                    FILE.write_text(_text)
                    Loger.Ok("Escritura correcta en: \"{0}\"".format(_name))
                    return True
                except:
                    Loger.Error("Error al escribir en \"{0}\"".format(_name))
            except:
                Loger.Error("Error al escribir en \"{0}\"".format(_name))
        else:
            Loger.Error("El archivo \"{0}\" ya existe".format(_name))
        return False

    @staticmethod
    def fileExist(_file: str) -> bool:
        FILE = Path(_file)
        return FILE.exists()

    @staticmethod
    def deleteFile(_file: str):
        os.system("del /F {0}".format(_file))
        if FileManager.fileExist(_file):
            Loger.Warning("Archivo eliminado: \"{0}\"".format(_file))
            return True
        else:
            Loger.Warning("No se pudo eliminar: \"{0}\"".format(_file))
            return False


class FileTemplates:
    projectName = ""

    @staticmethod
    def main():
        return FileTemplates.MAIN_C.substitute(__FILENAME__="main.cpp", __USER__=getpass.getuser(),
                                               __DATE__=datetime.datetime.now().strftime("%Y/%m/%d"),
                                               __FILE__="main.h", __PROJECT__=FileTemplates.projectName)

    @staticmethod
    def mainLibrary():
        return FileTemplates.MAIN_LIBRARY.substitute(__FILE__=FileTemplates.projectName,
                                                     __FILEH__="MAIN_H")

    @staticmethod
    def library_H(_nameLibrary: str, _mode:bool ):
        _string = Template("")
        if _mode:
            _string = Template("""// Object declaration
class $__CLASS__
{
public:
    $__CLASS__();
private:

protected:

};

$__CLASS__::$__CLASS__()
{

}
""")
        return FileTemplates.LIBRARY_H.substitute(__CLASS__=_nameLibrary,
                                                  __MODE__ = _string.substitute(__CLASS__=_nameLibrary),
                                                  __FILE__="{0}_H".format(_nameLibrary.upper()))

    @staticmethod
    def library_C(_nameLibrary):
        return FileTemplates.LIBRARY_C.substitute(__CLASS__=_nameLibrary)

    MAIN_C = Template(
        """/**
    Project: $__PROJECT__
    File: $__FILENAME__
    Autor: $__USER__
    Version: 1.0
    Date: $__DATE__
*/
#include "$__FILE__"

int main(void)
{
    printf("Proyecto $__PROJECT__");
    return 0;
}
""")
    LIBRARY_H = Template(
        """/**
    Header class: $__CLASS__
    Documentation: 
*/
#ifndef $__FILE__
#define $__FILE__
// Libraries definitions

$__MODE__

#include "$__CLASS__.cpp"

#endif // !$__FILE__
""")

    LIBRARY_C = Template(
        """/**
    Object class: $__CLASS__
    Documentation: 
*/
#include "$__CLASS__.h"

// Functions of the class


""")

    MAIN_LIBRARY = Template(
        """/**
    Header project: $__FILE__
    Documentation: In this header you can include all libraries
                   or other class that you could need
*/
#ifndef $__FILEH__
#define $__FILEH__

#include <iostream>
#include <stdio.h>
///---
/// Dont delete this

#endif // !$__FILEH__
""")
