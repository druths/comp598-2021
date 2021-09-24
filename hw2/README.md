# Welcome to HW2! 

**Important instructions** 
Please read these instructions before submitting your assignment. 
If you do not follow the template specified here, **we will not able to grade your assignment**! 
To avoid pain and discomfort, follow the steps below carefully:


In this directory, you'll find another folder, `submission_template`.
**ALL YOUR ANSWERS** must be inside the `submission_template` folder. 

Note that HW2 has a mandatory `.txt` file. They should be inside `submission_template` directly. Like this:

```
submission_template
├── ip_address.txt
├── other folders are optional in this assignment
```

This file should be added by you at the root of `submission_template`.

## Your code

`ip_address.txt` should be a single-line file containing only the IP Address of your instance. **Do not add anything else in this file**.

If you want to add a data file to test your script, add it under the `data` folder. This is optional.
Do not add any Apache files in your submission.

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

(same command you ran for the other HW assignment).


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

* There are multiple ways to obtain free credits for using AWS. AWS offers "free tier" options, in which they might cover up to 75$ of your bill if you go for the 'free tier' settings. For HW2, it might work (but not for future assignments). Note: The TAs won't have specific instructions to help with specific questions related to these alternatives, but it might be a good idea to give it a try if you really need to save money for this particular assignment.
* `virtualenv` is an optional asset to help you keeping your Python environment organized.
* In many operating systems, you might need to replace the command `python` with `python3`. Watch out for that and **make sure you are always using Python 3**.
* If you are familiar with Git, clone this repository. But be careful! You can easily run into merge issues. Make sure you are familiar enough with git before going down on this path.

## Submitting the assignment


Once you are happy with your results, zip the **`submission_template` and send it through MyCourses**.

Make sure you zip and submit the entire folder. Just click on the `submission_template` folder and zip it once you complete the exercises.

The final zip file should be a `submission_template.zip` file.

Please do not submit any other file formats or folder structures.

**Note** This is VERY important. Please make sure you follow these steps accordingly, otherwise we won't be able to grade your assignment! 
