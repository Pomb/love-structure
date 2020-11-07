#!/usr/local/bin/python3

import os
import sys
import subprocess

def init_libraries(directory):
    '''My Common libraries'''
    
    libs = ["https://github.com/EmmanuelOga/easing.git", "https://github.com/airstruck/knife.git", 
    "https://github.com/vrld/moonshine.git", "https://github.com/Pomb/doodlehouse-love.git"]
    for repo in libs:
        args = ["clone", repo]
        subprocess.check_call(['git'] + list(args), cwd=directory+"/libraries")

def init_main_file(directory):
    '''Create the empty main.lua file common to love2d projects'''

    with open(directory+"/main.lua", "w") as main_file:
        main_file.write(f'''
function love.load()
end

function love.draw()
end

function love.update(dt)
end

function love.keypressed(key, scancode, isrepeat)
end''')

def init_conf_file(directory):
    '''Create a simple conf file for a love2d project'''

    with open(directory+"/conf.lua", "w") as conf_file:
        conf_file.write(f'''
function love.conf(t)
    t.version = "11.3"                  -- The LÖVE version this game was made for (string)
    t.window.width = 800                -- The window width (number)
    t.window.height = 600               -- The window height (number)
    t.window.title = "{directory}"      -- The window title (string)
end
''')

def init_git(directory):
    '''Pulls the libraries and creates a git project'''
    init_libraries(directory)
    # init repo
    subprocess.check_call(['git', 'init'], cwd=directory)
    # simple gitignore file
    filename = directory+"/"+".gitignore"
    with open(filename, "w") as ignore_file:
        ignore_file.write(f'''
    *.tmp
    [Tt]emp
    [Bb]uilds
    [Aa]uthor

    .DS_Store
    Thumbs.db
''')


def create_project(directory):
    try:
        print(f'creating project {directory}...')
        # root
        os.makedirs(directory)
        # sub folders
        print('creating sub folders...')
        folders = ["src", "libraries", "docs", "builds"]
        for f in folders:
            os.makedirs(directory+"/"+f)
        
        # readme
        print('creating initial files...')
        with open(directory+"/README.md", "w") as readme_file:
            readme_file.write(f'# {directory.upper()}\nA game made using the https://love2d.org\n\n## ABOUT\n...')

        # design / todo
        with open(directory+"/docs/TODO.md", "w") as readme_file:
            readme_file.write(f'# TODO\n\n## MVP Features\n\n[ ] - ...\n\n## Scope Dragon Features\n\n[ ] - ...')

        # love files
        init_main_file(directory)
        init_conf_file(directory)

        # git
        print('initializing git and libraries...')
        init_git(directory)

    except FileExistsError :
        print(f"\b[FAILED] - project [{directory}] already exists")
        return

    # complete
    print(f'\n[SUCCESS] - love2d project [{directory}] created ---')


if __name__ == "__main__":
    try:
        name = sys.argv[1]
        create_project(name)
    except:
        print("please try again with a project name argument")
        