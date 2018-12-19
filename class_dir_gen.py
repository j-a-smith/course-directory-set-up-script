import os
import sys

subdirectories = ['homework', 'lecture_notes', 'projects', 'course_info', 'resources']

print('Purpose: Set up directories and subdirectories for school term')

if (len(sys.argv) < 2):
    parentDir = input('Enter parent directory: ')
else:
    parentDir = sys.argv[1]

parentIsReady = False
while (parentIsReady == False):
    parentExists = os.path.exists(parentDir);
    if (not parentExists):
        shouldCreateParent = input(parentDir + ' does not exist. Create now? (y/n) ')
        while (shouldCreateParent != 'y' and shouldCreateParent != 'n'):
            shouldCreateParent = input(parentDir + ' does not exist. Create now? (y/n) ')
        if shouldCreateParent == 'n':
            parentDir = input('Enter parent directory: ')
        else:
            parentIsReady = True;
    else:
        print('Class directories will be set up at: ', parentDir)
        shouldKeepParent = input('Continue with current directory? (y/n) ');
        while (shouldKeepParent != 'y' and shouldKeepParent != 'n'):
            shouldKeepParent = input('Press [enter] to continue or [backspace] to change directory');
        if shouldKeepParent == 'n':
            parentDir = input('Enter parent directory: ')
        else:
            parentIsReady = True


term = input('Enter school term (example: \'fall_2018\'): ');

classes = [];
classNumber = 1;
while (True):
    nextClass = input('Enter class name #' + str(classNumber) + ': ')
    classes.append(nextClass)
    classNumber = classNumber + 1
    shouldKeepAdding = input('Add another class? (y/n) ')
    while (shouldKeepAdding != 'y' and shouldKeepAdding != 'n'):
        shouldKeepAdding = input('Add another class? (y/n) ')
    if (shouldKeepAdding == 'n'):
        break;

if (not os.path.exists(parentDir)):
    print('Creating parent directory...')
    os.mkdir(parentDir)
print('Entering parent directory...')
os.chdir(parentDir)
print('Creating school term directory: ', os.path.join(os.getcwd(), term))
os.mkdir(term)
os.chdir(term)
for i in classes:
    print('Creating ', i, ' directory...')
    os.mkdir(i)
    os.chdir(i)
    print('Setting up ', i, '\'s subdirectories...')
    for i in subdirectories:
        os.mkdir(i)
    print('Finished setting up ', i, 'directory.')
    os.chdir('..')
os.chdir('..')
print('Done.')
exit
