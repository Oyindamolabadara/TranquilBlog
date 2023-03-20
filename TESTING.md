<h1 align="center">TRANQUILBLOG TESTING FILE</h1>

### **Live Site:**

[Click here to visit the live site.](https://tranquilblog.herokuapp.com/)

### **Readme File:**
[Click here to visit the Readme File.](README.md)

## **Manual Testing**
![Manual Testing](static/media/readme-images/manual-testing-one.png)
![Manual Testing](static/media/readme-images/manual-testing-two.png)
![Manual Testing](static/media/readme-images/manual-testing-three.png)
![Manual Testing](static/media/readme-images/manual-testing-four.png)


[Back to top](#)

## **Automated Testing**

### **Lighthouse**
<details>
<summary>Lighthouse</summary>

![Lighthouse Results](static/media/readme-images/lighthouse.png)

</details><br>

### **Code Validation**
The [W3C Markup Validator](https://validator.w3.org/ "Link to W3C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The Code Institute Python Linter was used to validate the `Python` code used. 

#### **Results:**

#### **HTML Pages**
<details>
<summary>HTML Validation Errors</summary>

![Errors returned](static/media/readme-images/html-errors.png)

<summary>HTML Validation</summary>

![Validation Results](static/media/readme-images/html-validation.png)

</details><br>

#### **CSS Stylesheets**
<details>

<summary>CSS Validation</summary>

![CSS Validation](static/media/readme-images/css-validation.png)

</details><br>

### **Python Files**
<details>

<summary>Blog</summary>

admin.py
![blog-admin.py](static/media/readme-images/blog-admin.png)

forms.py
![blog-forms.py](static/media/readme-images/blog-forms.png)

models.py
![blog-models.py](static/media/readme-images/blog-models.png)

urls.py
![blog-urls.py](static/media/readme-images/blog-urls.png)

views.py
![blog-views.py](static/media/readme-images/blog-views.png)

</details>

<details>
<summary>Home</summary>

forms.py
![home-forms.py](static/media/readme-images/home-forms.png)

urls.py
![home-urls.py](static/media/readme-images/home-urls.png)

views.py
![home-views.py](static/media/readme-images/home-views.png)

</details>

<details>
<summary>Tranquilblog</summary>

urls.py
![home-urls.py](static/media/readme-images/tranquilblog-urls.png)

</details>

<details>

<summary>Users</summary>

forms.py
![users-forms.py](static/media/readme-images/users-forms.png)

models.py
![users-models.py](static/media/readme-images/users-models.png)

signals.py
![signals-urls.py](static/media/readme-images/signals.png)

views.py
![users-views.py](static/media/readme-images/users-views.png)

</details><br>

## **Bugs**
### **Solved Bugs**
* I had an issue using crispy forms for my blog posts, getting the “TemplateDoesNotExist” error when I clicked on a post. I found a solution in this [stack overflow link](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown),  adding these lines to my settings file; 
    `CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5”` and
    `CRISPY_TEMPLATE_PACK = 'bootstrap5'`
* Unable to display success message after a post has been successfully deleted. I learnt that the SuccessMessageMixin hooks to form_valid which is not present on DeleteView to push its message to the user. [Link to solution here](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown). 
* I had an issue with my images loading, using Cloudinary as my media and static files storage. It was being uploaded to Cloudinary, but the path of the image was not changing as it is a media file. I had to move the media folder within the static files, so it would be uploaded to Cloudinary . I also had to hard code the image and then change the file path to the image. This was solved with the help of a CI tutor. 

### **Unsolved Bugs**
I had limited time to fix the following. In the first submission, I did not implement these features, hence making it challenging to find a way around it promptly. 
* The image fields were not showing the current image for the blog and profile. 
* I was unable to resize the profile images, as adding images with high resolution fills and distorts the whole page. Resizing the image would also have saved space when uploaded on the web server. 
* Noticed very close to submission that the card text on the landing page was not very responsive on small screen sizes.<br>

### **Note:**
The contact form was left in testing mode. The email is sent to the CLI and not to an email inbox, using the Django email backend in settings.py. 


### **Responsive Testing**
I have tested this project's responsiveness across multiple devices and screen sizes using Google developer tools.<br>





