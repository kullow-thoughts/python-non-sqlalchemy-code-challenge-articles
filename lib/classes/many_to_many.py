class Band:

    all = []
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        Band.all.append(self)


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._name = value
        else:
            raise ValueError("Name cannot be an empty string")
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value: str):
        # Inserting an extra condition to handle corner cases like someone declaring the title as None
        if hasattr(self, '_hometown') and self._hometown is not None:
            raise AttributeError("Hometown can only be set once.")
        if isinstance(value, str) and len(value) >= 1:
            self._hometown = value
        else:
            raise ValueError("Hometown cannot be an empty string.")

    def concerts(self):
        result = []
        for concert in Concert.all:
            if concert.band == self:
                result.append(concert)
        return result


    def venues(self):
        result = set()
        for concert in self.concerts():
            result.add(concert.venue)
        return list(result)

    def play_in_venue(self, venue, date):
        # Takes a `Venue` instance and a date as arguments. Creates and returns a new concert object for the band in that venue on that date
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    # a list of all the concerts
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._date = value
        else:
            raise ValueError("Date cannot be an empty string")
        
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise TypeError("Band must be an instance of the type Band")
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise TypeError("Venue must be an instance of the type Venue")
        
    def hometown_show(self):
        # Making use of a comparison operator to return a boolean
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    # a list of all the Venue objects
    all = []

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        result = []
        for concert in Concert.all:
            if concert.venue == self:
                result.append(concert)
        return result
        

    def bands(self):
        result = set()
        for concert in self.concerts():
            result.add(concert.band)
        return list(result)
    
    # Takes in a date string(parameter)
    def concert_on(self, date):
        # Finds and returns the first concert object on that date at that venue.
        for concert in self.concerts():
            if concert.date == date:
                return concert
        # If there is no concert scheduled return None
        return None