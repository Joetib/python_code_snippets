# Use module 'modulegraph' to analyze Python module dependencies
# Install modulegraph using
# >> pip install modulegraph

from modulegraph.modulegraph import ModuleGraph

# Create a ModuleGraph object
graph = ModuleGraph()

# Add a Python file to analyze its dependencies
graph.run_script('your_script.py')

# Get the list of dependencies
dependencies = graph.flatten()

# Print the dependencies
for dependency in dependencies:
    print(dependency)
# Please Like and Subscribe