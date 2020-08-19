import subprocess
from subprocess import Popen,PIPE
import os,json,sys
from pathlib import Path



def config_file():

    d_list = ['binfile']
    config_file_path = os.path.join(Path.home(),'kconfig.json')

    jobj = None

    if os.path.exists(config_file_path):
        with open(config_file_path,'r',encoding='utf-8') as f:
            jobj = json.load(f)
            all_keys = jobj.keys()
            for element in d_list:
                if not element in all_keys:
                    if 'list' in element:
                        #if list is expected
                        jobj[element] = input(f'list for {element} :' ).split(',')
                    else:
                        jobj[element] = input(f'enter value for {element} :')

        #put the new data in config file
        with open(config_file_path,'w',encoding='utf-8') as fp:
            json.dump(jobj,fp)
        return jobj
    else:
        jobj = dict()
        all_keys = jobj.keys()
        for element in d_list:
            if not element in all_keys:
                if 'list' in element:
                    #if list is expected
                    jobj[element] = input(f'list for {element} :' ).split(',')
                else:
                    jobj[element] = input(f'enter value for {element} :')
        with open(config_file_path,'w',encoding='utf-8') as fp:
            json.dump(jobj,fp)
        return jobj


configdata = config_file()
binfile = configdata['binfile']

def verify_root():
    euid = os.geteuid()
    if euid != 0:
        raise PermissionError('roboserver needs to run as root')



def runrobo_sersver():
    full_path = os.path.join(binfile,'RoboServer')
    screen_command = f'screen -S roboserver -d -m {full_path}'
    run_command = f'{screen_command} -p 50000 -MC'
    Popen(run_command,shell=True,stdout=PIPE,stderr=PIPE)
    print('https://0.0.0.0:50080')

def stop_sersver():
    full_path = os.path.join(binfile,'ShutDownRoboServer')
    run_command = f'{full_path} localhost 50000 0'
    print(run_command)
    ps = Popen(run_command,shell=True,stdout=PIPE,stderr=PIPE)

    stdout,strerr = ps.communicate()
    
    if strerr:
        print(strerr)
    if stdout:
        print(stdout)    


def start_design_studio():
    full_path = os.path.join(binfile,'DesignStudio')
    screen_command = f'screen -S ds -d -m {full_path}'
    ps = Popen(screen_command,shell=True,stdout=PIPE,stderr=PIPE)

    stdout,strerr = ps.communicate()
    
    if strerr:
        print(strerr)
    if stdout:
        print(stdout)    


if __name__ == "__main__":
    #runrobo_sersver()
    start_design_studio()