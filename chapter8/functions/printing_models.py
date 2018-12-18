import printing_functions

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendent', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
