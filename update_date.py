import zipfile


zip_file_url = '/home/emirali/Documents/\
EmiraliCaferzade_Belgeler/Code/Projects/\
update_date_in_cv/emirali_CV_libreOffice_template.zip'

with zipfile.ZipFile(zip_file_url) as my_zip:
    with my_zip.open('emirali_CV_libreOffice_template.odt') as my_file:
        print(my_file.read())