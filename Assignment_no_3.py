symptoms_of_disease = {
    "Normal-flu": ['fever', 'cough', 'cold', 'sore-throat'],
    "flu": ['fever', 'cough', 'cold'],
    "covid-19": ['breathless', 'fever', 'cough', 'cold', 'sore-throat'],
    "Diarrohea": ['stomach-pain', 'vomiting', 'diarrhoea']
}

symptoms_to_person = {
    "John": ['fever', 'cough', 'cold'],
    "Alice": ['breathless', 'cough', 'cold', 'sore-throat'],
    "kento": ['stomach-pain', 'vomiting', 'diarrhoea'],
    "Mento": ['cough', 'cold', 'sore-throat'],
}

def has_symptom(person, symptom):
    return symptom in symptoms_to_person.get(person, [])

def has_disease(person, disease):
    disease_symptoms = set(symptoms_of_disease.get(disease, []))
    person_symptoms = set(symptoms_to_person.get(person, []))
    return disease_symptoms.issubset(person_symptoms)

def run_diagnosis_loop():
    print("Type 'exit' to stop.")
    while True:
        person = input("Enter the person's name: ").strip()
        if person.lower() == "exit":
            break
        query = input("Enter a disease or a symptom: ").strip()
        if query.lower() == "exit":
            break

        if query in symptoms_of_disease:
            result = has_disease(person, query)
            print(f"HasDisease({person}, {query}): {result}")
        else:
            result = has_symptom(person, query)
            print(f"HasSymptom({person}, {query}): {result}")
        print("-" * 40)

run_diagnosis_loop()
