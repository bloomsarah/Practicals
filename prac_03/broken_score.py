def main():
    """
    CP1404/CP5632 - Practical
    Broken program to determine score status
    """

    score = float(input("Enter score: "))
    result = score_calculator(score)
    print(result)

    def score_calculator(score):
        if score < 0 or score > 100:
            result = "Invalid"
        elif score >= 90:
            result = "Excellent"
        elif score >= 50 and score < 90:
            result = "Passable"
        else:
            result = "Bad"
        return result



main()

