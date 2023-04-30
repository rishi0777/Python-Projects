
from cx_Freeze import *
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", #shortcut
     "DesktopFolder",#Directory
     "Go Fast",#Name
     "TARGETDIR",#component
     "[TARGETDIR]\Go_Fast.exe",#Target
     None,#Arguments
     None,#Description
     None,#Hotkey
     None,#Icon
     None,#IconIndex
     None,#ShowCmd
     "TARGETDIR",#Wkdir
     )
]
msi_data={"Shortcut": shortcut_table}

#change some default Msi options and specify the use of above shortcut table

bdist_msi_options={'data' : msi_data}
setup(
    version="1.0",
    description="GO_FAST Typing Speed Test Game",
    author="RISHI MISHRA",
    name="GO_FAST",
    options={'build.exe':  {"include_files": ['copyright.png','logo_rm.png','GO_FAST_setup.py']}, "bdist_msi": bdist_msi_options, },
        executables=[
            Executable(
                script="main.py",
                base=base,
                icon="Go_Fast_icon.ico",
            )
        ]
)
