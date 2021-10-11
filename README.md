
# Smart cam

The world is rapidly urbanizing. This has resulted in a manifold increase in the number of vehicles plying on city roads engendering traffic violations to become more critical nowadays. This causes severe destruction of property and more accidents that may endanger the lives of the people. Sometimes emergency vehicles like ambulance, fire-Engine get stuck in the traffic causing threat to life in many cases. It is important to give priority to these vehicles and help to clear its path. A populated country like india it's hard to find and trace the accused to trace and find out the accused the police must continuously monitor the cctv footage of various location  which is a weary tedious task to solve this problem we found out a way to solve this problem through AI. To solve the alarming problem and prevent such unfathomable consequences a smart system is needed. here we came up with the solution of smart cam  where it can solve both of these problems


## Appendix

### Detailed Problem Statement:

#### Problem 1:-

Violation of traffic rules has become a major issue in today's developing world. The rise in the number of vehicles every day has eventually led to a gradual increase in the sum of traffic rule violations. Automation in daily life has gained a lot of importance in recent years. The main reason for the increase in the number of violations is because of the violating rules such as breaking traffic signals, over-speeding, not wearing a helmet  etc. In order to prevent these traffic violations, the police department should be present on the road and must continuously monitor the vehicles violating traffic rules. According to the traffic rules, wearing a helmet is mandatory and violating this rule results in huge fines. Despite implementing this rule, many motorcyclists are ignorant. To prevent we came with an idea of Smart cam
#### Problem 2:-
A highly populated country like India  faces too many traffic jams. Sometimes emergency vehicles like ambulance, fire-Engine get stuck in the traffic causing threat to life in many cases. It is important to give priority to these vehicles and help to clear its path. But it is difficult or sometimes impossible for traffic police to handle this. For this reason, we need an automated system that will be able to detect an emergency Vehicle  in a heavy traffic road, let the controller know or automatically navigate other cars to clear its path. 

#### Problem 3:- 
A populated country like india it's hard to find and trace the accused to trace and find out the accused the police must continuously monitor the cctv footage of various location  which is a weary tedious task to solve this problem we found out a way to solve this problem through AI 


  
### Prescribed Solution:
#### For solving the problem 1 , 2 and 3 we came up with a integrated solution:-
We use traffic cameras in the desired location for detecting the motorcycle. System creates bounding boxes using (YOLOV5) over the two wheelers around it and crops the frames then supplied it to a Convolutional neural network model that has been applied for classifying whether the rider is with helmet or not. If the helmet has been detected then the system will consider there is no violation else it stores the picture of the accused and number plate of accused bike then  sends it to the control room. It also detects emergency vehicles from CCTV footage using the deep convolutional neural network.
If our model classify weather a emergency vehicle present in the frame then the model sends a signal to the traffic light and traffic light changes the signal  to green.

## All features of our project
1)Emergency vehicle detection

2)Traffic rule violation detection(helmet detection)

3)Vehicle detection and counting 

4)Object detection and  counting 

5)Accused detection



## Acknowledgements

 - [presentation](https://bit.ly/3iQACvW)
 - [Document ](https://bit.ly/3BvTDLy)
 - [Connect with me for models](https://www.linkedin.com/in/pradeepodela/)

## DEMO

https://user-images.githubusercontent.com/72432569/136819806-b283adbe-81ae-4893-9de1-23805196ba49.mp4




## NOTE :- models are not uploaded to get the models connect with me on  <a href= https://www.linkedin.com/in/pradeepodela/>Linkedin</a>
## Run Locally

Clone the project

```bash
  git clone https://github.com/pradeepodela/Smart-cam
```

Go to the project directory

```bash
  cd Smart-cam
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run main.py 
```

  
## Authors

- [@pradeepodela](https://github.com/pradeepodela)

  
