name = input("Enter patient name: ")
symptoms = input(f"Enter symptoms for {name} (comma-separated): ")

facts = set(sym.strip().lower() for sym in symptoms.split(','))

print("\nEnter rules in the format: condition1,condition2 => conclusion")
print("Type 'done' when finished entering rules.")

rules = []
while True:
    rule_input = input("Rule:").strip().lower()
    if rule_input == 'done':
        break
    if "=>" in rule_input:
        conds, concl = rule_input.split("=>")
        conditions = set(c.strip() for c in conds.split(',') if c.strip())
        conclusion = concl.strip()
        rules.append((conditions, conclusion))
    else:   
        print(" Invalid")


new_inference = True
while new_inference:
    new_inference = False
    for conds, concl in rules:
        if conds.issubset(facts) and concl not in facts:
            facts.add(concl)
            new_inference = True

print(f"\n Inference result for {name.title()}:")
for fact in sorted(facts):
    print(f"{name}({fact})")
