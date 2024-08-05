Problem Statement: Develop a healthcare recommendation system that leverages user-input symptoms to identify potential diseases and recommends relevant healthcare providers based on specialty and availability. 

Solution: Our solution addresses the problem statement by allowing users to input their symptoms, generating potential disease matches, and providing detailed information about each disease, including recommended diet, precautions, and workouts. Additionally, the system recommends healthcare providers specialized in treating the identified diseases, considering factors such as specialty, distance, availability,experience and user ratings.

Approach - 
I have used different ai algorithms to train data of symptoms and align them with its diseases and its respective medications,diet and workout.I have used streamlite to run the app in the browser.For the doctor recommendation i have generated a dataset which include Doctor name,distance ,hospital ,fees ,rating and availability from various sources.I have given user preferences on basis of which best doctor will be recommended.It uses simple algorithm and takes few features to decide what will be the best.From disease the specialization is aligned and from specialization and user preference doctor is recommended.
I wanted to further add the real time geographical data to know exact distance and a strong dataset 
to give accuracy .I also wanted to provide a interface where user can book appointments directly so that they don’t have to visit hospital.I further wanted to use k-mean clustering to find similar hospitals and doctor with almost same preferences so that user can compare.
Regarding security aspect ,store only the minimum necessary information required for the functioning of the system, minimizing the risk associated with handling sensitive data.

Steps to run-
1.pip install -r requirements.txt
2.Open main.py
3.streamlit run main.py

