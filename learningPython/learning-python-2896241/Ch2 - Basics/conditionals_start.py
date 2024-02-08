#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else

    if x < y:
        result = "x is less than y"
    elif x==y:
        result = "x is the same as y"
    else:
        result = "x is greater that y"
    print(result)

    # conditional statements let you use "a if C else b"
    result = "x < y" if x<y else "x>=y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three":
            result = 3

    print(result)

    
if __name__ == "__main__":
    main()
