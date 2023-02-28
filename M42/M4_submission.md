<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Anupama Chakrabhavi Venkatappa (ac298)</td></tr>
<tr><td> <em>Generated: </em> 2/28/2023 1:18:13 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/ac298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221760410-204247f6-f9a4-42b5-9cc0-97d3c7ba937a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of valid Addition Function: This is a Python class named &quot;MyCalc&quot;<br>that has an attribute &quot;ans&quot; initialized to 0 in its constructor method &quot;init&quot;.<br>It also has a method named &quot;add&quot; that takes a parameter &quot;x&quot; and<br>adds it to the &quot;ans&quot; attribute. It does not have any other methods<br>or attributes defined. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221760410-204247f6-f9a4-42b5-9cc0-97d3c7ba937a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid Subtraction Function: The &quot;subtract&quot; method in the &quot;MyCalc&quot; class is<br>used to subtract a given value &quot;x&quot; from the current value of the<br>&quot;ans&quot; attribute of the object. It takes a single parameter &quot;x&quot; that represents<br>the value to be subtracted. It then updates the value of the &quot;ans&quot;<br>attribute by subtracting the value of &quot;x&quot; from it using the &quot;-&quot; operator.<br>The updated value of &quot;ans&quot; is stored back in the &quot;ans&quot; attribute. This<br>method can be called on an instance of the &quot;MyCalc&quot; class to perform<br>subtraction operations on the &quot;ans&quot; attribute.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221760410-204247f6-f9a4-42b5-9cc0-97d3c7ba937a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid Multiplication Function: The &quot;multiply&quot; method in the &quot;MyCalc&quot; class is<br>used to multiply a given value &quot;x&quot; with the current value of the<br>&quot;ans&quot; attribute of the object. It takes a single parameter &quot;x&quot; that represents<br>the value to be multiplied. It then updates the value of the &quot;ans&quot;<br>attribute by multiplying the value of &quot;x&quot; with it using the &quot;*&quot; operator.<br>The updated value of &quot;ans&quot; is stored back in the &quot;ans&quot; attribute. This<br>method can be called on an instance of the &quot;MyCalc&quot; class to perform<br>multiplication operations on the &quot;ans&quot; attribute.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221760410-204247f6-f9a4-42b5-9cc0-97d3c7ba937a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The &quot;divide&quot; method in the &quot;MyCalc&quot; class is used to divide the current<br>value of the &quot;ans&quot; attribute of the object by a given value &quot;x&quot;.<br>It takes a single parameter &quot;x&quot; that represents the divisor.  First, it<br>checks if the value of &quot;x&quot; is equal to zero. If it is,<br>the method prints an error message &quot;Error: Cannot divide by zero.&quot; because division<br>by zero is undefined in mathematics.  If &quot;x&quot; is not zero, the<br>method updates the value of the &quot;ans&quot; attribute by dividing the current value<br>of &quot;ans&quot; by &quot;x&quot; using the &quot;/&quot; operator. The updated value of &quot;ans&quot;<br>is then stored back in the &quot;ans&quot; attribute.  This method can be<br>called on an instance of the &quot;MyCalc&quot; class to perform division operations on<br>the &quot;ans&quot; attribute, but it will raise an error if the divisor is<br>zero.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221764966-dd67f512-3df6-498b-8d30-da337066b939.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passing number-add-number Test Case and code snippet: The &quot;test_add&quot; function tests<br>the &quot;add&quot; method of the &quot;MyCalc&quot; class. It first creates an instance of<br>the &quot;MyCalc&quot; class called &quot;calculator&quot;. Then it calls the &quot;add&quot; method of the<br>&quot;calculator&quot; object twice, with arguments 2 and 3 respectively. This should result in<br>the &quot;ans&quot; attribute of the &quot;calculator&quot; object being updated to 5.  The<br>function then uses the &quot;assert&quot; statement to check if the value of the<br>&quot;ans&quot; attribute of the &quot;calculator&quot; object is equal to 5. If the value<br>of &quot;ans&quot; is 5, the &quot;assert&quot; statement passes and the test is successful.<br>If the value of &quot;ans&quot; is not equal to 5, the &quot;assert&quot; statement<br>fails and an error is raised indicating that the test has failed. <br>The UCID and date provided appear to be a comment, possibly indicating the<br>author of the code and the date it was last modified. However, they<br>do not affect the behavior or functionality of the &quot;test_add&quot; function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221765346-f4551c80-e31b-4dee-b55d-a5479c28714b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passing ans-add-number Test Case and code snippet: The &quot;test_ans_add&quot; function tests<br>the functionality of the &quot;ans&quot; attribute of the &quot;MyCalc&quot; class when used in<br>conjunction with the &quot;+&quot; operator.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221765686-3202c309-9353-4324-8065-d8b9332ce005.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of passing number-sub-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221765969-f01b90db-cbea-4b79-ba98-75bc8941a402.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of passing ans-sub-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221766574-8af26f0c-770e-47b7-9902-bb9d955326c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passing number-mult-number Test Case and code snippet: The &quot;test_multiply&quot; function tests<br>the &quot;multiply&quot; method of the &quot;MyCalc&quot; class. The  &quot;test_multiply&quot; function tests if<br>the &quot;multiply&quot; method correctly updates the value of the &quot;ans&quot; attribute of the<br>&quot;MyCalc&quot; object when it is called.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221766933-79314ec5-4f66-40f3-a303-bdef39857882.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passing ans-multi-number Test Case and code snippet: The &quot;test_ans_multiply&quot; function tests<br>the functionality of the &quot;ans&quot; attribute of the &quot;MyCalc&quot; class when used in<br>conjunction with the &quot;<em>&quot; operator. the &quot;test_ans_multiply&quot; function tests if the &quot;ans&quot; attribute<br>of the &quot;MyCalc&quot; class can be used to correctly evaluate a mathematical expression<br>involving multiplication when it is used in conjunction with the &quot;</em>&quot; operator.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221763200-23c4aa1f-0c55-41e9-9883-40bb15707e36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of passing number-div-number Test Case and code snippet: this code is a<br>unit test for the divide method of the MyCalc class, which checks that<br>the method correctly divides the calculator&#39;s internal state by a given number.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420651/221763401-cf65644f-5d28-4c73-8a0b-982fb293c700.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passing ans-div-number Test Case and code snippet: The &quot;test_ans_divide&quot; function is<br>a test case for the &quot;ans&quot; attribute of the &quot;MyCalc&quot; class when used<br>in conjunction with the &quot;/&quot; operator.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>This homework helped me to learn the use of arithmetic operations along with<br>basic fundamentals of python.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>After creating the test scenario, we would execute the test case and compare<br>the results to what was anticipated. The test case succeeds if the actual<br>output matches the anticipated output. The test case fails if the actual output<br>differs from what was anticipated, and we would then need to look into<br>and address any code problems.<div><br></div><div>This homework helped to understand the use of basic<br>arithmetic operations along with the test cases.</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anu0408/IS601/pull/15">https://github.com/Anu0408/IS601/pull/15</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/ac298" target="_blank">Grading</a></td></tr></table>