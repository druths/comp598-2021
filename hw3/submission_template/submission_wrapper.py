import argparse
import os, sys
from zipfile import ZipFile

parser = argparse.ArgumentParser()
parser.add_argument('-id', help='Student ID (only numbers)', required=True)
args = parser.parse_args()
STUDENTID = '{}'.format(args.id) 

def main():
    print("Preparing files to zip")
    src_folder = os.path.join('.', 'src')
    scripts_folder = os.path.join('.', 'scripts')
    
    to_zip = [src_folder, scripts_folder]
    final_zip_name = f"{STUDENTID}_submission_template.zip"
    with ZipFile(final_zip_name,'w') as zipp:
        for path in to_zip:
            for folderName, subfolders, filenames in os.walk(path):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipp.write(filePath)
        output_file = os.path.join('.', 'output.json')
        zipp.write(output_file)
    print(f"{final_zip_name} file created successfully - submit it through myCourses <3")


if __name__ == "__main__":
    main()