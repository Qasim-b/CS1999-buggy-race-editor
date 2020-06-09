CS1999: Buggy Race Editor
=========================

> This is the "buggy editor" component of the Foundation Year Computer Science
> project at RHUL.

Overview
--------

This is the skeleton of an application for editing a racing buggy.

It runs as a webserver so you can edit the configuration of a buggy in your
browser. The editor can then generate the data, in JSON format, that you need
in order to enter races on the [race server](http://rhul.buggyrace.net).

The application is written in Python3 using the
[Flask](https://palletsprojects.com/p/flask/) microframework.

> It's also written in a way which you can and should fix! You should be able
> to get it up and running (with SQLite) without needing to change the code...
> but from that point on you'll need to change pretty much everything to make
> it better (including switching away from SQLite, perhaps?).

GitHub repo: [RHUL-CS-Projects/CS1999-buggy-race-editor](https://github.com/RHUL-CS-Projects/CS1999-buggy-race-editor])


**Project overview**
---------------------------------
**task1**
ADD:
>initially I put in most of the fields as text inputs. However, when I finished all
>inputs were either radio buttons for equipment types, number fields for quantities or
>color pickers for flag colours. This meant that there was less need for validation as the
>user was restricted in what they could input.

VALID:
>initially I used isdigit() on all fields requiring a number.
>However, afterwards it was not necessary as I had changed the fields that required numbers
>into ones that only accepted numbers. Thus isdigit became redundant. However, problems
>could arise from the input of negative numbers into the fields which should be fixed.

STYLE:
>I changed the background, banner and button themes to a beige and green style.

**task2**
EDIT:
>I was able to load the forms for non radio buttons as there were errors if I tried
>applying the same code to them. This should be fixed in future.

FORM:
>I lined up all the inputs, labelled all of them. Displayed errors at the top.

COST:
>Cost mostly working, does not properly work with consumable fuels and also armor
>calculations are not their to figure out proper cost.

RULES:
> There are game rules, however if user breaks multiple only one error is shown.
> Data isn't saved unless there are no errors

**task3**
Flag:
>FLAG, partially completed- I am able to show the colour of the flag to the user when they edit their buggy

ENV:
> when programming, I set flask to development by inputting
> 'FLASK_ENV="development" python app.py' into Git Bash
> if I want to go into production mode
> 'FLASK_ENV" python app.py' into Git Bash
> production is the default state
>

MULTI:
>Sort of works, always starts off with a buggy from the database, also the stored values for radio buttons don't work due to limitations.
>Couldn't get DELETE to work, tried putting buggy_id in but wouldn't update.

Delete:
>Tried to implement using what I learnt from multi however, it said that it deleted the entry yet it would still appear on buggy show.
>So I removed it as to not cause further issues.

AUTOFILL:
> Never got around to doing, however if possible would have preferred to implement server side thus meaning I had control over autofill.
> However could also be useful on client side if they wanted to modify their own autofill.

Tests:
> Will do test plan, shown in testing.md file
