import pickle

class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def save_state(self):
        current_state = pickle.dumps(self.__dict__)

        return current_state
    
    def restore_state(self, memento):
        previous_state = pickle.loads(memento)

        self.__dict__.clear()
        self.__dict__.update(previous_state)

    def __str__(self):
        return f"{self.text} \n - By {self.author}"
    
def main():
    print("*** Quote 1 ***")
    q1 = Quote("a room without books is like a body without a soul", "unknown author")
    print(f"\nOriginal version: \n{q1}")
    q1_mem = q1.save_state()

    q1.author = "Marcus Tullius Cicero"
    print(f"\n we found the author, and did an updated:\n{q1}")

    q1.restore_state(q1_mem)
    print(f"\n we had to restore the previous version: \n{q1}")

    print()
    print("*** Quote 2 ***")
    text = ("to be you in a world that is constantly trying to make you be something else is the greatest accomplishment")

    q2 = Quote(text, "Ralph Waldo Emerson")
    print(f"\n original versio: \n{q2}")
    _ = q2.save_state()

    q2.text = ("to be yourself in a world that is constantly trying to make you something else is the greatest accomplishment")
    print(f"\n we fixed the text again: \n {q2}")
    q2_mem2 = q2.save_state()

    q2.text = ("to be yourself when the world is constantly trying to make you something else is the greatest accomplishment")
    print(f"\n we fixed the text again: \n {q2}")

    q2.restore_state(q2_mem2)
    print(f"\n we restored the 2nd version, the correct one: \n{q2}")

if __name__ == "__main__":
    main()