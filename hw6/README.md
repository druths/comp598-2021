# Welcome to HW6! 

**Important instructions** 
Please read these instructions before submitting your assignment. 
If you do not follow the template specified here, **we will not able to grade your assignment**! 
To avoid pain and discomfort, follow the steps below carefully:


In this directory, you'll find another folder, `submission_template`.
**ALL YOUR ANSWERS** must be inside the `submission_template` folder. 

HW6 has several files that must be submitted. They all should be inside `submission_template` following the file structure below:

```
submission_template
├── src
    ├── collect.py
    ├── compute_title_lengths.py
    ├── collect_relationships.py
├── sample1.json
├── sample2.json
├── other folders are optional in this assignment
```

`src` can also carry any other additional code files that you need to write.

## Your code

`collect.py` must be successfully invoked with the following command:

`python collect.py`

And it should produce the sample files (which should look like [this](https://gist.github.com/hannelita/eb06c75a7b98cc2e16cb8727039e4911) ). Make sure the produced files are also in the root of `submission_template`.

`compute_title_lengths.py` must be successfully invoked with the following command:

`python compute_title_lengths.py PATH_TO_SAMPLE_JSON_FILE`


There are no named arguments, just one single argument with the full path for a sample JSON file. We will test this against the sample files you submit and against our own samples, so do not hardcode anything.

`collect_relationships.py` must be successfully invoked with the following command:

`python collect_relationships.py -c <config-file.json> -o <output_file.json>`

You do not have to submit your config file nor the output file - for this question, we'll test your script against our configuration directly.


If needed, you can have auxiliary code/scripts. Make sure everything goes under the `src` folder.

**DO NOT MODIFY** the structure of the folders in this assignment.



## Setting up the project

Make sure you have these elements installed in your computer:

* Python 3.6 or higher
* `pip` - see instructions [here](https://packaging.python.org/tutorials/installing-packages/)

Wait - what is all that?

At this time, you might have tried any other programming language, and you know most of them have a wide variety of libraries that you can use. In this course, we'll use a ton of them! Starting from this assignment.

`pip` will help you to manage these dependencies in a very easy way. Do you see a file named `requirements.txt`? It contains the libraries we'll need (to wither test, grade or run the assignment). It also bakes a fixed version on it, to avoid mismatching problems.

Once you install `pip`, run (in the `submission_template` folder):

```
pip install -r requirements.txt
```

(same command you ran for the other HW assignments).


## Are you on the right track?

For each HW assignment, we'll provide you with a set of automated tests. They are located under the `test` folder. 
For this assignment, do now edit the contents of it!

These tests should give you some guidance during the process of solving the problems.
In the `submission_template` folder, run:

```
python -m unittest
```

and check the output.

If you are on the right track, you should receive a nice message saying all check passed! 

**ProTip** Make sure the tests succeed in each HW assignment.


## Other tips

* There are multiple ways to solve this assignment.
* `virtualenv` is an optional asset to help you keeping your Python environment organized.
* In many operating systems, you might need to replace the command `python` with `python3`. Watch out for that and **make sure you are always using Python 3**.
* If you are familiar with Git, clone this repository. But be careful! You can easily run into merge issues. Make sure you are familiar enough with git before going down on this path.

# Submitting the assignment - VERY IMPORTANT - NEW INSTRUCTIONS


Once you are happy with your results, head to the `submission_template` folder and locate the `submission_wrapper.py` file (it is on the root of `submission_template`. Then run

`python submission_wrapper.py -id STUDENTID`.

**Replace `STUDENTID` with your McGill ID (a number).** For example, if your student ID is `123456`, run `python submission_wrapper.py -id 123456`.

**Make sure you call this script from the `submission_template` folder for hw4 and not from other folders.**

The script will zip everything needed for this assignment into a **`STUDENTID_submission_template.zip` file. You must submit the produced .zip on MyCourses**.


You can unzip and inspect the generated `submission_template.zip` file to double check it corresponds to the submission guideline; just make sure the final submission that goes to myCourses is **the generated zip file**.

Please do not submit any other file formats or folder structures.

**Note** This is VERY important. Please make sure you follow these steps accordingly, otherwise we won't be able to grade your assignment! If you mistype your ID, we won't be able to grade your submission!