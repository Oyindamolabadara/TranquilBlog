<h1 align="center">TRANQUILBLOG TESTING FILE</h1>

### **Live Site:**

[Click here to visit the live site.](https://tranquilblog.herokuapp.com/)

### **Readme File:**
[Click here to visit the Readme File.](/README.md)

## **Manual Testing**
 

[Back to top](#)

## **Automated Testing**

### **Lighthouse**
<details>
<summary>Lighthouse</summary>

![Lighthouse Results](static/media/readme-images/lighthouse.png)

</details>

### **Code Validation**
The [W3C Markup Validator](https://validator.w3.org/ "Link to W3C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python` code used. The [JSHint JavaScript Validator](https://jshint.com/ "Link to the JSHint JavaScript Validator Site") was used to validate the `JavaScript` code used.

#### **Results:**

#### **HTML Pages**
<details>
<summary>HTML Validation Errors</summary>

![Errors returned](media/readme_images/html_errors_one.png)

![Errors returned](media/readme_images/html_errors_two.png)

<summary>HTML Validation</summary>

![Validation Results](media/readme_images/html_validation.png)

</details>

#### **CSS Stylesheets**
<details>

<summary>CSS Validation</summary>

![CSS Validation](media/readme_images/css_validation.png)

</details>

### **JavaScript Files**
<details>
<summary>JavaScript Files - JS Validation</summary>

<summary>bag.html</summary>

![JS validation results - bag.html - postloadjs](media/readme_images/bag.html_validation.png)

<summary>base.html</summary>

![JS validation results - base.html - postloadjs](media/readme_images/base.html_validation.png)

<summary>countryfield.js</summary>

![JS validation results - countryfield.js](media/readme_images/countryfield.js_validation.png)

<summary>quantity_input_script.js</summary>

![JS validation results - quantity_input_script.js](media/readme_images/quantity_input_script_validatio.png)

</details>

### **Python Files**
The python files were validated using Pep8 Online. However, I was unable to attach their images due to time constraints. 

### **Responsive Testing**
I have tested this project's responsiveness across multiple devices and screen sizes using Google developer tools.

### **Bugs**

* My app kept on crashing during my initial deployment to Heroku with the error message; "NameError: name 'application' is not defined". After having another pair of eyes to help go through it, I noticed that I missed out on making 'signature.herokuapp.com' a string in allowed host in settings.py.
* CSS was not loading on browser, even after hard refresh. I checked on the slack channel and found similar issues. It was solved by clearing my browser cache on chrome. 
* During the process of creating the contact us form, when trying to send a message through Gmail with my app, I got the error message; OSError: [Errno 101] Network is unreachable. I tried testing getting the emails using the terminal, which worked fine. In the tutorial I used, I was instructed to change settings to allow Gmail to use less secure apps. I found out that the setting is no longer available on google. Google updated their security such that there are port restrictions and emails don't work on GitPod anymore.
* The Django-Summernote editor was not showing in the Admin panel for my content/body, thus I was unable to add any review or comment to the body. In the console, I got the Uncaught Type Error; Cannot read properties of undefined (reading 'summernote'). I figured that the issue was with the iframe in the settings file. It was set to False. When I changed it to True, it worked fine and I was able to use the editor.
* Another deployment issue was a ProgrammingError; at /blog/ relation "products_product" does not exist. I had to reset the database entirely from the Elephant SQL dashboard and delete all migration files. I created an env.py file to contain the config var variables, then reloaded the data to the database.

    I had to update the DATABASE_URL on my Heroku Config Vars, then got another error from Heroku; cannot overwrite attachment values DATABASE_URL. I was told that I will not be able to remove the DATABASE_URL Heroku config var while I have a Heroku Postgres addon. I temporarily removed the Heroku Postgres addon to update the DATABASE_URL.
* The secret key had been previously exposed but was recovered and a new one was generated.



