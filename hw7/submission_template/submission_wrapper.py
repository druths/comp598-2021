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
    
    
    to_zip = [src_folder]
    final_zip_name = f"{STUDENTID}_submission_template.zip"
    with ZipFile(final_zip_name,'w') as zipp:
        for path in to_zip:
            for folderName, subfolders, filenames in os.walk(path):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipp.write(filePath)
        sample1 = os.path.join('.', 'concordia.json')
        sample2 = os.path.join('.', 'mcgill.json')
        annotated1 = os.path.join('.', 'annotated_concordia.tsv')
        annotated2 = os.path.join('.', 'annotated_mcgill.tsv')
        zipp.write(sample1)
        zipp.write(sample2)
        zipp.write(annotated1)
        zipp.write(annotated2)
    print(f"{final_zip_name} file created successfully - submit it through myCourses <3")


if __name__ == "__main__":
    main()