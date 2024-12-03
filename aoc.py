# ############################################################################## #
# This is my Advent of Code local setup tool.                                    #
# It creates a folder structure for the daily challenge and opens it in VS Code. #
# ############################################################################## #

import os
import random
import argparse
import subprocess

#########################
# Configs and variables #
#########################

LANGUAGES = ['python', 'node.js', 'c#', 'java']
LANG_EXTENSIONS = { 'python': 'py', 'node.js': 'js', 'c#': 'cs', 'java': 'java' }
ROOT_DIR = os.path.dirname(__file__)
VS_CODE_PATH = 'D:\\Microsoft VS Code\\bin\\code.cmd'
SRC_FILE_NAME = 'solve'

###################
# Language setups #
###################

def setup_python(day_dir):
    file = setup_language_file(day_dir, 'py')
    with open(file, 'w') as f:
        f.write('# Advent of Code\n\n')

def setup_nodejs(day_dir):
    file = setup_language_file(day_dir, 'js')
    return

def setup_csharp(day_dir):
    file = setup_language_file(day_dir, 'cs')
    return

def setup_java(day_dir):
    file = setup_language_file(day_dir, 'java')
    return

def setup_language_file(day_dir, lang_ext):
    return f'{day_dir}\\{SRC_FILE_NAME}.{lang_ext}'


###################
# Directory setup #
###################

def setup_dir(year, day, language):
    day_dir = os.path.join(ROOT_DIR, str(year), f'Day {day}')
    if os.path.exists(day_dir):
        print(f'Found folder for Year {year} Day {day}. Opening in VS Code...')
        return day_dir
    
    os.makedirs(day_dir)
    create_input_file(day_dir)
    
    # Setup language specific files
    if language.lower() == 'python':
        setup_python(day_dir)
    elif language.lower() == 'node.js':
        setup_nodejs(day_dir)
    elif language.lower() == 'c#':
        setup_csharp(day_dir)
    elif language.lower() == 'java':
        setup_java(day_dir)
    
    
    return day_dir

def create_input_file(day_dir):
    if not os.path.exists(day_dir):
        print('Error creating input file.')
        exit()
        
    input_file = f'{day_dir}\\input.txt'
    test_input_file = f'{day_dir}\\test.txt'
    
    open(input_file, 'w').close()
    open(test_input_file, 'w').close()


####################
# Input validation #
####################

def validate_day(day):
    if day < 1 or day > 25:
        raise ValueError('Day must be between 1 and 25')

def validate_language(language: str):
    if language.lower() not in LANGUAGES and language.lower() not in LANG_EXTENSIONS.values():
        raise ValueError(f'Invalid language: {language}')

########################
# Auto open in VS Code #
########################

def open_vscode(path):
    try:
        subprocess.run([VS_CODE_PATH, path], check=True)
    except subprocess.CalledProcessError:
        print('Error opening VS Code')
        exit()

####################
# Argument parsing #
####################

def parse_args():
    arg_parser = argparse.ArgumentParser(description='Advent of Code setup tool')
    arg_parser.add_argument('-y', '--year', type=int, required=True, help='Year of the challenge (i.e. 2024)')
    arg_parser.add_argument('-d', '--day', type=int, required=True, help='Day of the challenge (1-25)')
    arg_parser.add_argument('-l', '--language', type=str, choices=LANGUAGES, help='Language to use (random if not specified)')
    
    args = arg_parser.parse_args()
    validate_day(args.day)
    validate_language(args.language)

    return args.year, args.day, args.language

###########################
# Picking random language #
###########################

def pick_random_language():
    return random.choice(LANGUAGES)

########
# Main #
########

def main():
    year, day, language = parse_args()
    if language is None:
        language = pick_random_language()
    
    day_dir = setup_dir(year, day, language)
    if day_dir is None:
        print('Error setting up directory')
        exit()
    
    open_vscode(day_dir)
    print('Happy coding!')

###############
# Entry point #
###############

if __name__ == '__main__':
    main()