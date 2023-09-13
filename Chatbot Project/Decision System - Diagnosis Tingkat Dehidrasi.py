welcome_prompt = "Welcome doctor, what would you like to do today?\n" \
                "- To list all patients, press 1\n- to run a new diagnosis, press 2\n" \
                "- to quit, press q\n"

name_prompt = "What is the patient's name?\n"

appearance_promp = "How is the patient's general appearance?\n- 1: Normal Appearance\n" \
                   "- 2: Irritable or lethargic\n"

eye_prompt = "How are the patient's eyes?\n- 1: Eyes normal or slightly sunken\n" \
             "- 2: Eyes very sunken\n"

skin_prompt = "How is the patient's skin when you pinch it?\n- 1: Normal skin pinch\n" \
              "- 2: Slow skin pinch\n"

error_message = "could not save patient and diagnosis due to invalid input"

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehidration"

patients_adn_diagnosis =[
    "Karina - Severe dehydration",
    "Jake - No dehydration",
    "Julia - Some dehydration"
]

def list_patients():
    for patiens in patients_adn_diagnosis:
        print(patiens)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + " - " + diagnosis
    patients_adn_diagnosis.append(final_diagnosis)
    print(f"Final diagnosis : {final_diagnosis} \n")

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""

def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def assess_appearance():
    appearance = input(appearance_promp)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def main():
    while True:
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()
