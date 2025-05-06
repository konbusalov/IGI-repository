from abc import ABC, abstractmethod
import csv, pickle

class Serializer(ABC):
    @abstractmethod
    def serialize(filename, data):
        pass

    @abstractmethod
    def deserialize(filename):
        pass

class CsvSerializer(Serializer):
    @staticmethod
    def serialize(filename, data):
        if isinstance(data, dict):
            columns = data.keys()
            with open(filename, 'w', encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
                writer.writerow(data)
        elif isinstance(data, list):
            columns = data[0].keys()
            with open(filename, 'w', encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
                writer.writerows(data)
        else:
            raise ValueError("Data must be a dictionary or a list of dictionaries.")
        
    @staticmethod
    def deserialize(filename):
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if len(rows) == 0:
                return None
            elif len(rows) == 1:
                return rows[0]
            else:
                return rows
            
class PickleSerializer(Serializer):
    @staticmethod
    def serialize(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    
    @staticmethod 
    def deserialize(filename):
        deserialized_data = None
        with open(filename, 'rb') as file:
            deserialized_data = pickle.load(file)
        return deserialized_data
    
class SerializerFactory:
    @staticmethod
    def get_serializer(filename):
        if filename.endswith('.csv'):
            return CsvSerializer
        elif filename.endswith('txt'):
            return PickleSerializer
        else:
            raise ValueError("Unsupported file format. Use .csv or .pkl/.pickle")




            
    
            





        

