import streamlit as st
from owlready2 import *
from datetime import datetime
import os

class CourseOntologyManager:
    def __init__(self, ontology_path):
        # Load the ontology
        self.onto = get_ontology(ontology_path).load()
        self.base_iri = "http://www.university.edu/ontologies/course#"

    def create_course(self, data):
        with self.onto:
            # Create course instance
            course_name = f"Course_{data['course_code'].replace(' ', '_')}"
            course = types.new_class(course_name, (self.onto.Course,))
            course_instance = course()
            course_instance.courseCode = data['course_code']
            course_instance.courseTitle = data['course_title']

            # Create and link course learning objectives
            for obj in data['course_objectives']:
                if obj.strip():  # Only create if not empty
                    obj_instance = self.onto.LearningObjective()
                    obj_instance.objectiveDescription = obj
                    course_instance.hasLearningObjective.append(obj_instance)

            # Create and link modules
            for module_data in data['modules']:
                module_instance = self.onto.Module()
                module_instance.moduleTitle = module_data['title']
                module_instance.moduleOrder = module_data['order']
                course_instance.hasModule.append(module_instance)

                # Module learning objectives
                for obj in module_data['objectives']:
                    if obj.strip():
                        obj_instance = self.onto.LearningObjective()
                        obj_instance.objectiveDescription = obj
                        module_instance.hasLearningObjective.append(obj_instance)

                # Key terms
                for term_data in module_data['key_terms']:
                    if term_data['term'].strip():
                        term_instance = self.onto.KeyTerm()
                        term_instance.termName = term_data['term']
                        term_instance.termDefinition = term_data['definition']
                        module_instance.hasKeyTerm.append(term_instance)

                # Learning content
                for content_data in module_data['content']:
                    if content_data['title'].strip():
                        content_instance = self.onto.LearningContent()
                        content_instance.contentTitle = content_data['title']
                        content_instance.contentType = content_data['type']
                        content_instance.contentURL = content_data['url']
                        module_instance.hasLearningContent.append(content_instance)

                # Assignments
                for assignment_data in module_data['assignments']:
                    if assignment_data['title'].strip():
                        assignment_instance = self.onto.Assignment()
                        assignment_instance.assignmentTitle = assignment_data['title']
                        assignment_instance.assignmentDescription = assignment_data['description']
                        
                        due_date_instance = self.onto.DueDate()
                        due_date_instance.dueDateTime = datetime.strptime(
                            assignment_data['due_date'], 
                            '%Y-%m-%d %H:%M'
                        )
                        assignment_instance.hasDueDate.append(due_date_instance)
                        module_instance.hasAssignment.append(assignment_instance)

    def save_ontology(self, save_path):
        self.onto.save(save_path)

def main():
    st.title("Course Information Entry Form")

    # Initialize session state for dynamic forms
    if 'module_count' not in st.session_state:
        st.session_state.module_count = 1

    # Course Basic Information
    st.header("Course Information")
    course_data = {
        'course_code': st.text_input("Course Code"),
        'course_title': st.text_input("Course Title"),
        'course_objectives': []
    }

    # Course Learning Objectives
    st.subheader("Course Learning Objectives")
    num_objectives = st.number_input("Number of Course Objectives", min_value=1, value=3)
    for i in range(num_objectives):
        obj = st.text_area(f"Course Objective {i+1}")
        course_data['course_objectives'].append(obj)

    # Modules
    st.header("Modules")
    num_modules = st.number_input("Number of Modules", min_value=1, value=st.session_state.module_count)
    st.session_state.module_count = num_modules

    course_data['modules'] = []
    for m in range(num_modules):
        with st.expander(f"Module {m+1}"):
            module_data = {
                'title': st.text_input(f"Module {m+1} Title"),
                'order': m+1,
                'objectives': [],
                'key_terms': [],
                'content': [],
                'assignments': []
            }

            # Module Learning Objectives
            st.subheader("Module Learning Objectives")
            num_mod_obj = st.number_input(f"Number of Objectives for Module {m+1}", min_value=1, value=2)
            for i in range(num_mod_obj):
                obj = st.text_area(f"Module {m+1} Objective {i+1}")
                module_data['objectives'].append(obj)

            # Key Terms
            st.subheader("Key Terms")
            num_terms = st.number_input(f"Number of Key Terms for Module {m+1}", min_value=1, value=3)
            for i in range(num_terms):
                term = st.text_input(f"Term {i+1} Name", key=f"term_{m}_{i}")
                definition = st.text_area(f"Term {i+1} Definition", key=f"def_{m}_{i}")
                module_data['key_terms'].append({'term': term, 'definition': definition})

            # Learning Content
            st.subheader("Learning Content")
            num_content = st.number_input(f"Number of Content Items for Module {m+1}", min_value=1, value=2)
            for i in range(num_content):
                content_title = st.text_input(f"Content {i+1} Title", key=f"content_title_{m}_{i}")
                content_type = st.selectbox(
                    f"Content {i+1} Type",
                    ['Video', 'Reading', 'Presentation', 'Interactive'],
                    key=f"content_type_{m}_{i}"
                )
                content_url = st.text_input(f"Content {i+1} URL", key=f"content_url_{m}_{i}")
                module_data['content'].append({
                    'title': content_title,
                    'type': content_type,
                    'url': content_url
                })

            # Assignments
            st.subheader("Assignments")
            num_assignments = st.number_input(f"Number of Assignments for Module {m+1}", min_value=1, value=1)
            for i in range(num_assignments):
                assignment_title = st.text_input(f"Assignment {i+1} Title", key=f"assignment_title_{m}_{i}")
                assignment_desc = st.text_area(f"Assignment {i+1} Description", key=f"assignment_desc_{m}_{i}")
                due_date = st.text_input(
                    f"Due Date (YYYY-MM-DD HH:MM)",
                    value="2024-12-31 23:59",
                    key=f"due_date_{m}_{i}"
                )
                module_data['assignments'].append({
                    'title': assignment_title,
                    'description': assignment_desc,
                    'due_date': due_date
                })

            course_data['modules'].append(module_data)

    if st.button("Submit Course Information"):
        try:
            # Initialize ontology manager
            ontology_manager = CourseOntologyManager("course_ontology.owl")
            
            # Create course and related instances
            ontology_manager.create_course(course_data)
            
            # Save the ontology
            ontology_manager.save_ontology("updated_course_ontology.owl")
            
            st.success("Course information successfully added to the ontology!")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
