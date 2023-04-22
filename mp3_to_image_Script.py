import eyed3 as ey
from subprocess import call
from time import sleep
call('color a', shell=True)
print('*' * 3,' '* 4,'*' * 3,' '*6 ,'*' * 3,' '* 4,'*' * 3)
print('*' * 4,' '* 2,'*' * 4 ,' '*6,'*' * 4,' '* 2,'*' * 4)
print('*' * 2,' '* 1,'*' * 2,' '* 1, '*' * 2 ,' '*6 ,'*' * 2,' '* 1,'*' * 2,' '* 1, '*' * 2)
print('*' * 2,' '* 6, '*' * 2 ,' '*6 ,'*' * 2,' '* 6, '*' * 2)
print('*' * 2,' '* 6, '*' * 2 ,' '*2,'*' * 3 ,'*' * 2,' '* 6, '*' * 2 )
print('*' * 2,' '* 6, '*' * 2 ,' '*2,'*' * 3,'*' * 2,' '* 6, '*' * 2 ,)
print('''
Welcome to M.Metros Mp3 Editor 
It adds Information to Mp3 files eg image,artist name etc.
please input the path to your files when asked :-)
''')
name = input('Name of the Mp3 file with extension :')
audio_file = ey.load(name)


def add_image():
    '''
    This Is The Most Important Function For Me.
    It Basicaly Adds Artwork To images 
    '''    
    image = input('Name of the image file with extension: ')
    var = int(input('jpeg (1) or png (2): '))
    if var == 1:
        Mim_typ1 = 'image/jpeg'
        audio_file.tag.images.set(3,open(image,'rb').read(), Mim_typ1)
    elif var == 2:
        Mim_typ2 = 'image/png'
        audio_file.tag.images.set(3,open(image,'rb').read(), Mim_typ2)
    else:
        print('Typo Error: input 1 or 2 to specify the Mime type of the image')
        print('canceling .......')


def add_title():
    '''
    This Function Adds TiTle To The MP3 File  
    '''
    title = str(input('The Title of The Music: '))
    audio_file.tag.title = title
    print(f'MP3 Title - {audio_file.tag.title}')


def add_album():
    '''
    This Function Adds the Album Name To The File 
    '''
    album = input('The Album Name: ')
    audio_file.tag.album = album
    print(f'Mp3 Album- {audio_file.tag.album}')


def add_artist():
    '''
    This Function Adds The Name Of The Artist To The Mp3 File
    '''
    artist = input('The Name Of The Artist: ')
    audio_file.tag.artist = artist
    print(f'Mp3 Artist- {audio_file.tag.artist}')



command = ''
stats = False
while True:
    command = input('> ').lower()
    if command == 'title':
        add_title()
    elif command == 'image':
        add_image()
    elif command == 'artist':
        add_artist()
    elif command == 'album':
       add_album()
    elif command == 'help':
        print('''
Commands : Use Of The Command .
image  : This Command Adds Image To Your Mp3 File .
title  : This Command Adds A Title To Your Mp3 File.
artist : This Command Adds The Name Of The artist To The Mp3 File .
album  : This Command Adds The Name Of The Album To The Mp3 File .
Quit   : This Command Ends The Program.
        ''')
    elif command == 'quit':
        print('Closing Script 1 2 3.......')
        audio_file.tag.save()
        break
    else:
        print('command Error')
        break 
