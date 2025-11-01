""""" 
Creating a scrabble score calculator:
             
 We need:
    * a function for the calculator, which takes an argument 'word'
    * a variable to store the score in, set it to 0     
    * a for loop combined with an if statement to manage the handling of the score 
    * a placeholder variable (for the loop) - we will call it 'char'
    
 Data:
    Letter                        | Value
    A, E, I, O, U, L, N, R, S, T  |   1 
    D, G                          |   2
    B, C, M, P                    |   3
    F, H, V, W, Y                 |   4
    K                             |   5
    J, X                          |   8
    Q, Z                          |  10
    
"""""

one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
two_point_letters = ["d", "g"]
three_point_letters = ["b", "c", "m", "p"]
four_point_letters = ["f", "h", "v", "w", "y"]
five_point_letters = ["k"]
eight_point_letters = ["j", "x"]
ten_point_letters = ["q", "z"]

def scrabble_calculator(word):
    word_score = 0

    for char in word:  # --> this is our code block, now we move to the if statement:
        if char in one_point_letters:   # --> this will return true if it is and false if it is not
            word_score += 1
        elif char in two_point_letters:
            word_score += 2
        elif char in three_point_letters:
            word_score += 3
        elif char in four_point_letters:
            word_score += 4
        elif char in five_point_letters:
            word_score += 5
        elif char in eight_point_letters:
            word_score += 8
        elif char in ten_point_letters:
            word_score += 10
        else: word_score += 0

    return word_score

print(scrabble_calculator("zoo"))   # or ask for user input to calculate their own word
print(scrabble_calculator(input("Enter a word: ")))