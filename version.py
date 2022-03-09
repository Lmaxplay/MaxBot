import nextcord
import sys
import os
import platform

def getOSVersion():
    return f"{platform.system()} {platform.release()} (build {platform.version()}) {platform.architecture()[0]}"

def getNextcordVersion():
    return f"{nextcord.version_info.major}.{nextcord.version_info.minor}.{nextcord.version_info.micro} {nextcord.version_info.releaselevel}"

def getPythonVersion():
    return str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro) #+ " " + str(sys.version_info.releaselevel)