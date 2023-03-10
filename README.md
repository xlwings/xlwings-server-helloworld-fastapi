# xlwings Server: Hello World

This sample works with:

* Excel on Windows
* Excel on macOS
* Excel on the web
* Google Sheets

## Quickstart

### Run backend server locally

This is a good option if you want to try the VBA client via `Demo.xlsm`.

* Local Python installation: install the Python dependencies into a virtual env or Conda env by running `pip install -r requirements.txt`, then run `python app/main.py` to run the server
* Docker: copy `.env.template` to `.env` and enter an xlwings (trial) license key. You can get one from here: https://www.xlwings.org/trial. Then run  `docker compose up`.

### Run backend server via Gitpod

This is a good option if you want to try out hte Excel Office Scripts or Google Apps Script clients.

* Open this repo in GitPod:    
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/xlwings/xlwings-server-helloworld)
* When you open it the very first time, it will ask you to enter an xlwings (trial) license key. You can get one from here: https://www.xlwings.org/trial

### Clients

* **Excel (via VBA)**:
  * Local: Once the server is running, you can click the button directly.
  * GitPod: Open the VBA editor via `Ctrl-F11` (Windows) or `Cmd-F11` (macOS) and replace the URL in `RunRemotePython` with the respective URL that GitPod prints.
* **Excel (via Office Scripts)**:
  * Local: You will need to use a tool like ngrok to expose your local server to the internet, see https://docs.xlwings.org/en/latest/pro/server/server.html#part-i-backend
  * GitPod: In Excel's `Automate` tab, click on `New Script`. Replace the content of the script with the content of `js/xlwings_excel.ts` as you find it in GitPod. `Save` the script, then click on `Run`.
* **Excel (via Office.js Add-ins)** For Office.js add-ins, please follow this repo instead: https://github.com/xlwings/xlwings-officejs-quickstart
* **Google Sheets (via Google Apps Script)**:
  * Local: You will need to use a tool like ngrok to expose your local server to the internet, see https://docs.xlwings.org/en/latest/pro/server/server.html#part-i-backend
  * GitPod: Click on `Extensions` > `Apps Scripts`. Replace the code in the file `Code.gs` with the code in `js/xlwings_google.js`. Then hit the `Run` button.
  
  If you run this the very first time, Google Sheets will ask you for the permissions it needs.

To learn about how to call your script from a button with Google Sheets or Excel on the web, have a look at the docs (link below).

## Next Steps:

* **Docs**:  
https://docs.xlwings.org/en/stable/pro/server/server.html

* **Authentication**:  
https://docs.xlwings.org/en/stable/pro/server/server_authentication.html
