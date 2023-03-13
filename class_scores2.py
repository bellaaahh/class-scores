##
# Class_score2.py
# 13/03/2023

def minimum(scores):
    low_score = 50
    # set the minimum to the highest
    for score in scores:
        if score < low_score:
            low_score = score


    return low_score
        
        
        
 # if the score is less than the highest
 # set that as the newest minimum
    #return the minimum

def maximum(scores):
    high_score = 0
    for score in scores: 
        if score > high_score:
            high_score = score

    return high_score
    # do opposite of minimum
    
    

def average(scores):
    # iterating through a list
    total = 0
    counter = 0
    for score in scores:
        # total up the scores
        total += score
        # count the number of scores
        counter += 1 
    # return the total divided by the number
    av = total / counter
    
    return av



    
# Main routine
if __name__ == "__main__":
    class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
    class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]
    scores = class_a + class_b  # join lists together
    av = average(scores)
    print("This programs life purpose is to calculate the class scores\n")
    print("The average of class a is: ", average(class_a))
    print("The average of class b is: ", average(class_b))
    print("The average of class a and class b is: {}".format(average(scores)))
    print("The minimum is {}".format(minimum(scores)))
    print("The maximum is {}".format(maximum(scores)))
