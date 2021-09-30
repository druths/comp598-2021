import argparse
import os, sys
from zipfile import ZipFile

parser = argparse.ArgumentParser()
parser.add_argument('-id', help='Student ID (only numbers)', required=True)
args = parser.parse_args()
STUDENTID = '{}'.format(args.id) 

def main():
    print("Preparing files to zip - HW4")
    
    final_zip_name = f"{STUDENTID}_submission_template.zip"
    with ZipFile(final_zip_name,'w') as zipp:
        ip_addr_file = os.path.join('.', 'ip_address.txt')
        zipp.write(ip_addr_file)
        jupyter_log_file = os.path.join('.', 'jupyter.log')
        zipp.write(jupyter_log_file)
    print(f"{final_zip_name} file created successfully - submit it through myCourses <3")


if __name__ == "__main__":
    main()