from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Main.py", base=base)]

packages = ["os", "shutil", "subprocess"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "JRS House Constructor",
    options = options,
    version = "1.0.0.0",
    description = 'JRS House Constructor',
    executables = executables
)