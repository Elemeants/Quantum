#!/usr/bin/env python
import sys
import os
import subprocess
from pathlib import Path
from Modules.ColorLoger import Loger
from Modules.FileController import FolderManager, FileManager, FileTemplates

__VERSION__ = 1.2


def isInsideArray(__ARRAY__: list, __STR__: str) -> bool:
    for x in range(__ARRAY__.__len__()):
        if __TYPE__ == __ARRAY__[x]:
            return True
    return False


class Modules:
    __PATH__ = ""
    __BUILD_OPTIONS__ = ""

    @staticmethod
    def help():
        Loger.Help("""
 Quantum is a script for windows that help you to generate and manage c++ projects
 easier.
 Availables commands are:
    - clean <project> Deletes the data from a folder project
    - new <project>   Generates a new folder project
    - build           Builds a projects (you need to be inside the folder project)
    - run             Runs the .exe of the project 
    - add             Adds a component class or library into the actual project
    - help            Shows this message

 Script developed by: Polanco - Jdanypa@gmail.com
 Script version:      {0}""".format(__VERSION__))

    @staticmethod
    def clean(__PROJECTNAME__: str) -> bool:
        if Path(__PROJECTNAME__).exists():
            Loger.Warning("Limpiando proyecto: \"{0}\"".format(__PROJECTNAME__))
            try:
                output = subprocess.check_output("rd /S /Q {0}".format(__PROJECTNAME__), shell=True)
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
    def build(__BUILD_OPTIONS__: str):
        Wrapper = FolderManager(Modules.__PATH__)
        if Wrapper.enterDirectory("scr"):
            Loger.Info("Compilando Proyecto")
            try:
                subprocess.check_output(
                    "g++ main.cpp -o main.exe {0}".format(__BUILD_OPTIONS__), shell=True)
                Loger.Ok("Proyecto compilado")
                Loger.Info("Proyecto ejecutandose")
                print("")
                os.system("main.exe")
                print("\n")
                Loger.Ok("Ejecucion completada")
            except:
                Loger.Error("Error de compilacion")

    @staticmethod
    def run():
        Wrapper = FolderManager(Modules.__PATH__)
        if Wrapper.enterDirectory("scr"):
            if FileManager.fileExist("main.exe"):
                Loger.Info("Ejecutando proyecto")
                print("")
                os.system("main.exe")
                print("\n")
                Loger.Ok("Ejecucion completada")
            else:
                Loger.Error("No se puede ejecutar el proyecto")

    @staticmethod
    def genFileLib(__NAME__: str, __IS_CLASS: bool) -> bool:
        Wrapper = FolderManager(Modules.__PATH__)
        if Wrapper.enterDirectory("lib"):
            Wrapper.createfolder(__NAME__)
            if Wrapper.enterDirectory(__NAME__):
                FileManager.createFile("{0}.h".format(__NAME__),
                                       FileTemplates.library_H(__NAME__, _mode=__IS_CLASS))
                FileManager.createFile("{0}.cpp".format(__NAME__),
                                       FileTemplates.library_C(__NAME__))
                if FileManager.fileExist("{0}.h".format(__NAME__)) \
                        and FileManager.fileExist("{0}.cpp".format(__NAME__)):
                    Loger.Ok("Libreria creada")
                    os.system("{0}.h".format(__NAME__))
                    Wrapper.upFolder(2)
                    Modules.addLibtoH(__NAME__)
                    return True
        return False

    @staticmethod
    def addLibtoH(__NAME__):
        Wrapper = FolderManager(Modules.__PATH__)
        if Wrapper.enterDirectory("scr"):
            if FileManager.fileExist("main.h"):
                Manage = Path("main.h")
                Text = Manage.read_text().replace("///---",
                                                  """#include "..\lib\{0}\{0}.h"\n///---""".format(__NAME__))
                try:
                    FILE = open("main.h", "w")
                    FILE.write(Text)
                    Loger.Ok("Main.h actualizado")
                except:
                    Loger.Error("No se pudo actualizar main.h")

    @staticmethod
    def add(__TYPE__, __NAME__):
        availableTypes = ["library", "class"]
        if isInsideArray(availableTypes, __TYPE__):
            if __TYPE__ == availableTypes[0]:
                Loger.Info("Generando libreria")
                Modules.genFileLib(__NAME__, False)
            if __TYPE__ == availableTypes[1]:
                Loger.Info("Generando clase")
                Modules.genFileLib(__NAME__, True)

        else:
            Loger.Error("El componente no existe")

os.system("@echo off")
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
        try:
            __OPTIONS__ = sys.argv[2]
            Modules.build(__OPTIONS__)
        except:
            Modules.build("")

    if __COMMAND__ == "run":
        Modules.run()

    if __COMMAND__ == "help":
        Modules.help()
else:
    Modules.help()
