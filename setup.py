from cx_Freeze import setup, Executable
files = {"include_files": ["wkhtmltopdf","vcredist_x86.exe"],
         "packages": ["sqlalchemy.ext.baked","sqlalchemy.sql.default_comparator"],
         'include_msvcr': True,
         'replace_paths': [('*', '')],
         'zip_include_packages': ['*'],
         'zip_exclude_packages': [],
        
        }
setup(
    name = "ZHU Skoczylas Oferta" ,
    version = "0.1" ,
    description = "" ,
    options={'build_exe': files},
    executables = [Executable("main.py",base="Win32GUI",icon="favicon.ico")] ,
    )#