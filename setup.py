from setuptools import find_packages,setup
""" Meaning:
Yahaan hum setuptools library se find_packages aur setup functions ko import kar rahe hain.

setup() project ko installable banata hai.

find_packages() aapke project mein jitne bhi Python packages hain unko automatically dhoondta hai."""


from typing import List
""" Meaning:
Yeh typing module ka List import kar raha hai, jo batata hai ki kaunsi function ki return type list hogi."""




def get_requirements(file_path:str) -> List[str]:
    """Meaning:
Yeh ek function define kar raha hai get_requirements, jo ek file ka path lega (string) aur return karega string ki list (dependencies ki list). """
    
    get_requirements =[]
    
    with open(file_path) as file_obj:
        """ Meaning:
File ko open kar raha hai file_path wale location se, aur uska object file_obj mein save ho raha hai."""
       
        requirements=file_obj.readlines()
        """  Meaning:
File ki saari lines read karke ek list mein daal raha hai, requirements list ban jaati hai."""
       
        requirements=[req.replace("\n","") for req in requirements] 
        """ Meaning:
Har line mein se newline character \n ko hata raha hai, taaki clean list mile dependencies ki."""


    
        

        return requirements
    """ Meaning:
Yeh cleaned list return kar raha hai function se."""
    
setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "sujen",
    author_email = "sujenpurty4@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages = find_packages()
)

"""Meaning:
Ab setup() function call ho raha hai, jo pura package define karega. 
Package ka version number define kar raha hai: 0.0.1
Author ka naam: sujen
Author ka email address.
requirements.txt file se dependencies read karke yahan specify kar raha hai ki install karne time kaunse packages chahiye.
Automatically aapke project ke saare packages detect karega aur unko installation mein include karega.

"""