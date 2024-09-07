import os

os.makedirs('src', exist_ok=True)
os.makedirs('data', exist_ok=True)
os.makedirs('notebooks', exist_ok=True)
os.makedirs('models', exist_ok=True)

print('Folders created: src, data, notebooks, models.')

requirements_content = """
jupyter 
notebook
transformers
torch
gradio
opencv-python
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements_content)

print('requirements.txt file created with essential dependencies.')