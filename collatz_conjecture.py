# FORMEL: 3x + 1 -> if 
def collatz(n):
    return 3 * n + 1

n = 0

try:
    while True:

        n += 1
        
        step = 1

        f = collatz(n)

        print("Number: " + str(n))

        print("Step " + str(step) + ": " + str(f) + " (3 * " + str(n) + " + 1)")

        while f != 1:

            step += 1

            old_f = f
            if f % 2 == 0:
                f /= 2
                print("Step " + str(step) + ": " + str(f) + " (" + str(old_f) + " / 2)")
                
            else:
                f = collatz(f)
                print("Step " + str(step) + ": " + str(f) + " (3 * " + str(old_f) + " + 1)")
            
        print("Number: " + str(n) + "; Total steps: " + str(step))
        input()

except KeyboardInterrupt:
    quit(0)
