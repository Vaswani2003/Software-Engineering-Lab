class Weather:
    def __init__(self):
        self.output = None
        
    def predict(self,temp,humidity,windsp):
        weather = 0.5*(temp**2) - 0.2*humidity + 0.1*windsp - 15

        if weather > 300:
            self.output = "Sunny"
        elif 200< weather <= 300:
            self.output = "cloudy"
        elif 100< weather<= 200:
            self.output = "Rainy"
        else:
            self.output = "Stormy"
            
        return self.output
    
if __name__ == '__main__':

    Test_class = Weather()
    
    Test_cases = [[20,70,15],[30,60,10],[20,80,5],[15,90,25]]
    outputs = ["Rainy","Sunny","Rainy","Stormy"]

    predicted_outputs = []
    for conditions in Test_cases:
        predicted_outputs.append(Test_class.predict(conditions[0],conditions[1],conditions[2]))

    print(outputs)
    
    if outputs == predicted_outputs:
        print("All tests passed")
    
