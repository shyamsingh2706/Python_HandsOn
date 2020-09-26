1) Read the Below details using Pandas

	A) "Roser" file that contains the roster information for the class.
	B) "Exam_Grades" file that contains homework and exam scores. there are three values reported for each homework assignment and exam

		The score the student received
		The maximum score for that assignment
		The time the student submitted the assignment

	C) "Quiz_Grades" files contain information for quiz grades

2) Apply Transformations and Data Cleansing to merge these data sets in order to calculate grades for each Student.
3) Calculating Grades With Pandas DataFrames
   There are three categories of assignments that you had in your class:

	Exams
	Homework
	Quizzes

  Each of these categories is assigned a weight toward the students’ final score. For your class this term, you assigned the following   weights:

	Category	Percent of Final Grade	Weight
	Exam 1 Score	5	0.05
	Exam 2 Score	10	0.10
	Exam 3 Score	15	0.15
	Quiz Score		30	0.30
	Homework Score	40	0.40

  The final score can be calculated by multiplying the weight by the total score from each category and summing all these values. The final   score will then be converted to a final letter grade.
  
  
	3.a Calculating the Exam Total Score : You’ll calculate grades for the exams first. Since each exam has a unique weight, you can calculate the total score for each exam individually
		each student scored between 0.0 and 1.0 on each of the exams. At the end of your script, you’ll multiply these scores by the weight to determine the proportion of the final grade.
	
	3.b Calculating the Homework Scores : 
		
		The max points for each homework assignment varies from 50 to 100. This means that there are two ways to calculate the homework score:

		1) By total score: Sum the raw scores and maximum points independently, then take the ratio.
		2) By average score: Divide each raw score by its respective maximum points, then take the sum of these ratios and divide the total by the number of assignments.
		
		The first method gives a higher score to students who performed consistently, while the second method favors students who did well on assignments that were worth more points. 
		To help students, you’ll give them the maximum of these two scores.
		At the end of your script, you’ll multiply final Homework score of each student by the weight to determine the proportion of the final grade.

    3.c Calculating the Quiz Score :  The quizzes also have different numbers of maximum points, so you need to do the same procedure you did for the homework. 
		The only difference is that the maximum grade on each quiz isn’t specified in the quiz data tables.
		Here are the max point for each Quiz.
		
		"Quiz 1": 11,  "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12
	
	3.d Calculate the Final Score for each Student as per above mentioned weights for each category
	
	3.e map each student’s ceiling score onto a letter grade. 

		A: Score of 90 or higher
		B: Score between 80 and 90
		C: Score between 70 and 80
		D: Score between 60 and 70
		F: Score below 60


4) separate the students into each section and sort them by their last name