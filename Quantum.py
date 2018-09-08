#!/usr/bin/env python
import sys
import os
from pathlib import Path
from Modules.ColorLoger import Loger
from Modules.FileController import FolderManager, FileManager, FileTemplates

__VERSION__ = 1.1

class Modules:
    __PATH__ = ""

    @staticmethod
    def help():
        Loger.Help("""
 Quantum is a script for windows that help you to generate and manage c++ projects
 easier.
 Availables commands are:
    - clean <project> Deletes the data from a folder project
    - new <project>   Generates a new folder project
    - build           Builds a projects (you need to be inside the folder project)
    - add             Adds a component class or library into the actual project
    - help            Shows this message

 Script developed by: Polanco - Jdanypa@gmail.com
 Script version:      {0}""".format(__VERSION__))

    @staticmethod
    def clean(__PROJECTNAME__: str) -> bool:
        if Path(__PROJECTNAME__).exists():
            Loger.Warning("Limpiando proyecto: \"{0}\"".format(__PROJECTNAME__))
            try:
                _index = 0
                while FileManager.fileExist(__PROJECTNAME__):
                    os.system("rd /S /Q {0}".format(__PROJECTNAME__))
                    if(_index >= 3):
                        Loger.Error("No se pudo eliminar el proyecto")
                        return False
                    _index += 1
                Loger.Ok("Limpieza terminada")
            except:
                Loger.Error("No se pudo eliminar el proyecto")
            return True
        # Si no se borro return false
        Loger.Error("No existe el proyecto: \"{0}\"".format(__PROJECTNAME__))
        return False

    @staticmethod
    def new(__PROJECTNAME__: str) -> bool:
        Wrapper = FolderManager(Modules.__PATH__)
        FileTemplates.projectName = __PROJECTNAME__
        if Wrapper.createfolder(__PROJECTNAME__) and Wrapper.enterDirectory(__PROJECTNAME__):
            Wrapper.createfolder("lib")
            if Wrapper.createfolder("scr"):
                if Wrapper.enterDirectory("scr"):
                    FileManager.createFile("main.cpp", FileTemplates.main())
                    FileManager.createFile("main.h", FileTemplates.mainLibrary())
                    if FileManager.fileExist("main.cpp") and FileManager.fileExist("main.h"):
                        os.system("start main.cpp")
                    return True
            Modules.clean(__PROJECT__)
        else:
            Loger.Error("No se puede crear el proyecto \"{0}\"".format(sys.argv[2]))
        return False

    @staticmethod
    def build():
        Wrapper = FolderManager(Modules.__PATH__)
        if Wrapper.enterDirectory("scr"):
            Loger.Info("Compilando Proyecto")
            os.system("g++ main.cpp -o main.exe")
            if FileManager.fileExist("main.exe"):
                 Loger.Info("Proyecto ejecutandose")
                 print("")
                 os.system("main.exe")
                 print("\n")
                 Loger.Ok("Ejecucion completada")
            else:
                Loger.Error("Error de compilacion main.cpp")
            return True
        return False

    @staticmethod
    def add(__TYPE__, __NAME__):
        Loger.Ok("Iniciando ADD Module")


os.system("@echo off")
# print(Loger.CBLUE2 + sys.argv.__str__() + Loger.CEND)
if sys.argv.__len__() > 1:
    Modules.__PATH__ = sys.argv[0]
    __COMMAND__ = sys.argv[1]

    if __COMMAND__ == "add":
        __HELP__ = """
 Para ejecutar este comando es necesario que estes dentro de la carpeta del proyecto
 Utilizacion:
    Quantum add <tipo> <nombre>
    tipo    - Determina que componente se añadira al proyecto actual
            - Componentes disponibles:
            -       library : Para generacion de un componente tipo libraria con sus
            -                 archivos tipo .h y .cpp correspondientes
            -       class   : Genera un componente heredado de 'library' pero el cual
            -                 incluye dentro de ella un constructor de clase
    nombre  - El nombre que llevara el componente"""
        if not sys.argv.__len__() < 3:
            __TYPE__ = sys.argv[2]
            __NAME__ = sys.argv[3]
            if __TYPE__ == "help":
                Loger.Help(__HELP__)
            else:
                Modules.add(__TYPE__=__TYPE__, __NAME__=__NAME__)
        else:
            Loger.Help(__HELP__)

    if __COMMAND__ == "new":
        try:
            __PROJECT__ = sys.argv[2]
            Modules.new(__PROJECT__)
        except IndexError:
            Loger.Error("Comando \"new\" necesita el nombre del proyecto")

    if __COMMAND__ == "clean":
        try:
            __PROJECT__ = sys.argv[2]
            Modules.clean(__PROJECT__)
        except IndexError:
            Loger.Error("Comando \"clean\" necesita el nombre del proyecto")

    if __COMMAND__ == "build":
        if not Modules.build():
            Loger.Error("No se pudo compilar el proyecto")

    if __COMMAND__ == "help":
        Modules.help()
else:
    Modules.help()