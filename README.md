# GUI apps for Python
I was using Tkinter, but it was not simpler for me in case of UI design. I Personally like Electron for creating Desktop applications with javascript. I was searching for Electron like framework for Python and found eel.
This project is basic tutorial for eel where we will create GUI app for desktop and call Python functions from Javascript and vice-versa.

## Installation
We need eel, ntplib for our project to work.
```bash
pip install eel
pip install ntplib
```

Folder structure for our project will be as like as below diagram.
```bash

eel_basic
|
|----|app.py
|
|----|web
     |
     |----html
     |    |----index.html
     |
     |----css
     |    |----index.css
     |
     |----js
     |    |----index.js
     |
     |----image
          |----img.jpg
```

## Let's Code
Clone the repository for running the exact code. I will describe how eel works.
app.py should look like this.
```python
import eel

# expose to javascript
@eel.expose
def ask_python_from_js_get_time(server):
    # DO SOMETHING

    # call javascript function
    eel.run_js_from_python(now_time)

# initialize the folder which contents html,js,css,etc
eel.init("web")

# start app
eel.start("html/index.html")
```
By defining a function with @eel.expose decorator, we will be able to access through Javascript. In this case we can access by calling eel.ask_python_from_js_get_time(arg) from javascript.


index.js should look like this.
```javascript
// this function is called when button is clicked
function getCurrentTime() {
    // call python function
    eel.ask_python_from_js_get_time(server);
}

// this function will be executed from python
// msg is the argument received from python side
// it will show the message received to user
eel.expose(run_js_from_python);
function run_js_from_python(msg) {
    document.getElementById("result").innerHTML = msg;
}
```
By calling expose method with the function as argument, we will be able to access it through Python.

## Run
Now, Open terminal and run this code from eel_basic folder.
```bash
python app.py
```
Your GUI app is ready.
