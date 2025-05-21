from external import Musician, Dancer

class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"the club {self.name}"
    
    def organize_event(self):
        return "hires an artist to perform"
    
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)
    
def main():
    objects = [Club("Jazz cafe"), Musician("Chester"), Dancer("Michael")]

    for object in objects:
        if hasattr(object, "play") or hasattr(object, "dance"):
            if hasattr(object, "play"):
                adapted_methods = dict(organize_event=object.play)
            elif hasattr(object, "dance"):
                adapted_methods = dict(organize_event=object.dance)
            
            object = Adapter(object, adapted_methods)
        
        print(f"{object} {object.organize_event()}")

if __name__ == "__main__":
    main()