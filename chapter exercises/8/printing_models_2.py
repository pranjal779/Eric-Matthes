def print_models(unprinted_designs, completed_models):
    """
    Simulated printing each design, until none are left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """SHow all the models that were printed."""
    print("\nTHe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 184
# print(model(unprinted_designs[:], completed_models))
