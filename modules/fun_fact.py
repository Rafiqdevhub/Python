from random import choice

capital = "Islamabad"

bird = "Western"

flower = "Sunflower"

song = "Home on the Range"


def ran_fun_fact():
    fun_facts = [
        "Islamabad is the capital of Pakistan.",
        "The Western Meadowlark is the state bird of Islamabad.",
      
    ]

    index = choice("0123")

    print(fun_facts[int(index)])

if __name__ == "__main__":
    ran_fun_fact()
  
