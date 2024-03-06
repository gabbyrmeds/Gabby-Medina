def get_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue
            return score
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade():
    assignments_score = get_score("Enter total score for assignments (out of 100): ")
    midterm_score = get_score("Enter score for the midterm exam (out of 100): ")
    final_score = get_score("Enter score for the final exam (out of 100): ")

    assignments_weight = 0.4
    midterm_weight = 0.3
    final_weight = 0.3

    total_score = (assignments_score * assignments_weight) + (midterm_score * midterm_weight) + (final_score * final_weight)
    
    return total_score

def determine_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Grade Calculator!")
    print("This program calculates your overall grade based on scores for assignments, midterm, and final exam.")

    total_score = calculate_grade()
    letter_grade = determine_letter_grade(total_score)

    print(f"\nYour overall grade is: {total_score:.2f}")
    print(f"Your letter grade is: {letter_grade}")

main()
