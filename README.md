# xlwings Server: Hello World

This sample works with:

* Excel on Windows
* Excel on macOS
* Excel on the web
* Google Sheets

## Quickstart

### Development Server

* Open this repo in GitPod:    
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/xlwings/xlwings-remote-fastapi/tree/simplify)
* When you open it the very first time, it will ask you to enter an xlwings (trial) license key. You can get one from here: https://www.xlwings.org/trial

### Client

* **Desktop Excel**: Open the VBA editor via `Ctrl-F11` (Windows) or `Cmd-F11` (macOS) and replace the URL in `RunRemotePython` with the URL that GitPod prints. If your version of Excel has an automate tab, you can alternatively follow the instruction for Excel on the web below.
* **Google Sheets**: Click on `Extensions` > `Apps Scripts`. Replace the code in the file `Code.gs` with the code in `js/xlwings_google.js`. Then hit the `Run` button. If you run this the very first time, Google Sheets will ask you for the permissions it needs.
* **Excel on the web**: In the `Automate` tab, click on `New Script`. Replace the content of the script with the content of `js/xlwings_excel.ts`. `Save` the script, then click on `Run`.

To learn about how to call your script from a button with Google Sheets or Excel on the web, have a look at the docs (link below).

## Next Steps:

* **Authentication**:  
https://github.com/xlwings/xlwings-googlesheets-auth

* **Docs**:  
https://docs.xlwings.org/en/stable/remote_interpreter.html

* **Docker**:  
  A Docker image can be built for local development or can serve as a basis for production deployment:

  First, build the Docker image:

  ```
  docker build -t xlwings .
  ```

  Then run the server locally like this:

  ```
  docker run --rm -p 8000:8000 -e XLWINGS_LICENSE_KEY=your-license-key xlwings
  ```
