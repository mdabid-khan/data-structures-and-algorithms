Hero = ["A", "B", "C", "D", "E"]
target = "C"

def linear_Search(Hero, target):
    for i in range(len(Hero)):
        if Hero[i] == target:
            return f"kick {target}! at the postion {i+1}"
    return f"Sorry {target} is not found!"

print(linear_Search(Hero, target="A"))
