#!/usr/bin/env python3

# -------------------------------------
# Test Scores Program
# Murach's Python Programming
# Chapter 2 Exercises
# -------------------------------------

# display a welcome message
print("The Test Scores Program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
#total_score = 0  # initialize the variable for accumulating scores
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))

# calculate the total score
total_score = score1 + score2 + score3

# calculate average score
average_score = round(total_score / 3)

# format and display the result
print("======================")
print("Your Scores:   " + str(score1) + " " + str(score2) + " " + str(score3))
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")