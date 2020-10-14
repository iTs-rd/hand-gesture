<h1 align="center"> Hand-Gesture </h1>
<h3>Introduction</h3>

<strong>In this project user can input pin code of any district by showing his hand</strong><br>
For input we use webcam to take live video input of user. User can show no of finger for all 6 digit (one digit at a time) with the help of machine learning program will automatically count how many finger user is showing. After 6-digit number is generated it will show the result.

<br>

<h3>Requirements</h3>

```bash
- Python
- OpenCV-python
- Numpy
- Pandas
- Tensorflow 
```
<br>


<h3>1 Getting Started</h3>


<h3>1.1 Installation</h3>

   
1. Clone this repository
   
```bash
git clone https://github.com/iTs-rd/hand-gesture.git
```
   
2. Install the required packages
```bash
cd hand-gesture
pip install -r requirements.txt
```
<strong>If above code do not work replace pip by pip3.</strong><br>
It will install everything you need. If you have already installed some of the required packages it will skip that.

<h3>1.2 Check your present condition </h3>

First of all, You have to check your hand is properly detected or not.

```bash
python Set_HSV_values.py
```

It will open 3 windows, One will show normal video of input, 2nd window will show B&W video, and 3rd window will show 7 trackbars, you can play with the first 6 trackbars to get a good B&W video of yours in which your hand is properly distinctable. When it has done then close it.
<strong>Note:-</strong> If you want to reset all values then click on reset trackbar.

<strong>If all done the program is ready to run</strong>

<h3>1.3 Run program</h3>

To run the program simply enter this line

```bash
python index.py
```


<h3>summary</h3>

Run these code line by line

```bash
git clone https://github.com/iTs-rd/hand-gesture.git
cd hand-gesture
pip install -r requirements.txt
python Set_HSV_values.py
python index.py
```

<br><h4>Special Thanks to Rohit Jain</h4>
<h3>Contacts</h3>
Email- Rudresh.gupta.che19@iitbhu.ac.in <br>
Linkedin- https://www.linkedin.com/in/rudresh-gupta-b87a84190
