import glob, os, datetime, shutil,time

from file_format import * #Config of all format:

########################First Step : Creating directory to organize########################
start = time.time()

current_time = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S') #Getting time to generate a name

current_dir = os.getcwd() #Current Directory

new_dir = current_dir+"\\Organized%s"%current_time

executing_dir = os.makedirs(new_dir) #Creating A New directory

##############################Getting files names###########################################
file_counter = 0
for existing_file in glob.glob(os.path.join(current_dir, '*.*')):
    file_counter += 1
    z = existing_file.split('\\')
    x = z[-1]                  #File Name
    y = x.split('.')[-1]        #File Format
    if y in text_for:
            try:
                text_dir = os.makedirs(new_dir+'\\Text')
                shutil.move(existing_file, new_dir+'\\Text')
            except FileExistsError as e:
                shutil.move(existing_file, new_dir+'\\Text')
    elif y in code_for:
            try:
                code_dir = os.makedirs(new_dir+'\\Codes')
                shutil.move(existing_file, new_dir+'\\Codes')
            except FileExistsError as e:
                shutil.move(existing_file, new_dir + '\\Codes')
    elif y in archive_for:
        try:
            archive_dir = os.makedirs(new_dir+'\\Archives')
            shutil.move(existing_file, new_dir+'\\Archives')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Archives')
    elif y in image_for:
        try:
            image_dir = os.makedirs(new_dir+'\\Images')
            shutil.move(existing_file, new_dir+'\\Images')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Images')
    elif y in video_for:
        try:
            video_dir = os.makedirs(new_dir+'\\Videos')
            shutil.move(existing_file, new_dir+'\\Videos')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Videos')
    elif y in web_for:
        try:
            web_dir = os.makedirs(new_dir+'\\Web')
            shutil.move(existing_file, new_dir + '\\Web')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Web')
    elif y in sheet_for:
        try:
            sheet_dir = os.makedirs(new_dir+'\\Sheets')
            shutil.move(existing_file, new_dir+'\\Sheets')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Sheets')
    elif y in slide_for:
        try:
            slide_dir = os.makedirs(new_dir+'\\Slides')
            shutil.move(existing_file, new_dir+'\\Slides')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Slides')
    elif y in exec_for:
        try:
            exec_dir = os.makedirs(new_dir+'\\Executables')
            shutil.move(existing_file,new_dir+'\\Executables')
        except FileExistsError as e:
            shutil.move(existing_file,new_dir+'\\Executables')
    elif y in audio_for:
        try:
            audio_dir = os.makedirs(new_dir+'\\Audios')
            shutil.move(existing_file, new_dir+'\\Audios')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Audios')
    elif y in font_for:
        try:
            font_dir = os.makedirs(new_dir+'\\Fonts')
            shutil.move(existing_file, new_dir+'\\Fonts')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Fonts')
    elif y in book_for:
        try:
            book_dir = os.makedirs(new_dir+'\\Books')
            shutil.move(existing_file, new_dir+'\\Books')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Books')
    else:
        try:
            other_dir = os.makedirs(new_dir+'\\Others')
            shutil.move(existing_file, new_dir+'\\Others')
        except FileExistsError as e:
            shutil.move(existing_file, new_dir + '\\Others')
print('Total files in this folder : %d' %file_counter)
print('process took',((time.time()-start),'seconds'))
