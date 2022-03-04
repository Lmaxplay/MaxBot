import nextcord
import sys

def getnextcordversion():
    return str(nextcord.version_info.major) + "." + str(nextcord.version_info.minor) + "." + str(nextcord.version_info.micro) + " " + str(nextcord.version_info.releaselevel)

def getpythonversion():
    return str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro) #+ " " + str(sys.version_info.releaselevel)