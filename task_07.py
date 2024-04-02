class TrafficLight:
    permissible_values = ['зеленый', 'желтый', 'красный']
    last_values = []

    def __init__(self):
        self.current_signal = 'зеленый'
        TrafficLight.last_values.append(self.current_signal)

    def next_signal(self):
        if self.current_signal == TrafficLight.permissible_values[0]:
            self.current_signal = TrafficLight.permissible_values[1]
            TrafficLight.last_values.append(self.current_signal)
        elif self.current_signal == TrafficLight.permissible_values[2]:
            self.current_signal = TrafficLight.permissible_values[1]
            TrafficLight.last_values.append(self.current_signal)
        else:
            if TrafficLight.last_values[-2] == TrafficLight.permissible_values[0]:
                self.current_signal = TrafficLight.permissible_values[2]
                TrafficLight.last_values.append(self.current_signal)
            else:
                self.current_signal = TrafficLight.permissible_values[0]
                TrafficLight.last_values.append(self.current_signal)
        return self.current_signal


light1 = TrafficLight()
print(light1.current_signal)
print(light1.next_signal())
print(light1.next_signal())
print(light1.next_signal())
print(light1.next_signal())
print(light1.next_signal())
print(light1.next_signal())
print(light1.next_signal())
