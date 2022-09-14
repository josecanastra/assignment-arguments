# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

### Part 1: Greet Template
def greet(s_name, s_template="Hello, <name>!"):
    # Replace part of the template string with another string
    greeting = s_template.replace("<name>", s_name)
    return greeting

# Test Part 1
a1 = greet("Jane")
b1 = greet("John", "What's up, <name>!")
print(f"{a1}\n{b1}")
### End Part 1


### Part 2: Force
def force(mass, body="earth"):
    # Dictionary gravity celestial bodies
    body_gravity = dict(
        Sun = 274,
        Jupiter = 24.92,
        Neptune = 11.15,
        Saturn = 10.44,
        Earth =  9.798,
        Uranus = 8.87,
        Venus = 8.87,
        Mars = 3.71,
        Mercury = 3.7,
        Moon = 1.62,
        Pluto = 0.58
    )
    
    # Get gravity from the dictionary
    for key in body_gravity.keys():
        if body.lower() == key.lower():
            gravity = round(body_gravity[key], 1)
            formula = float(mass) * gravity
            return formula
    else:
        return "Body not found in the dictionary!"

# Test Part 2
a2 = force(mass=5)
b2 = force(mass=10.5, body="Sun")
c2 = force(mass=50, body="Pluto")
d2 = force(mass=25.75, body="Star")
print(f"{a2}\n{b2}\n{c2}\n{d2}")
print(type(b2))
### End Part 2


### Part 3: Gravity
def pull(m1, m2, d):
    m1 = float(m1)
    m2 = float(m2)
    d = float(d)
    g = 6.674 * 10 ** -11
    formula = g * ((m1 * m2) / d ** 2)
    return formula

# Test Part 3
a3 = pull(800, 1500, 3)
b3 = pull(0.1, 5.972*10**24, 6.371*10**6)
print(f"{a3}\n{b3}")
print(type(a3))
### End Part 3