import os
import csv

##commit pred files to git first

#get relevant file names
in_dir="preds"
with os.scandir(in_dir) as dir:
	file_list = [file.name for file in dir if file.is_file() == True]

#write url file
with open('pred_urls_s3.csv', mode='w', newline='') as url_file:
    csv_writer = csv.writer(url_file, delimiter=',')

    #write header
    csv_writer.writerow(['pred_file', 'url'])

    for file in file_list:
    	csv_writer.writerow([file, "s3://accs-data.rand.cloud/services/roeda/{0}".format(file)])
