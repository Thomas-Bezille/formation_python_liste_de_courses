from dataclasses import dataclass
import logging


LOGGER = logging.getLogger()

@dataclass
class Liste(list):
    nom: str
    
    def ajouter(self, element):
            if not isinstance(element, str):
                raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères !")
            
            if element in self:
                LOGGER.error(f"{element} est déjà dans la liste !")
                return False
            
            self.append(element)
            return True
