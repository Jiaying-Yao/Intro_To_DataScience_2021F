# Welcome to HW5! 

**Important instructions** 
Please read these instructions before submitting your assignment. 
If you do not follow the template specified here, **we will not able to grade your assignment**! 
To avoid pain and discomfort, follow the steps below carefully:


In this directory, you'll find another folder, `submission_template`.
**ALL YOUR ANSWERS** must be inside the `submission_template` folder. 

Note that HW5 has a mandatory `clean.py` and a `test_clean.py` file. They should be inside `submission_template` following the file structure below:

```
submission_template
├── src
    ├── clean.py
├── test
    ├── test_clean.py
├── other folders are optional in this assignment
```

This file should be added by you at the root of `submission_template`.

## Your code

`clean.py` must be successfully invoked with the following command:

`python clean.py -i <input_file> -o <output_file>`

The arguments for `-i` and `-o` are the full path locations for input and output files respectively.

If needed, you can have auxiliary code/scripts. Make sure everything goes under the `src` folder.

**The example file is inside the `data/` folder.**

**DO NOT MODIFY** the fixture file names, nor the test file name. You can write as many methods as you need in the test file. You can also write other fixtures if you want. 

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

In this assignment, you must write your own test cases! Follow the instructions on the PDF. In the `submission_template` folder, run:

```
python -m unittest
```

and check the output.

All your tests must pass!

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