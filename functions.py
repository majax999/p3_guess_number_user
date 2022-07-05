
from os import system
import platform

# Fonction permettant le "Nettoyage de l'ecran"
def ClearScreen():
	os = platform.system() # recuperation de l'OS courante
	cmd_clear = {"Linux":"clear", "Windows":"cls"} # Dict des valeurs OS/Cmd
	for get_os, get_cmd in cmd_clear.items():
		if get_os == os:
			system(get_cmd)
