
## [ 1. OVERVIEW ]()
[ **1.1 About the data**: ]() 

**- The problem:** my team and I want to create an ML models that can classify different fruits with the pictures.
**- The approach:** we will try first by classifing Apple, Banana and Cherry.

[ **1.2 About the data**: ]() 

**1. Kaggle datatset:** There are many difference kind of fruit label in Kaggle dataset. We will simplify it and start first with only 3 classes. 

**2. Google datatset:** we learned along the way that Kaggle images are way different than real life pictures, so we solved this problem by 
adding Google images to train our model.

[ **1.3 What you can expect in this github**: ]() 
**1. How to build an simple ML to detect difference labels**
**2. Beautiful UI flask app templates.**
![](https://cdn.discordapp.com/attachments/660062916674060298/663622644662272021/unknown.png)

---
## [ 2. THE RESULT ]()

### *Our model can predict correctly around 90% fruits of three classes. Here was what we learned how to make our model worked.*

**Banana: for banana, preprocessing img is very important as well.**
- In order to predict banana correctly, preprocessing img is an important part. We tried two approach on preprocessing img and one worked very well, the other is not.

**Cherry: for cherry, data and model is what makes them work.**
- At first, since cherry and apple is really similar on picture. So we have to add more data and train models again and again so that they can learn correctly.

**Apple: just like cherry, data and model is important for the model to predict them correctly.**
- At first, since we have so many apple data. The model confidently predict cherry and banana as apple, so we use the technique to decrease the amount of apple data.

---



