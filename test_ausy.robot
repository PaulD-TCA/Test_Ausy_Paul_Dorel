*** Settings ***
Documentation     That test go on the Ranstad page, does a basic search (a Boulanger in
...               Bretagn), then click on the first job offer and finaly assert that
...               the part "Informations complémentaires" is completed..
...

Library          SeleniumLibrary


*** Variables ***
${SERVER}         https://www.randstad.fr/
${BROWSER}        Firefox
${DELAY}          3
${kind of job}    Boulanger

*** Test Cases ***
Open browser to randstad page

  Open Browser    ${SERVER}    ${BROWSER}
  maximize browser window

Input kind of job "Boulanger"
  Input Text    id:id_What    ${kind of job}
  Sleep    1s

#Select Bretagne From List
#  Scroll Element Into View  location
#  Sleep    1s

Accept cookies
  Press Keys  class:optanon-allow-all.accept-cookies-button  RETURN
  Sleep    4s

Click on first list result
  Press Keys  Job-1  RETURN
  Sleep    4s

Check the presence of additional information
   Page Should Contain  niveau d'études
   Page Should Contain  salaire minimum
   Page Should Contain  type de salaire

  Close Browser

*** Keywords ***
