class Car(object):
    
    # initializing car defaults
    def __init__(self, name=None, model=None, _type=None):
        # default speed of a parked car
        self.speed = 0

        # setting default name and model
        if name is None:
            self.name = 'General'
            self.num_of_doors = 4
        else:
            self.name = name

        if model is None:
            self.model = 'GM'
        else:
            self.model = model

        # A saloon is the default car type
        if _type is None:
            self._type = 'saloon'
        else:
            self._type = _type

        # saloons have 4 wheels while trailers have 8
        if _type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        # Porsche & Koennigsegg = 2 doors, default = 4 doors
        if name is not None and (name is 'Porshe' or name is 'Koenigsegg'):
            self.num_of_doors = 2
        elif name is not None and (name is not 'Porshe' or name is not 'Koenigsegg'):
            self.num_of_doors = 4
        else:
            pass

    # check if car is saloon
    def is_saloon(self):
        if self._type == 'saloon':
            return True
        else:
            return False

    # adjsust trailer and saloon speed
    def drive(self, move):
        assert isinstance(move, int), "drive argument has to be an integer"
        if self._type == 'trailer':
            self.speed = move * 11
            return self
        elif self._type == 'saloon':
            self.speed = 10 ** move
            return self
        else:
            pass