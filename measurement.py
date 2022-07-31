import json


class Measurement():

    def __init__(self, measurement_dict, measurement_name="measurement"):
        self.measurement_dict = measurement_dict
        self.measurement_name = measurement_name
        for measurement in self.measurement_dict.keys():
            setattr(self, measurement, self.measurement_dict[measurement])
    
    def to_json(self):
        measurement_json = json.dumps(self.measurement_dict)
        with open("./results/" + ".".join([self.measurement_name, "json"]), "w") as f:
            f.write(measurement_json)
        pass

class MeasurementStatistics(Measurement):

    def __init__(self, measurement_dict, measurement_name="measurement"):
        super().__init__(measurement_dict, measurement_name)
