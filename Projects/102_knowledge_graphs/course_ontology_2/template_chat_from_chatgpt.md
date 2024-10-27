I'm glad the ontology works for your needs! To create a program that allows teachers to input course details and automatically convert those inputs into OWL individuals and data property assertions, you can follow these steps to develop a basic application.

I'll outline how to approach this using Python with the `Flask` framework for the web form and `Owlready2` to manipulate the OWL ontology. Below is a basic structure you can follow:

### Prerequisites

You will need the following Python packages:

- **Flask**: To create the web form for input.
- **Owlready2**: To manipulate the OWL ontology and generate instances.

Install them using:

```bash
pip install Flask Owlready2
```

### 1. Basic Flask Web Form

First, let’s create a web form where teachers can input details about a course and its modules. Here is a simple Flask app that presents a form:

```python
from flask import Flask, render_template, request
from owlready2 import *

# Load the ontology
onto = get_ontology("file://path_to_your_ontology.owl").load()

app = Flask(__name__)

@app.route('/')
def course_form():
    return render_template('course_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    course_name = request.form['course_name']
    learning_objective = request.form['learning_objective']
    module_name = request.form['module_name']
    module_objective = request.form['module_objective']
    key_terms = request.form['key_terms']
    content = request.form['content']
    assignment = request.form['assignment']
    due_date = request.form['due_date']

    # Create instances in the ontology
    with onto:
        # Create course individual
        course_instance = onto.Course(course_name.replace(" ", "_"))
        course_instance.hasLearningObjective.append(onto.LearningObjective(learning_objective.replace(" ", "_")))

        # Create module individual
        module_instance = onto.Module(module_name.replace(" ", "_"))
        module_instance.hasLearningObjective.append(onto.LearningObjective(module_objective.replace(" ", "_")))
        course_instance.hasModule.append(module_instance)

        # Add key terms, content, and assignments
        for term in key_terms.split(','):
            module_instance.hasKeyTerm.append(onto.KeyTerm(term.strip().replace(" ", "_")))

        module_instance.hasContent.append(onto.Content(content.replace(" ", "_")))

        assignment_instance = onto.Assignment(assignment.replace(" ", "_"))
        assignment_instance.hasDueDate.append(onto.DueDate(due_date))
        module_instance.hasAssignment.append(assignment_instance)

    # Save the updated ontology
    onto.save(file="updated_ontology.owl")

    return "Course and Module information submitted and saved to ontology!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 2. HTML Form for Input (`templates/course_form.html`)

Here’s a simple HTML form (placed in the `templates` folder) that collects the data:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Input Form</title>
</head>
<body>
    <h1>Course Input Form</h1>
    <form action="/submit" method="POST">
        <label for="course_name">Course Name:</label>
        <input type="text" id="course_name" name="course_name" required><br><br>

        <label for="learning_objective">Course Learning Objective:</label>
        <input type="text" id="learning_objective" name="learning_objective" required><br><br>

        <h3>Module Details</h3>
        <label for="module_name">Module Name:</label>
        <input type="text" id="module_name" name="module_name" required><br><br>

        <label for="module_objective">Module Learning Objective:</label>
        <input type="text" id="module_objective" name="module_objective" required><br><br>

        <label for="key_terms">Key Terms (comma-separated):</label>
        <input type="text" id="key_terms" name="key_terms"><br><br>

        <label for="content">Content:</label>
        <textarea id="content" name="content" rows="4" cols="50" required></textarea><br><br>

        <label for="assignment">Assignment Name:</label>
        <input type="text" id="assignment" name="assignment" required><br><br>

        <label for="due_date">Assignment Due Date:</label>
        <input type="date" id="due_date" name="due_date" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### 3. Explanation of How the Program Works

- **Flask** serves the web form and handles the data submission.
- **Owlready2** allows manipulation of the ontology.
  - When the form is submitted, the data from the form is used to create instances of the ontology's classes.
  - The submitted course name, learning objectives, module details, key terms, content, and assignments are transformed into corresponding individuals and added to the ontology.
- **Instances**: 
  - For example, if a teacher enters "Introduction to AI" as the course name, a new individual `Introduction_to_AI` of the class `Course` is created. Similarly, instances are created for learning objectives, modules, and assignments.
- The **updated ontology** is saved as `updated_ontology.owl`.

### 4. Running the Program

To run the program:

1. Save the Python script and HTML form.
2. Launch the Flask app with:

   ```bash
   python your_flask_app.py
   ```

3. Open a browser and navigate to `http://127.0.0.1:5000/` to access the form.

4. After submitting the form, the ontology will be updated with the provided data, and saved to a new OWL file.

### Future Improvements

- You can extend this application to add more fields, validate inputs, or allow editing and deleting of course details.
- For a more complex UI, consider using a frontend framework like React.
- You could also incorporate an interface for viewing and querying the ontology data directly.

This program provides a basic, user-friendly way to input course details into the OWL ontology through a simple web form!