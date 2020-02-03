from parser import parser
from calc import calc

if __name__ == "__main__":
    # parser returns arguments `pre-processed` for us
    numbers, oper, rev = parser()
    # use calc to calculate result of our program
    res = calc(numbers, oper)
    # check variable res to give appropriate visualization
    if rev:
        print(str(res)[::-1])
    else:
        print(res)

    # TIP:
    # Check these 3 steps:
    # 1.Get parameters from shell command (input parameters "numbers, operation", output parameters "reverse")
    # 2.Process data according to input parameters
    # 3.Output result according to output parameters