<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Anupama Chakrabhavi Venkatappa (ac298)</td></tr>
<tr><td> <em>Generated: </em> 4/13/2023 10:26:14 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/ac298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231638987-ef709d25-86a1-46e1-81be-782613da77c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Index Page displaying URL, &quot;Brought to you by...&quot; message , first<br>name, UCID and IS601 section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231639762-4f5c025d-0391-4334-99ea-daedc8d57877.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of URL and DIAR-ac298 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231640918-5796d3da-7ff1-4f4b-b0b6-c3fc8f594dd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of company search and company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231641198-be130c2b-ed03-40d2-9651-85bb739ab19d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL screenshot of company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231641534-2fd55d9b-9bf9-419f-816d-9525b8933f23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL screenshot of company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231641664-911fbe88-6d91-4107-bac9-f12db2768d09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL screenshot of employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231641803-4b761c39-7bc0-4fce-a811-57b529c60400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL screenshot of employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231642186-72383c6b-36ab-4b1b-841f-21e13fb99729.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of URL - employee search and add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231641987-0b7de038-35ae-45a4-8d6e-5682d33c8a7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL screenshot of admin import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231642607-f685de35-9927-4613-8984-100982e412ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of IS601_MP3_Companies table and 	IS601_MP3_Employees table with db  name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231917574-4167302f-b92a-46f0-a870-8e211b94b4d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1 and #2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231917957-6ea8400d-7687-489f-951f-5cb452db8db3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #2, #3, #4 and #5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231918321-6a4df6bd-b44e-4a7b-98f1-832b43b071e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #6<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231643348-ecdd7a20-68e6-442a-a23c-7c01c5e50e8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successfully importing the csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231642893-c56c00c6-e4b3-40f7-913e-26a626b6c376.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot with a reject flash for non-csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231646410-c0a56524-098d-4a4b-a9f9-586a220611d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some company data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231647001-effdd35f-13f4-4877-a3d4-c4146f2134fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some company data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231647112-52e750c6-63c6-457b-a4e5-ce2ff5e03a5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some company data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231647211-ad675a5d-e8fa-4763-9103-6e9bc9f4db91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some company data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231648090-03ad1701-9e12-453b-8345-c687fd759a28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some employee data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231648320-2a5f6e50-f93f-455f-8a64-8da2ab8dae95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some employee data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231648481-23070075-5607-4ab5-ab55-54b226226e95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some employee data was uploaded in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231919847-f814de99-7b54-4d53-a377-b15669623316.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some company data was uploaded in DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231920035-202abb25-de97-4be7-baa6-5746d9763c17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a screenshot showing some employee data was uploaded in DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231664337-1a4df6e6-a26e-48ea-92b9-5d22ba58385e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of checklist #1, #2, #3, #4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231664721-4d18cbd5-eded-41b9-ae66-6c34dc89b033.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of checklist #5, #6, #7, #8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231665299-10e2f763-d173-47cd-9b3c-b086c6e63efa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of a) fetch the updated data b)make this user-friendly c)pass the employee<br>data to the render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231665780-03ab5b07-b3be-475b-a90b-936d3723fbb3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231665901-c7cada7d-e80b-4b79-9af3-40c30620ebd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successfully  created/added employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231666237-8012ae73-28fc-4f37-853a-1409c898e51c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing first_name error message prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231666353-39819b41-af95-49e8-8c82-a37fec20eb2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231666512-ef3b9f54-2fb8-4c5b-b85b-06f6e7455f2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing last_name error message prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231666936-6b8c75ba-f33b-4f01-a907-b5cbd19b94ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231667207-a090daa9-27d1-43c0-8682-34d9b598bcfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231669898-41d80f90-40e3-4d1f-b1bb-ac81cec770a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of code for  #1, #2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231920658-e73b1d41-7db4-42bd-a813-e242427e6000.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231920829-20f42d1a-f823-4daa-a72b-b9aaf16626d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #2<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231670570-80d6587a-d4e3-42bf-a3d1-b6118574162e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231670771-83737c21-b3d5-4aeb-8ce9-0c24c19b0a78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231671669-689c79c5-c431-4b50-afd0-4043f5f5ceb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #3, #4, #5, #6, #7, #8, #9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231671989-c19b337e-bc99-4afe-9e44-8c8e0d647cf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of  #9, #10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231672500-fedea6d9-b13e-4122-950d-c2578fa12f74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with first_name filter applied; no combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231672741-5cc603ac-1df8-4bf5-a0a4-c0bc8adc93e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with lat_name filter applied; no combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231672919-c6c0b60d-40d9-4a32-aa2e-90251321f374.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with email filter applied; no combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231673384-a8e8f79b-219c-4d04-b06b-f47089e66974.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with company filter applied; no combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231673769-7f46b5bb-3b9f-40a4-883b-20df3426eae9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter - last_name is choosen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231673968-2e28bb21-24d7-4e00-8c93-c0202f59002a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter - last_name is choosen<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231674386-78134e76-372c-4e09-ac21-32671a71293e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1, #2, #3, #4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231676085-ff2db19f-e949-4199-8344-b435d2d28fc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #5, #6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231676496-fa0998c8-d11d-44d9-8110-4d53721e78c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #6, #7, #8, #9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231921323-252464ff-4e18-4c3e-bb56-3f2279e05be8.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing data before an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231921805-7d55985c-3502-4ebb-81ff-ea517d0181d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Editing the details of employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231922073-4d64cdbe-e56a-4597-8690-4a82bc9dccea.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing data after an edit&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231921500-1d27d692-dae3-4f49-8d85-02237029d8f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing data before an edit in DB&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231922309-e4277322-8c83-4428-9026-b4656ee6b309.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing data after an edit in DB&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231839671-d3bee5b2-2783-484f-abfa-872f964f3572.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231840001-78e63981-60d7-4f88-9a0b-0dc8a6c466be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #2 to #9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231840718-089d0e9d-7d58-454b-9d60-3ade5841bbbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #10 to #12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231841271-a7856239-e198-41ae-ac9b-e8129df16149.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231841393-9ed4a3e6-de10-4572-ab51-8f0cdb07cd08.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing success message&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231841632-caa28537-4603-404d-a39d-d4b551716562.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing name error prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231841777-568c889d-cc49-4ce4-b966-6f43e6b6b0ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing name error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231841960-c8851523-77e8-4014-9e92-8ca02f4b8b00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing address error prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231842059-9b8c7e6a-435c-4958-9651-12d8e05e0fa1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing address error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231842315-db2f0342-385b-47e1-895e-bcdcc8bb175c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing city error prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231842438-e3d32fdc-c56a-4a18-886a-1ad4e88643f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing city error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231843426-2ec63b13-422c-4824-a2ae-5e29ebbe8ac7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing zip error prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231843581-ca92fff8-600b-4d43-ba32-e432b6f6d25c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing zip error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231844507-cce565ec-0b7d-4916-beb7-bb01b9d580e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing country error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231844930-cf08a07c-2c87-46d8-9299-5d76a5e95b9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing state error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231922574-798a4f89-cc94-4d29-b0a7-29552cee4150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the  successfully added previous valid company data in DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231678141-b9738a54-c1a0-49d6-b05a-9b54640bec3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of  #1, #2, #3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231678573-a5a0b12b-1b0c-4c3f-9e2c-7c3e34e4ab54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #3, #4, #5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231678905-645bd74c-8676-4caf-9666-bf019383308c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231679214-91123b25-c315-434d-a484-65bdae434c7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #6, #7, #8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231852202-7c738f40-5d61-472f-8528-986a29639034.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing results with name filter applied; no combine filters&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231852363-66784c8d-bf1d-4396-94ef-fd3a65a16c56.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing results with name filter applied; no combine filters&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231852637-751ac588-4a92-435e-a320-cd7be8cee15d.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing results with country filter applied; no combine filters&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231853226-dcd43556-bcba-4182-a02c-bf7ead9ba124.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing results with state filter applied; no combine filters&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231853520-1a5e267a-bbe3-4212-838f-278520fac586.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Show one asc filter applied with name coulumn&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231853656-1ae8d8c5-62d4-420a-88c4-6441eb46b965.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Show one desc filter applied with name coulumn&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231883885-bad10646-c95f-4e54-b4e0-071ff421ce4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231884325-d358b573-272b-4e73-930c-1324774c9c68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of #2 to #8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231884646-970933ee-0a17-4e12-a7dd-a757711152ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot  of #9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231884762-13917a25-b521-4cf5-a438-559e23007f99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot  of #9 to #11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231885478-2b7b20cf-a3ac-4c2f-9435-d0eacb3ff3d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot  of #6 &amp; #8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231886152-6bb82312-b331-42ec-8d95-5cd0a2247692.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>example 1) Showing data before an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231886460-78cd9704-e988-4551-9d32-7c0e9e6a3fa4.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>    example 1)  Showing data before an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231886534-251d0865-b22e-4061-b852-6fc90d3e193d.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>example 1) Showing data before an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231886633-249db84c-5565-4acb-8e03-6d180b1cfd7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>example 1) edit updated successfully&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231887011-2f63f21d-3c1f-4276-ad8e-520a9c1eb8bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>    example 1) Showing data after an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231923597-628b6cfb-c008-4fc2-9390-5dd4d771c3b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>example 2) 	Showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231924041-705d96bf-070a-4293-a56b-7922b742ad33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>example 2) 	successfully editing the data - here, I have edited the city<br>name as &#39;Jersey City&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231924262-50f7da21-b3d1-4bd3-9814-186ad76d5f3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>example 2) 	Showing data after an edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231923795-5f3ec2a3-581f-480f-b8bd-d518f6a0675b.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>example 2) showing data in DB before an edit&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231924391-6f8893d0-9cf5-4d30-ae27-7ce4dccc201a.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>example 2)  showing data in DB after an edit. Here, city name&lt;br&gt;is edited as &#39;Jersey city&quot;&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231899250-07d05efb-c70e-473a-b54e-95c272430d9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231906717-cf368905-3788-484f-b5a4-2740003822b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231906889-f3580fe3-fd63-4683-8a56-953faf35ad6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting the company data before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231907011-5dae6d41-acb4-483e-a4ea-a0525881f990.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting the company data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231907659-89670491-7f31-438a-874b-cdbbe827752b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting the employee data before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231908068-4290214d-bd64-426e-99a6-0a95f37ad093.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting the employee data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231908431-d1fa61a1-29ba-4721-be26-e01669e18e29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of deleting an employee prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231908613-948bb9d3-3199-469a-8d93-ab2fa142e150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleted successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231908889-5fd7b8eb-8db9-42dd-885c-f44e16701787.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of deleting an employee after submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231909100-a3873913-48f7-42da-b7ca-2be023a9927a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of code for /delete route of company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231909631-00634588-6b19-4f14-9912-5db11762bcea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of  deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231909717-ca3ea03b-2131-4e17-ac2a-5586291d8947.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231909812-c106769c-f631-47ac-afff-080eb45901ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot of deleting a company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/231910381-e8dace80-5e41-4216-a78c-4c5852fe5a07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of all test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>There are definitely a lot of new concepts I learned while doing this<br>assignment, especially the database connection, creating tables in the database, deploying mp3-dev and<br>mp3-prod branches from heroku, creating a website using html files, learning how to<br>create a search/edit/delete options in HTML, while also learning from the errors while<br>running the code. I had one issue while creating a table in db,<br>which I overcame by creating the proper database connection, over again. Overall, this<br>assignment boosts confidence to handle any such projects in future.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/ac298" target="_blank">Grading</a></td></tr></table>