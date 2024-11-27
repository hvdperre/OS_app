#imports 
import os 
import art


#function check (main function)
def checkchoice(choice: int) -> None:
    """check what choice you make

    Parameters
    ----------
        choice : choice you make (int)

    Returns
    -------
        NONE

    """
    #like switch in Java and C++
    match choice:
        case (1):
            make_folder(get_name())
        case (2):
            create_file(get_name())
        case (3):
            delete_folder(get_name())
        case (4):
            delete_file(get_name())
        case (5):
            write_file(get_name(), get_text())
        case (6):
            read_file(get_name())

        case (7):
            append_file(get_name, get_text())
        case (8):
            change_dir(get_name())
        case (9):
            list_dir()
        case (0):
            exit()
        case _:
            choice_help()

#function to get the choice of the user
def get_choice() -> str:
    """Get the choice you make
    Parameters
    ----------
        NONE
    Returns
    -------
        result : your choice (str)
    """
    try: #try and if there is a value error he just print a message
        return int(input("Enter your choice: "))
    except ValueError:
        print('format of the number isn\'t correct')

#function to get the name of a file or a directory
def get_name() -> str:
    """Get the name you want to assign on the file/directory

    Parameters
    ----------
        NONE

    Returns
    -------
        result : the name of the file/directory (str)

    """
    return input("Enter the name : ")

#function to get the text you want to put in a file 
def get_text() -> str:
    """Get the text you want to put in a file
    
    Parameters 
    ---------
        NONE

    Returns
    -------
        result : the text you enter (str)
    """
    return input('Enter the text : ')

#function to make a folder 
def make_folder(folder_name : str) -> None:
    """Make a folder

    Parameters
    ---------
        folder_name : name of the directory (str)

    Returns
    -------
        NONE
    """
    print(f'Making folder in {os.getcwd()}')
    os.mkdir(folder_name)#create a folder if the folder doesn't exist 

#function to create a file
def create_file(file_name : str) -> None:
    """Create a file

    Parameters
    ---------
        file_name : Name of the file (str)

    Returns
    -------
        NONE
    """
    print(f'Creating file in {os.getcwd()}')
    file = open(file_name, 'w')#create a file if the file doesn't exist in the directory
    file.close()#close the file

#function to delete a folder
def delete_folder(folder_name : str) -> None:
    """Delete the folder

    Parameters
    ---------
        folder_name : name of the folder (str)

    Returns
    ------
        NONE
    """
    if check_existing(folder_name):#check if the folder exist
        os.rmdir(folder_name)
        print(f'You remove the folder {folder_name} in {os.getcwd}')
    else:#else he restard the function
        delete_folder(get_name)

#function to delete a file
def delete_file(file_name : str) -> None:
    """Delete the file

    Parameters
    ----------
        file_name : name of the file (str)

    Returns
    -------
        NONE

    """
    if check_existing(file_name): #check if a file exist 
        os.remove(file_name)
        print(f'You remove the file {file_name} in {os.getcwd}')
    else:#else he restard the function
        delete_file(get_name)
    
#function to write in a file
def write_file(file_name : str, text : str) -> None:
    """Write in a file

    Parameters
    ---------
        file_name : name of the file (str)
        text : text to write (str)

    Returns
    ------
        NONE
    """
    file = open(file_name, 'w') #open the file with the writing mode 
    file.write(text + '\n', file_name) #write the text with a \n in the file
    print(f'You write {text} in {file_name}')
    file.close()#close the file

#function to read a file 
def read_file(file_name : str) -> str:
    """Read a file

    Parameters
    ---------
        file_name : name of the file (str)

    Returns
    -------
        result : lines of the file (str)
    """
    if check_existing(file_name):#check if the file exist 
        file = open(file_name, 'r') #open it in reading mode
        lines = file.read()#read the content of the file
        file.close()#close the file and return the content
        print(f'The content of the file : {file_name} is {lines}')
    else:
        read_file(get_name)#else restard the function

#function to add in a file
def append_file(file_name : str, text : str) -> None:
    """Add text on the file

    Parameters
    ---------
        file_name : name of the file (str)
        text : text you want to add (str)

    Returns 
    -------
        NONE
    """
    if check_existing(file_name): #check if a file exist
        file = open(file_name, 'a')#open the file in append mode
        file.write(text)#write the text in the file
        print(f'You add {text} in {file_name}')
        file.close()#close the file
    else:
        append_file(get_name, text)#restard if the file doesn't exist

#function to change the directory
def change_dir(place : str) -> None:
    """Change the current directory

    Parameters
    ----------
        place : place you want to go (str)

    Returns
    -------
        NONE
    """
    try:#try and if the place you want to go doesn't exist the function restard
        os.chdir(place)
        print(f'You new current directory is {os.getcwd()}')
    except:
        print(list_dir())#show the repository bellow you
        change_dir(get_name)

#function to list all in the current directory
def list_dir() -> None:
    """List all in the current directory

    Parameters 
    ----------
        NONE

    Returns
    -------
        NONE
    """
    print(os.listdir())#show the repository in the current directory

#function to show all 
def choice_help() -> None:
    """Show all commands

    Parameters 
    ---------
        NONE

    Returns
    -------
        NONE
    """
    Art=art.text2art("Folder Maker")# Return ASCII text with block font
    print(f'\033[92m{Art}\033[0m') #show the message who has been in ASCII
    print(f'list of choice\n'
          f'make a folder : 1\n'
          f'make a file : 2\n'
          f'delete a folder : 3\n'
          f'delete a file : 4\n'
          f'write in a file : 5\n'
          f'read a file : 6\n'
          f'add in a file : 7\n'
          f'change directory : 8\n'
          f'list of the directory : 9\n'
          f'exit : 0\n'
          f'help : nothing\n')#show all function
    
#check if a file or a folder exist
def check_existing(name : str) -> bool:
    """Check if a folder or if a file exist

    Parameters
    ---------
        name : name of the file or name of the folder you want to check (str)

    Returns
    -------
        result : True or False (bool)
    """
    return os.path.exists(name)#return True or False