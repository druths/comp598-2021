# Welcome to HW1! 

**Important instructions** 
Please read these instructions before submitting your assignment. 
If you do not follow the template specified here, **we will not able to grade your assignment**! 
To avoid pain and discomfort, follow the steps below carefully:

## Getting this code

This code contains the templates for every HW assignment in this course.
Download the code from Github.


## HW1
Navigate to the sub-directory `hw1`. There, you'll find another folder, `submission_template`.
**ALL YOUR ANSWERS** must be inside the `submission_template` folder. 

Note that HW1 has two mandatory `.tsv` files and a `README.md`. They should be inside `submission_template` directly. Like this:

```
submission_template
├── dataset.tsv
├── results.tsv
├── README.md
├── other folders are optional in this assignment
```

These three files should be added by you at the root of `submission_template`.

## Your code

If you are submitting any code, use the template we provided.
Add your scripts under the `scripts` folder. For this assignment, you'll have freedom to select file and function names. For future assignments, we'll be a bit more strict.

Add any dataset (`.csv` initial file) into the `data` folder.

Feel free to ignore the `src` folder for this assignment.

## Setting up the project

Make sure you have these elements installed in your computer:

* Python 3
* `pip` - see instructions [here](https://packaging.python.org/tutorials/installing-packages/)

Wait - what is all that?

At this time, you might have tried any other programming language, and you know most of them have a wide variety of libraries that you can use. In this course, we'll use a ton of them! Starting from this assignment.

`pip` will help you to manage these dependencies in a very easy way. Do you see a file named `requirements.txt`? It contains the libraries we'll need (to wither test, grade or run the assignment). It also bakes a fixed version on it, to avoid mismatching problems.

Once you install `pip`, run (in the `submission_template` folder):

```
pip install -r requirements.txt
```

For this assignment, it should install `pandas` for you.

After you run this command, you are ready to go!

## Are you on the right track?

For each HW assignment, we'll provide you with a set of automated tests. They are located under the `test` folder. 
For this assignment, do now edit the contents of it!

These tests should give you some guidance during the process of solving the problems.
In the `submission_template` folder, run:

```
python -m unittest
```

and check the output.

If you are on the right track, you should receive a nice message saying all check passed! Something like that:

```
RUNNING TESTS FOR HW1 - dataset.tsv
Ensure dataset.tsv exists
✅
Check header
✅
Check file contents
✅
You are all set! 💜
.
RUNNING TESTS FOR HW1 - results.tsv
Ensure results.tsv exists
✅
Check header
✅
Check file contents
✅
You are all set! 💜
.
----------------------------------------------------------------------
Ran 2 tests in 0.029s

```

**ProTip** Make sure the tests succeed in each HW assignment.

## Other tips

* `virtualenv` is an optional asset to help you keeping your Python environment organized.
* In many operating systems, you might need to replace the command `python` with `python3`. Watch out for that and **make sure you are always using Python 3**.
* If you are familiar with Git, clone this repository. But be careful! You can easily run into merge issues. Make sure you are familiar enough with git before going down on this path.

## Submitting the assignment


Once you are happy with your results, zip the **`submission_template` and send it through MyCourses**.

Make sure you zip and submit the entire folder. Just click on the `submission_template` folder and zip it once you complete the exercises.

The final zip file should be a `submission_template.zip` file.

Please do not submit any other file formats or folder structures.

**Note** This is VERY important. Please make sure you follow these steps accordingly, otherwise we won't be able to grade your assignment! 
