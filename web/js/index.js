function getCurrentTime() {
    let server = document.getElementById("ntp").value;
    if (server.trim().length == 0) {
        document.getElementById("result").innerHTML = "Enter NTP server address!";
        return;
    }

    // call python function
    eel.ask_python_from_js_get_time(server);
    // NOTE
    // Following code will continuously query python with the time interval of 500ms
    /*
    setInterval(function () {
        eel.ask_python_from_js_get_time(server);
    }, 500);
    */
}

// this function will be executed from python
eel.expose(run_js_from_python);
function run_js_from_python(msg) {
    document.getElementById("result").innerHTML = msg;
}