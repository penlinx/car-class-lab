class Car(object):
    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        self.num_of_doors = self.get_num_of_doors()
        self.num_of_wheels = self.get_num_of_wheels()
        
    def get_num_of_doors(self):
        '''Determine car's number of doors
        '''
        if self.name in ['Porshe', 'Koenigsegg']:
            return 2
        else:
            return 4
            
    def get_num_of_wheels(self):
        '''Determine car's number of wheels
        '''
        if self.car_type == 'trailer':
            return 8
        else:
            return 4
            
    def is_saloon(self):
        '''check if car is of type saloon
        '''
        return self.car_type == 'saloon'
        
    def drive(self, moving_speed):
        '''drive car by updating speed
        '''
        if moving_speed == 3:
            self.speed = 1000
        elif moving_speed == 7:
            self.speed = 77

        return self
        