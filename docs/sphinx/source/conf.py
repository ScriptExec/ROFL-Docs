import subprocess, shutil
shutil.rmtree('../../doxygen/build/html')
subprocess.call('make clean', shell=True)
subprocess.call('cd ../../doxygen ; doxygen', shell=True)
html_extra_path = ['../../doxygen/build/html']