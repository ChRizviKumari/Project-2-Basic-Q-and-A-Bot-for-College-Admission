import json

class ChatBot:
    def __init__(self):
        with open('data/admissions_data.json', 'r') as file:
            self.data = json.load(file)
        self.context = {}

    def get_response(self, query):
        if 'procedure' in query:
            return self.data['admission_procedures']
        elif 'scholarship' in query:
            return self.data['scholarships']
        elif 'requirement' in query:
            return self.data['requirements']
        elif 'name' in query:
            return self.data['name']
        elif 'hi' in query:
            return self.data['greetings']
        elif 'hello' in query:
            return self.data['greetings']
        elif 'help' in query:
            return self.data['abilities']
        elif 'deadline' in query:
            return self.data['deadlines']
        elif 'program' in query:
            return self.data['academics']
        elif 'department' in query:
            return self.data['academics']
        elif 'engineering' in query:
            return self.data['engineering']
        elif 'arts' in query:
            return self.data['arts']
        elif 'science' in query:
            return self.data['science']
        elif 'address' in query:
            return self.data['address']
        elif 'locate' in query:
            return self.data['address']
        elif 'location' in query:
            return self.data['address']
        elif 'contact' in query:
            return self.data['contact']
        elif 'transport' and 'inside campus' in query:
            return self.data['transport_facilities_inside_campus']
        elif 'transport' in query:
            return self.data['transport_facilities']
        elif 'sport' in query:
            return self.data['sports']
        elif 'extra-curricular' in query:
            return self.data['extra_curricular']
        elif 'student body' in query:
            return self.data['student_bodies']
        elif 'hostel' in query and 'facilities' in query:
            return self.data['hostel_facilities']
        elif 'college type' in query:
            return self.data['college_type']
        elif 'teaching staff' in query:
            return self.data['teaching_staff_qualifications']
        elif 'department' in query:
            return self.data['department_info']
        elif 'fee structure' in query:
            return self.data['fee_structure']
        elif 'highest percentage' in query:
            return self.data['highest_percentage']
        elif 'topper' in query:
            return ", ".join(self.data['toppers'])
        elif 'infrastructure' in query:
            return self.data['infrastructure']
        elif 'timing' in query:
            return self.format_timings()
        elif 'tech class' in query:
            return self.data['tech_classes']
        elif 'extra curricular' in query:
            return self.data['extra_curricular_activities']
        elif 'sport facility' in query:
            return self.data['sport_facilities']
        elif 'pwd' in query:
            return self.data['pwd_facilities']
        elif 'hostel detail' in query:
            return self.data['hostel_details']
        elif 'hostel distance' in query:
            return self.data['hostel_distance']
        elif 'mess menu' in query:
            return self.data['mess_menu']
        elif 'hostel sports' in query:
            return self.data['hostel_sports']
        elif 'medical' in query:
            return self.data['medical_facilities']
        elif 'grading' in query:
            return self.data['grading_system']
        elif 'out of syllabus' in query:
            return self.data['out_of_syllabus_teaching']
        elif 'coding class' in query:
            return self.data['coding_classes']
        elif 'digital teaching' in query:
            return self.data['digital_teaching']
        elif 'student teacher ratio' in query:
            return self.data['student_teacher_ratio']
        elif 'male female ratio' in query:
            return self.data['male_female_ratio']
        elif 'student encouragement' in query:
            return self.data['student_encouragement']
        elif 'faculty training' in query:
            return self.data['faculty_training']
        elif 'soft skills training' in query:
            return self.data['soft_skills_training']
        elif 'placement cell' in query:
            return self.data['placement_cell']
        elif 'research session' in query:
            return self.data['research_sessions']
        elif 'sexual harassment' in query:
            return self.data['sexual_harassment_ragging']
        elif 'ragging' in query:
            return self.data['sexual_harassment_ragging']
        elif 'religious activity' in query:
            return self.data['religious_activities']
        elif 'women protection' in query:
            return self.data['women_protection_cell']
        elif 'student body' in query:
            return self.data['student_body']
        elif 'fire safety' in query:
            return self.data['fire_safety']
        elif 'rti' in query:
            return self.data['rti_act']
        elif 'on campus bank' in query:
            return self.data['on_campus_banks']
        elif 'fest' in query:
            return self.data['fests']
        elif 'pet policy' in query:
            return self.data['pets_policy']
        elif 'service scheme' in query:
            return self.data['service_schemes']
        elif 'competition' in query:
            return self.data['competitions']
        elif 'bye' in query:
            return self.data['farewell']
        elif 'see you' in query:
            return self.data['farewell']
        else:
            return "I'm sorry, I don't understand your question. Could you please rephrase?"

    def remember_context(self, user_query, user_response):
        self.context[user_query] = user_response

    def get_contextual_response(self, user_query):
        return self.context.get(user_query, None)

    def format_timings(self):
        timings = self.data['timings']
        formatted_timings = f"Library: {timings['library']}, Classes: {timings['classes']}, Labs: {timings['labs']}"
        return formatted_timings