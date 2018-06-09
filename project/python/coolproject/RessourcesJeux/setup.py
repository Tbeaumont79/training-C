import cx_Freeze
executables = [cx_Freeze.Executable("flappython.py")]

cx_Freeze.setup(
    name = "ballon volant",
    options ={"build_exe": {"packages":["pygame"],"include_files":["Ballon01.png","BradBunR.ttf","NuageBas.png","NuageHaut.png"],"excludes":["tcl","ttk","tkinter","Tkinter"]}},
    executables = executables

)
