from flask import Flask, request, jsonify, send_from_directory
import os
import random
from algebra import generate_algebra

app = Flask(__name__, static_folder='build')

# Serve React App (static files)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# API Endpoints
@app.route('/api/algebra', methods=['POST'])
def algebra_problems():
    data = request.json
    topic = data.get('topic', 'Algebra')
    problem_type = data.get('problem_type', "Solve for x (Linear)")
    difficulty = data.get('difficulty', "Medium")
    num_problems = data.get('num_problems', 5)
    
    # Initialize problem and solution lists
    problems = []
    solutions = []
    
    # Generate problems based on the topic
    if topic == "Algebra":
        for _ in range(num_problems):
            if problem_type == "Solve for x (Linear)":
                if difficulty == "Easy":
                    a = random.randint(1, 10)
                    b = random.randint(1, 20)
                    answer = b / a
                    problems.append(f"{a}x = {b}")
                    solutions.append(f"x = {answer}")
                elif difficulty == "Medium":
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 20)
                    answer = (c - b) / a
                    problems.append(f"{a}x + {b} = {c}")
                    solutions.append(f"x = {answer}")
                else:  # Hard
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 10)
                    d = random.randint(1, 20)
                    answer = (d - b) / (a - c) if a != c else "No solution"
                    problems.append(f"{a}x + {b} = {c}x + {d}")
                    solutions.append(f"x = {answer}")
            
            elif problem_type == "Evaluate Expression":
                x = random.randint(-10, 10)
                if difficulty == "Easy":
                    a = random.randint(1, 5)
                    b = random.randint(1, 10)
                    expr = f"{a}x + {b}"
                    result = a * x + b
                elif difficulty == "Medium":
                    a = random.randint(1, 5)
                    b = random.randint(1, 5)
                    c = random.randint(1, 10)
                    expr = f"{a}x² + {b}x + {c}"
                    result = a * (x ** 2) + b * x + c
                else:  # Hard
                    a = random.randint(1, 3)
                    b = random.randint(1, 5)
                    c = random.randint(1, 5)
                    d = random.randint(1, 10)
                    expr = f"{a}x³ + {b}x² + {c}x + {d}"
                    result = a * (x ** 3) + b * (x ** 2) + c * x + d
                
                problems.append(f"Evaluate {expr} when x = {x}")
                solutions.append(str(result))
            
            elif problem_type == "Factoring":
                if difficulty == "Easy":
                    a = random.randint(1, 5)
                    b = random.randint(1, 10)
                    problems.append(f"Factor: {a}x + {b}")
                    solutions.append(f"{a}x + {b} (already in factored form)")
                elif difficulty == "Medium":
                    a = random.randint(1, 5)
                    b = random.randint(-10, 10)
                    c = random.randint(-10, 10)
                    problems.append(f"Factor: {a}x² + {b}x + {c}")
                    solutions.append(f"See solution (quadratic factoring)")
                else:  # Hard
                    a = random.randint(1, 3)
                    b = random.randint(-5, 5)
                    c = random.randint(-5, 5)
                    d = random.randint(-10, 10)
                    problems.append(f"Factor: {a}x³ + {b}x² + {c}x + {d}")
                    solutions.append(f"See solution (cubic factoring)")
                    
            elif problem_type == "Systems of Equations":
                if difficulty == "Easy":
                    a1 = random.randint(1, 5)
                    b1 = random.randint(1, 10)
                    a2 = random.randint(1, 5)
                    b2 = random.randint(1, 10)
                    x = random.randint(-5, 5)
                    y = random.randint(-5, 5)
                    c1 = a1*x + b1*y
                    c2 = a2*x + b2*y
                    problems.append(f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}")
                    solutions.append(f"x = {x}, y = {y}")
                else:
                    # More complex systems for medium/hard
                    a1 = random.randint(1, 5)
                    b1 = random.randint(1, 5)
                    c1 = random.randint(1, 10)
                    a2 = random.randint(1, 5)
                    b2 = random.randint(1, 5)
                    c2 = random.randint(1, 10)
                    problems.append(f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}")
                    # Calculate solution using Cramer's rule
                    det = a1*b2 - a2*b1
                    if det == 0:
                        solutions.append("No unique solution")
                    else:
                        x = (c1*b2 - c2*b1)/det
                        y = (a1*c2 - a2*c1)/det
                        solutions.append(f"x = {round(x, 2)}, y = {round(y, 2)}")
    
    elif topic == "Geometry":
        for _ in range(num_problems):
            if problem_type == "Triangles":
                if difficulty == "Easy":
                    base = random.randint(5, 20)
                    height = random.randint(5, 20)
                    problems.append(f"Find the area of a triangle with base {base} and height {height}.")
                    solutions.append(f"Area = {base * height / 2}")
                elif difficulty == "Medium":
                    a = random.randint(5, 15)
                    b = random.randint(5, 15)
                    c = random.randint(max(a, b) - min(a, b) + 1, a + b - 1)  # Triangle inequality
                    problems.append(f"Find the perimeter of a triangle with sides {a}, {b}, and {c}.")
                    solutions.append(f"Perimeter = {a + b + c}")
                else:  # Hard
                    a = random.randint(3, 12)
                    b = random.randint(4, 12)
                    c = round(((a**2 + b**2) ** 0.5), 2)
                    problems.append(f"Find the hypotenuse of a right triangle with sides {a} and {b}.")
                    solutions.append(f"Hypotenuse = {c}")
            
            elif problem_type == "Circles":
                radius = random.randint(1, 15)
                if difficulty == "Easy":
                    problems.append(f"Find the area of a circle with radius {radius}.")
                    solutions.append(f"Area = {round(3.14159 * radius**2, 2)}")
                elif difficulty == "Medium":
                    problems.append(f"Find the circumference of a circle with radius {radius}.")
                    solutions.append(f"Circumference = {round(2 * 3.14159 * radius, 2)}")
                else:  # Hard
                    diameter = radius * 2
                    problems.append(f"Find the area of a circle with diameter {diameter}.")
                    solutions.append(f"Area = {round(3.14159 * (diameter/2)**2, 2)}")
            
            elif problem_type == "Rectangles":
                length = random.randint(5, 20)
                width = random.randint(3, 15)
                if difficulty == "Easy":
                    problems.append(f"Find the area of a rectangle with length {length} and width {width}.")
                    solutions.append(f"Area = {length * width}")
                elif difficulty == "Medium":
                    problems.append(f"Find the perimeter of a rectangle with length {length} and width {width}.")
                    solutions.append(f"Perimeter = {2 * (length + width)}")
                else:  # Hard
                    problems.append(f"Find the diagonal of a rectangle with length {length} and width {width}.")
                    solutions.append(f"Diagonal = {round(((length**2 + width**2) ** 0.5), 2)}")
    
    elif topic == "Arithmetic":
        for _ in range(num_problems):
            a = random.randint(1, 100) if difficulty == "Easy" else random.randint(10, 1000)
            b = random.randint(1, 100) if difficulty == "Easy" else random.randint(10, 1000)
            
            if problem_type == "Addition":
                problems.append(f"{a} + {b} = ?")
                solutions.append(f"{a + b}")
            elif problem_type == "Subtraction":
                # Ensure a >= b for easier subtraction
                if a < b:
                    a, b = b, a
                problems.append(f"{a} - {b} = ?")
                solutions.append(f"{a - b}")
            elif problem_type == "Multiplication":
                problems.append(f"{a} × {b} = ?")
                solutions.append(f"{a * b}")
            elif problem_type == "Division":
                # Create division problems with whole number answers
                product = a * b
                problems.append(f"{product} ÷ {b} = ?")
                solutions.append(f"{a}")
            elif problem_type == "Mixed":
                # Generate a random operation
                op = random.choice(["Addition", "Subtraction", "Multiplication", "Division"])
                if op == "Addition":
                    problems.append(f"{a} + {b} = ?")
                    solutions.append(f"{a + b}")
                elif op == "Subtraction":
                    if a < b:
                        a, b = b, a
                    problems.append(f"{a} - {b} = ?")
                    solutions.append(f"{a - b}")
                elif op == "Multiplication":
                    problems.append(f"{a} × {b} = ?")
                    solutions.append(f"{a * b}")
                else:  # Division
                    product = a * b
                    problems.append(f"{product} ÷ {b} = ?")
                    solutions.append(f"{a}")
    
    # Placeholder for other topics - you can expand these as needed
    else:
        for _ in range(num_problems):
            problems.append(f"Sample {topic} problem: {problem_type} ({difficulty} difficulty)")
            solutions.append("This is a placeholder solution. More topics will be implemented soon.")
    
    return jsonify({
        'problems': problems,
        'solutions': solutions,
        'problem_type': problem_type,
        'difficulty': difficulty,
        'topic': topic
    })

@app.route('/api/topics', methods=['GET'])
def get_topics():
    # Return available math topics
    topics = ["Algebra", "Geometry", "Trigonometry", "Calculus", "Discrete Math", "Word Problems", "Arithmetic"]
    return jsonify(topics)

@app.route('/api/problem-types', methods=['GET'])
def get_problem_types():
    topic = request.args.get('topic', 'Algebra')
    print(f"Getting problem types for topic: {topic}")
    
    problem_types = {
        "Algebra": ["Solve for x (Linear)", "Evaluate Expression", "Factoring", "Systems of Equations"],
        "Geometry": ["Triangles", "Circles", "Rectangles"],
        "Trigonometry": ["Right Triangle", "Unit Circle", "Identities"],
        "Calculus": ["Integrals", "Derivatives", "Limits"],
        "Discrete Math": ["Logic", "Truth Tables", "Set Theory"],
        "Word Problems": ["Age Problems", "Motion Problems", "Mixture Problems", "Work Problems"],
        "Arithmetic": ["Addition", "Subtraction", "Multiplication", "Division", "Mixed"]
    }
    
    result = problem_types.get(topic, [])
    print(f"Returning problem types: {result}")
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)