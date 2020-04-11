pushd %~dp0
 python email-sim.py email username password emailrecieveremail "C:\\Emailbot.txt"
REM python email-sim.py messenger username password messengerpersonname "C:\\Emailbot.txt"
REM python email-sim.py instagram username password messengerpersoname "C:\\Emailbot.txt"
REM taskkill /f /im chromedriver.exe
REM taskkill /f /im chrome.exe
popd