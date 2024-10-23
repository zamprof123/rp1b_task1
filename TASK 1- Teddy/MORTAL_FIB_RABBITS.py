"""
RABBIT SEASON.
This tool is designed to take two inputs, n(the length of simuation) and m(the lifespan of rabbits)
and then return the expected number of rabbits at the end of month n.
"""

def extractNM(file_path):
    try:
        with open(file_path, 'r') as file:
            # read the first line and split it into parts
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 2:
                raise ValueError("The file must contain exactly 2 numbers split by whitespace")

            # assume the numbers are separated by whitespace, a better man would add some error handling here.
            n, m = map(int, line.split())
        
    except FileNotFoundError:
        print("NO FILE WAS FOUND, CHECK INPUT LOCATION FOR SPELLING MISTAKES")
        raise
    except ValueError:
        print("INT VALUES ONLY.")
        raise
    except Exception:
        print("what did you even do?")
        raise
        #explanatory checks
        
    return n, m

def rabbitsim(n, m):
    #new rabbits
    population = [0] * m #making a list the size of the lifecycle and kicking anything too old out of it
    population[0] = 1 # initial list seeding

    for _ in range(1, n): # simulates from month 1 to month n
        #behold, rabbits
        new_births = sum(population[1:]) # this sum gives us the number of reproducing rabbits
        
        population = [new_births] + population[:-1] #newbirths are added to the list, oldest gen are removed

    # return the total population at the end of n months
    return sum(population)
try:
    file_path = '(rabbits) Example File.txt'
    n, m = extractNM(file_path)
    print(rabbitsim(n, m)) 
except Exception:
    print("Failed to simulate rabbits )o:B")
    raise